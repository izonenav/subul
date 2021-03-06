var today = new Date();
$('input[name="display_date"]').val(today.yyyymmdd());

let loadForm = function () {
    let row = $(this);
    let pk = row.attr("data-id");
    if (pk) {
        $.ajax({
            url: '/labor/egg',
            type: 'get',
            dataType: 'json',
            data: {'pk': pk},
            beforeSend: function () {
                $("#js-complete-modal .modal-body").html("");
                $("#js-complete-modal").modal("show");
            }
        }).done(function (data) {
            $("#js-complete-modal .modal-content").html(data['form'])
        }).fail(function () {
            alert('에러발생: 브라우저 및 PC를 리부팅하세요');
        });
    }
};

let updateform = function (e) {
    e.preventDefault();
    let form = $(this);

    $.ajax({
        url: form.attr("action"),
        data: form.serialize() + "&display_date="+$('input[name="display_date"]').val(),
        type: form.attr("method"),
        dataType: 'json',
    }).done(function (data) {
        $("div.table").html(data.list);
        $("#js-complete-modal").modal("hide");
    }).fail(function () {
        alert('에러발생: 브라우저 및 PC를 리부팅하세요');
    });
};

function getEggsList(){
    $.ajax({
        url: '/labor/egg',
        type: 'get',
        data: {display_date: $('input[name="display_date"]').val()},
    }).done(function (data) {
        $("div.table").html(data.list);
    });
}

$('input[name="display_date"]').change(function () {
   getEggsList();
});

setInterval(getEggsList, 10000);
$("div.table").on("click", "div.row", loadForm);
$("#js-complete-modal").on("submit", ".js-update-form", updateform);
