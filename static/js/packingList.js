$('#start_date').val(start_day);
$('#end_date').val(end_day);
fetch_data(start_day, end_day);
function fetch_data(start_date='', end_date='')
{
     start_date = set_yyyymmdd(start_date);
     end_date = set_yyyymmdd(end_date);
     var LOOKUP_TABLE = {
          "stepOne": function(args) {
            return setStepOneDataTable(args);
          },
          "stepTwo": function() {
            return setStepTwoDataTable(args);
          },
          "stepThree":  function() {
            return setStepThreeDataTable(args);
          },
          "stepFour":  function() {
            return setStepFourDataTable(args);
          },
          "stepFive":  function() {
            return setStepFiveDataTable(args);
          },
          "stepSix":  function() {
            return setStepSixDataTable(args);
          }
     };

    let gubunFilter = $('#tabnavigator a.nav-link.active').attr('href');
    gubunFilter = gubunFilter.substring(1);
    let releaseTypeFilter = $('.type_filter #releaseType_List select').val();
    let productTypeFilter = $('.type_filter #releaseProduct_List select').val();
    let locatoinTypeFilter = $('.type_filter #releaseLocation_List select').val();
    let table = $('#'+gubunFilter +' .datatable');
    var args={
            'table' : table,
            'start_date' : start_date,
            'end_date' : end_date,
            'releaseTypeFilter':releaseTypeFilter,
            'productTypeFilter':productTypeFilter,
            'locatoinTypeFilter':locatoinTypeFilter,
             'gubunFilter': gubunFilter };
    table.DataTable().destroy();
    console.log(args);
    LOOKUP_TABLE[gubunFilter](args);
}

function setStepOneDataTable(args)
{
    table = args['table'].DataTable({
        "select": true,
        "processing": true,
        "serverSide": true,
        "ajax": {
            "url": "/api/packingList/",
            "type": "GET",
            "data": {
                start_date:args['start_date'],
                end_date:args['end_date'],
                releaseTypeFilter:args['releaseTypeFilter'],
                productTypeFilter:args['productTypeFilter'],
                locatoinTypeFilter:args['locatoinTypeFilter'],
                gubunFilter:args['gubunFilter']
                }
        },
        "responsive" : true,
        "columnDefs": [
            { responsivePriority: 1, targets: 0 },
            { responsivePriority: 3, targets: -1, orderable: false },
        ],
        "columns": [
            {"data": "id"},
            {"data": "type", "render" : function(data, type, row, meta){return setTypeButton(data);}},
            {"data": "ymd"},
            {"data": "code"},
            {"data": "codeName"},
            {"data": "locationCode_code"},
            {"data": "locationCodeName"},
            {"data": "count" , "render": $.fn.dataTable.render.number( ',')},
            {"data": "price" , "render": $.fn.dataTable.render.number( ',')},
            {"data": "memo"},
            {"data": null, "render": function(data, type, row, meta){return setDataTableActionButton();}}
        ],
        stateSave:  true,
        dom: 'Bfrtip',
        buttons: [
                    {
                        extend: 'pageLength',
                        className:'btn btn-light',
                        text : '<i class="fas fa-list-ol fa-lg"></i>',
                        init : function(api, node, config){
                            $(node).removeClass('btn-secondary');
                        }
                    },
                    {
                        extend: 'colvis',
                        className:'btn btn-light',
                        text : '<i class="far fa-eye fa-lg"></i>',
                        init : function(api, node, config){
                            $(node).removeClass('btn-secondary');
                        }
                    },
                    {
                        extend: 'copy',
                        className:'btn btn-light',
                        text : '<i class="fas fa-copy fa-lg"></i>',
                        init : function(api, node, config){
                            $(node).removeClass('btn-secondary');
                        }
                    },
                    {
                        extend: 'excel',
                        className:'btn btn-light',
                        text : '<i class="far fa-file-excel fa-lg"></i>',
                        init : function(api, node, config){
                            $(node).removeClass('btn-secondary');
                        }
                    }],        buttons: [
                    {
                        extend: 'pageLength',
                        className:'btn btn-light',
                        text : '<i class="fas fa-list-ol fa-lg"></i>',
                        init : function(api, node, config){
                            $(node).removeClass('btn-secondary');
                        }
                    },
                    {
                        extend: 'colvis',
                        className:'btn btn-light',
                        text : '<i class="far fa-eye fa-lg"></i>',
                        init : function(api, node, config){
                            $(node).removeClass('btn-secondary');
                        }
                    },
                    {
                        extend: 'copy',
                        className:'btn btn-light',
                        text : '<i class="fas fa-copy fa-lg"></i>',
                        init : function(api, node, config){
                            $(node).removeClass('btn-secondary');
                        }
                    },
                    {
                        extend: 'excel',
                        className:'btn btn-light',
                        text : '<i class="far fa-file-excel fa-lg"></i>',
                        init : function(api, node, config){
                            $(node).removeClass('btn-secondary');
                        }
                    }],
        lengthMenu : [[30, 50, -1], [30, 50, "All"]]
    });
}

