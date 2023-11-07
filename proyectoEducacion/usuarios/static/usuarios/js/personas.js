$(function () {
    $(".js-create-persona").click(function () {
        $.ajax({ url: '/usuarios/agregar/', type: 'get', dataType: 'json', beforeSend: function () 
        {$("#modal-persona").modal("show"); }, success: function (data) 
            { $("#modal-persona .modal-content").html(data.html_form); } 
        }); 
    }); 
});