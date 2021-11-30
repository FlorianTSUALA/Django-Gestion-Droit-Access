$(function () {

    /* FUNCTIONS */
    var load_form = function () {
        btn = $(this)
        console.log(btn.attr("data-url"))
        if(btn.attr("data-url") == undefined)
          return
        $.ajax({
            url: btn.attr("data-url"), 
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
              $("#modal-gestionnaire").modal("show")
            },
            success: function (data) {
              $("#modal-gestionnaire .modal-content").html(data.html_form)
              $("#modal-gestionnaire .modal-content .select2").select2();
              console.log('Yes Inset done')
            }
        })
    }

    var save_form = function () {
        var form = $(this)
        $.ajax({
          url: form.attr("action"),
          data: form.serialize(),
          type: form.attr("method"),
          dataType: 'json',
          success: function (data) {
            if (data.form_is_valid) {
              $("#gestionnaire-table tbody").html(data.html_gestionnaire_list)
              $("#modal-gestionnaire").modal("hide")
            }
            else {
              $("#modal-gestionnaire .modal-content").html(data.html_form)
            }
          }
        })
        return false
      }

    /* EVENTS */

    //CREATE
    $("#modal-gestionnaire").on("submit", ".js-gestionnaire-create-form", save_form)
    $(".js-create-gestionnaire").click(load_form)

    $("#chat-circle, #chat-box-toggle, #chat-popup").click(function(){
      load_form(this)
      // $("#chat-box-body").toggleClass("show");
    });

    //UPDATE
    $("#gestionnaire-table").on("click", ".js-update-gestionnaire", load_form)
    $("#modal-gestionnaire").on("submit", ".js-gestionnaire-update-form", save_form)

    //DELETE
    $("#gestionnaire-table").on("click", ".js-delete-gestionnaire", load_form)
    $("#modal-gestionnaire").on("submit", ".js-gestionnaire-delete-form", save_form)

});