function setStepTwoDataTable(args)
{
    releaseTable = args['table'].DataTable({
        "language": {
        "lengthMenu": "_MENU_ 페이지당 개수",
        "zeroRecords": "결과 없음",
        "info": "",
        "infoEmpty": "No records available",
        "infoFiltered": "(검색된결과 from _MAX_ total records)"
        },
         "createdRow": function( row, data, dataIndex ) {
            $( row ).find('td:eq(0)').attr('data-title','포장재명');
            $( row ).find('td:eq(1)').attr('data-title','재고수량');
         },
        "paging": false,
        "processing": true,
        "serverSide": true,
        "ajax": {
            "url": "/api/packing/",
            "type": "GET"
        },
        "columns": [
            {"data": "packing_codeName"},
            {"data": "totalCount" , "render": $.fn.dataTable.render.number( ',')},
        ],
        dom: 'Bfrtip',
        buttons: [
                    {
                        extend: 'pageLength',
                        className:'btn btn-light',
                        text : '<i class="fas fa-list-ol fa-lg"></i>',
                        init : function(api, node, config){
                            $(node).removeClass('btn-secondary');
                        }
                    },
                    {
                        extend: 'colvis',
                        className:'btn btn-light',
                        text : '<i class="far fa-eye fa-lg"></i>',
                        init : function(api, node, config){
                            $(node).removeClass('btn-secondary');
                        }
                    },
                    {
                        extend: 'copy',
                        className:'btn btn-light',
                        text : '<i class="fas fa-copy fa-lg"></i>',
                        init : function(api, node, config){
                            $(node).removeClass('btn-secondary');
                        }
                    },
                    {
                        extend: 'excel',
                        className:'btn btn-light',
                        text : '<i class="far fa-file-excel fa-lg"></i>',
                        init : function(api, node, config){
                            $(node).removeClass('btn-secondary');
                        }
                    }],        buttons: [
                    {
                        extend: 'pageLength',
                        className:'btn btn-light',
                        text : '<i class="fas fa-list-ol fa-lg"></i>',
                        init : function(api, node, config){
                            $(node).removeClass('btn-secondary');
                        }
                    },
                    {
                        extend: 'colvis',
                        className:'btn btn-light',
                        text : '<i class="far fa-eye fa-lg"></i>',
                        init : function(api, node, config){
                            $(node).removeClass('btn-secondary');
                        }
                    },
                    {
                        extend: 'copy',
                        className:'btn btn-light',
                        text : '<i class="fas fa-copy fa-lg"></i>',
                        init : function(api, node, config){
                            $(node).removeClass('btn-secondary');
                        }
                    },
                    {
                        extend: 'excel',
                        className:'btn btn-light',
                        text : '<i class="far fa-file-excel fa-lg"></i>',
                        init : function(api, node, config){
                            $(node).removeClass('btn-secondary');
                        }
                    }],
    });
}

