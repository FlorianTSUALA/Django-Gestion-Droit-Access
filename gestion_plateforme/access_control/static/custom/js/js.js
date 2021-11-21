+function ($) {
    'use strict'

    $("#chat-circle, #chat-box-toggle, #chat-popup").click(function(){
        $("#chat-box-body").toggleClass("show");
    });
      
  }(jQuery) //