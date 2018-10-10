from django.db import models
from core.models import Code, Detail, Location, Out , TimeStampedModel
from release.models import Release
from django.db.models import Sum

class ProductMaster(models.Model):
    produce_id = models.IntegerField(default=0)
    ymd = models.CharField(max_length=8)
    total_loss_openEgg = models.IntegerField(default=0)
    total_loss_insert = models.IntegerField(default=0)
    total_loss_clean = models.IntegerField(default=0)
    total_loss_fill = models.IntegerField(default=0)
    total_openEgg = models.IntegerField(default=0)
    total_eggUse = models.IntegerField(default=0)
    total_storeInsert = models.IntegerField(default=0)
    total_produceStore = models.IntegerField(default=0)
    total_productAmount = models.IntegerField(default=0)
    total_productCount = models.IntegerField(default=0)

    def __str__(self):
        return self.ymd + '_생산마스터'

class ProductEgg(models.Model):
    EGG_TYPE_CHOICES= (
        ('할란', '할란'),
        ('할란사용', '할란사용'),
        ('공정품투입', '공정품투입'),
        ('공정품발생', '공정품발생'),
    )

    TANK_TYPE_CHOICES= (
        ('01201', 'RAW Tank 전란'),
        ('01202', 'RAW Tank 난황'),
        ('01203', 'RAW Tank 난백'),
        ('01204', 'Past Tank 전란'),
        ('01205', 'Past Tank 난황'),
        ('01206', 'Past Tank 난백'),
        ('01207', 'RAW Tank 등급란 전란'),
        ('01208', 'RAW Tank 등급란 난황'),
        ('01209', 'RAW Tank 등급란 난백'),
    )

    master_id = models.ForeignKey(ProductMaster,
                                  on_delete=models.CASCADE,
                                  related_name='temp')
    ymd = models.CharField(max_length=8)
    type = models.CharField(
        max_length=30,
        choices=EGG_TYPE_CHOICES,
        default='',
    )
    tank = models.CharField(
        max_length=10,
        choices=TANK_TYPE_CHOICES,
        default='01201'
    )
    rawTank_amount = models.IntegerField(default=0)
    pastTank_amount = models.IntegerField(default=0)
    loss_insert = models.FloatField(default=0)
    loss_openEgg = models.FloatField(default=0)
    memo = models.TextField(blank=True)

    def __str__(self):
        return self.type + '_' + self.tank + '(' + self.ymd + ')'

    @staticmethod
    def makeVaildinfo(productEggInfo, memo): # ('이름','실제값') -> ('이름','실제값','메모')
        j = 0
        for info in productEggInfo:  # ('이름','실제값','메모')
            if '메모' in info[0]:
                j += 1
                pass
            else:
                info.append(memo[j])

        return productEggInfo

    @staticmethod
    def insertInfo(main, validInfo):
        for info in validInfo:  # ('이름','실제값','메모')
            if info[1] and '메모' not in info[0]:  # 값이 있으며 AND 메모가 아닌경우
                type, rawOrPastType, tankCode = info[0].split("_")
                productEgg = ProductEgg.objects.create(
                    master_id=main,
                    ymd=main.ymd,
                    type=type,
                    tank=tankCode,
                    memo=info[2],
                )

                if '투입' in type or '사용' in type : #공정품투입 , 할란사용 경우 -number 입력
                    print(type)
                    info[1] = -info[1]

                if 'RawTank' in rawOrPastType:
                    productEgg.rawTank_amount = info[1]
                elif 'PastTank' in rawOrPastType:
                    productEgg.pastTank_amount = info[1]
                productEgg.save()  # TODO 할란 , 할란사용 수율 비례식 계산 필요

    @staticmethod
    def getLossOpenEggPercent(masterInstance):
        total_rawTank_amount = 0
        eggs = ProductEgg.objects.filter(master_id=masterInstance).filter(type='할란')
        for egg in eggs:
            total_rawTank_amount += egg.rawTank_amount

        try:
            for egg in eggs:
                percent = egg.rawTank_amount / total_rawTank_amount
                openEgglossPercent = round(masterInstance.total_loss_openEgg * percent ,2)
                insertlossPercent = round(masterInstance.total_loss_insert * percent, 2)
                egg.loss_openEgg = openEgglossPercent
                egg.loss_insert = insertlossPercent
                egg.save()
        except ZeroDivisionError:
            pass


class ProductCode(Code):
    CONTENT_TYPE_CHOICES= (
        ('전란', '전란'),
        ('난백', '난백'),
        ('난황', '난황'),
        ('X', '없음'),
    )

    STORE_TYPE_CHOICES = (
        ('AP','AP'),
        ('BIB','BIB'),
        ('CT','CT'),
        ('PAC','PAC'),
        ('PKG','PKG'),
        ('TANK','TANK'),
        ('TON','TON'),
        ('TOTE','TOTE'),
        ('', '없음'),
    )

    type = models.CharField(
        max_length=10,
        choices=CONTENT_TYPE_CHOICES,
        default='',
    )

    amount_kg = models.FloatField()
    price = models.IntegerField()
    store_type = models.CharField(
        max_length=10,
        choices=STORE_TYPE_CHOICES,
        default=''
    )
    vat = models.IntegerField(default=0)
    expiration = models.IntegerField(default=0)

    def __str__(self ):
        return self.codeName + '(' + self.code + ')'


class Product(Detail): #TODO 주문 나갈때 Tag 붙이는 필드 필요
    master_id = models.ForeignKey(ProductMaster,
                                  on_delete=models.CASCADE,
                                  related_name='master_id')
    loss_clean = models.FloatField(default=0)
    loss_fill = models.FloatField(default=0)
    '''OEM 상품에 한해서 있는 필드'''
    purchaseYmd = models.CharField(max_length=8, blank=True, null=True)
    purchaseLocation = models.ForeignKey(Location,on_delete=models.CASCADE,related_name='purchase_locationCode', blank=True, null=True)
    purchaseLocationName = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.codeName + '(' + self.ymd + ')'

class ProductAdmin(models.Model):
    RELEASE_TYPE_CHOICES = (
        ('생성','생성'),
        ('판매','판매'),
        ('샘플','샘플'),
        ('증정','증정'),
        ('자손','자손'),
        ('이동','이동'),
    )
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    count = models.IntegerField()
    ymd = models.CharField(max_length=8)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    releaseType = models.CharField(
        max_length=10,
        choices=RELEASE_TYPE_CHOICES,
        default='생성',
    )
    releaseSeq = models.ForeignKey(Release, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.product_id.codeName + '(' + self.ymd + ') _' + self.releaseType


class ProductUnitPrice(TimeStampedModel):
    locationCode = models.ForeignKey(Location, on_delete=models.CASCADE,related_name='location')
    productCode = models.ForeignKey(ProductCode, on_delete=models.CASCADE,related_name='product')
    price = models.IntegerField()


class SetProductMatch(TimeStampedModel):
    setProductCode = models.CharField(max_length=255)
    productCode = models.ForeignKey(ProductCode, on_delete=models.CASCADE)
    price = models.IntegerField()
    saleLocation = models.ForeignKey(Location, on_delete=models.CASCADE)


class SetProductCode(Code):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)