$("#modal-persona").on("submit", ".js-create-persona", function () {
    var form = $(this);
    $.ajax({
        url: form.attr("action"),
        data: form.serialize(),
        type: form.attr("method"),
        dataType: 'json',
        success: function (data) {
            if (data.form_is_valid) {
                alert("La persona fue creada");
            }
            else {
                $("#modal-persona .modal-content").html(data.html_form);
            }
        }
    });
    return false;
});