function setStepThreeDataTable(args)
{
    eggReportTable = args['table'].DataTable({
        "language": {
        "lengthMenu": "_MENU_ 페이지당 개수",
        "zeroRecords": "결과 없음",
        "info": "",
        "infoEmpty": "No records available",
        "infoFiltered": "(검색된결과 from _MAX_ total records)"
        },
        "processing": true,
        "serverSide": true,
        "ajax": {
            "url": "/api/packingReport/",
            "type": "GET",
            "data": {
                start_date:args['start_date'],
                end_date:args['end_date']
                }
        },
        "columns": [
            {"data": "codeName"},
            {"data": "previousStock" , "render": $.fn.dataTable.render.number( ',')},
            {'data': 'in', "render": $.fn.dataTable.render.number( ',')},
            {'data': 'in_price', "render": $.fn.dataTable.render.number( ',')},
            {'data': 'insert', "render": $.fn.dataTable.render.number( ',')},
            {'data': 'loss', "render": $.fn.dataTable.render.number( ',')},
            {'data': 'release', "render": $.fn.dataTable.render.number( ',')},
            {'data': 'adjust', "render": $.fn.dataTable.render.number( ',')},
            {'data': 'currentStock', "render": $.fn.dataTable.render.number( ',')}
        ],
        dom: 'Bfrtip',
        buttons: [
                    {
                        extend: 'pageLength',
                        className:'btn btn-light',
                        text : '<i class="fas fa-list-ol fa-lg"></i>',
                        init : function(api, node, config){
                            $(node).removeClass('btn-secondary');
                        }
                    },
                    {
                        extend: 'colvis',
                        className:'btn btn-light',
                        text : '<i class="far fa-eye fa-lg"></i>',
                        init : function(api, node, config){
                            $(node).removeClass('btn-secondary');
                        }
                    },
                    {
                        extend: 'copy',
                        className:'btn btn-light',
                        text : '<i class="fas fa-copy fa-lg"></i>',
                        init : function(api, node, config){
                            $(node).removeClass('btn-secondary');
                        }
                    },
                    {
                        extend: 'excel',
                        className:'btn btn-light',
                        text : '<i class="far fa-file-excel fa-lg"></i>',
                        init : function(api, node, config){
                            $(node).removeClass('btn-secondary');
                        }
                    }],        buttons: [
                    {
                        extend: 'pageLength',
                        className:'btn btn-light',
                        text : '<i class="fas fa-list-ol fa-lg"></i>',
                        init : function(api, node, config){
                            $(node).removeClass('btn-secondary');
                        }
                    },
                    {
                        extend: 'colvis',
                        className:'btn btn-light',
                        text : '<i class="far fa-eye fa-lg"></i>',
                        init : function(api, node, config){
                            $(node).removeClass('btn-secondary');
                        }
                    },
                    {
                        extend: 'copy',
                        className:'btn btn-light',
                        text : '<i class="fas fa-copy fa-lg"></i>',
                        init : function(api, node, config){
                            $(node).removeClass('btn-secondary');
                        }
                    },
                    {
                        extend: 'excel',
                        className:'btn btn-light',
                        text : '<i class="far fa-file-excel fa-lg"></i>',
                        init : function(api, node, config){
                            $(node).removeClass('btn-secondary');
                        }
                    }],
        lengthMenu : [[30, 50, -1], [30, 50, "All"]]
    });
}

function setTypeButton(data)
{
    switch(data)
    {
        case '입고':
            return '<button class="btn btn-dark btn-sm">'+ data +'</button>'
            break;
        case '생산':
            return '<button class="btn btn-warning btn-sm">'+ data +'</button>'
            break;
        case '폐기':
            return '<button class="btn btn-danger btn-sm">'+ data +'</button>'
            break;
        case '조정':
            return '<button class="btn btn-primary btn-sm ">'+ data +'</button>'
            break;
    }
}

$(document).on('click', "#releasePacking tbody tr", function()
{
    let data = releaseTable.row($(this)).data();
    manualReleaseModal(data);
});

function manualReleaseModal(data)
{
    console.log(data);
    $("#id_type").val("생산").change();
    $("#id_code").val(data['code']);
    $("#id_fakeYmd").val("");
    $('#id_count').val("").attr("max",data['totalCount']);
    $('#id_memo').val("");
    $("#Modal").modal();
}
function editButtonClick(data)
{
    console.log(data);
    $('#modify_id_count').val(data['count']).removeAttr( "min" );
    $('#modify_id_price').val(data['price']).removeAttr("required");
    $('#modify_id_memo').val(data['memo']);
    $('.codeName').text(data['codeName']);
    $("#eggModifyModal").modal();
}

function deleteButtonClick(data)
{
    $('#modal_title').text('DELETE');
    $("#confirm").modal();
}

function pdfButtonClick(data)
{
    console.log(data);
    let ymd = data['ymd'];
    let locationCode = data['locationCode'];
    let moneyMark = $("#moneyMark").is(":checked");
    window.open('/eggs/pdf?ymd=' + ymd + '&locationCode=' + locationCode + "&moneyMark=" + moneyMark, '_blank');
}

$('.deleteAndEdit').on('submit', function (e)
{
    e.preventDefault();
    $this = $(this);
    let type = $this.find('.ajaxUrlType').val();
    let data = $this.serialize();
    let url = '/api/packing/'+id;

    $.ajax({
    url: url,
    type: type,
    data: data,
    }).done(function(data) {
        alert('완료');
        $('#stepOne .datatable').DataTable().search($("input[type='search']").val()).draw();
        $(".everyModal").modal('hide');
    }).fail(function() {
        alert('수정 에러 전산실로 문의바랍니다.');
    });
});


$('#manualRelease').on('submit', function (e)
{
    e.preventDefault();
    $this = $(this);
    let type = $this.find('#id_type').val();
    let fakeYmd = set_yyyymmdd($this.find('#id_fakeYmd').val());
    $this.find('#id_ymd').val(fakeYmd);
    let data = $this.serialize();
    $.ajax({
    url: '/packing/release',
    type: 'post',
    data: data,
    }).done(function(data) {
        alert('수정완료');
        $(".everyModal").modal('hide');
        $('#stepTwo .datatable').DataTable().search($("input[type='search']").val()).draw();
    }).fail(function() { alert('수정 에러 전산실로 문의바랍니다.'); });
});