$(document).ready(function () {

  /* Signup Form
  ---------------------------------------------------------------------------*/
  var $signupForm = $('#signup-form');
  $signupForm.validate({
    rules: {
      email: {
        email: true,
        required:true
      },
      password_1: {
        required:true
      },
      password_2: {
        required:true,
        equalTo: "#id_password_1"
      },
      name: {
        required:true
      },
      last_name: {
        required:true
      }
    },

    highlight: function(element, errorClass) {
        $(element).removeClass(errorClass);
    },
    submitHandler: function(form)  {
      $('.signup-alert').hide();
      $('.signup-loader').show();
      form.submit();
    }
  });

  
  /* Login Form
  ---------------------------------------------------------------------------*/
  var $loginForm = $('#login-form');
  $loginForm.validate({
    rules: {
      username: {
        email: true
      }
    },
    highlight: function(element, errorClass) {
      $(element).removeClass(errorClass);
    },
    submitHandler: function(form)  {
      $('.login-alert').hide();
      $('.login-loader').show();
      form.submit();
    }
 });
  
  
  /* Date Form
  ---------------------------------------------------------------------------*/
  var $dateForm = $('#dateForm');
  $dateForm.validate({
    rules: {
      number: {
        number: true,
        maxlength: 10
      }
    },
    highlight: function(element, errorClass) {
        $(element).removeClass(errorClass);
    },
    submitHandler: function(form)  {
      $('.date-loader').show();
      form.submit();
    }
  });
  
  $('#pay-form').validate({
    highlight: function(element, errorClass) {
        $(element).removeClass(errorClass);
    }
  });

  $('#contactForm').validate({
    errorClass: "errorWhite",
    onkeyup: false,
    onfocusout: false,
    highlight: function(element, errorClass) {
        $(element).removeClass(errorClass);
    }
  });

  $('#joinForm').validate({
    rules: {
      age: {
        number: true,
        maxlength: 2
      },
      phone_movile: {
        number: true,
        maxlength: 10
      },
      phone: {
        number: true,
        maxlength: 10
      }
    },
    highlight: function(element, errorClass) {
        $(element).removeClass(errorClass);
    }
  });

  // Mensajes de error

  jQuery.extend(jQuery.validator.messages, {
    required: "Este campo es obligatorio",
    remote: "Please fix this field.",
    email: "Ingresa una dirección de correo valida",
    url: "Please enter a valid URL.",
    date: "Please enter a valid date.",
    dateISO: "Please enter a valid date (ISO).",
    number: "Ingresa un numero valido",
    digits: "Please enter only digits.",
    creditcard: "Please enter a valid credit card number.",
    equalTo: "Los valores deben coincidir.",
    accept: "Please enter a value with a valid extension.",
    maxlength: jQuery.validator.format("No ingreses mas de {0} caracteres."),
    minlength: jQuery.validator.format("Ingresa al menos {0} caracter."),
    rangelength: jQuery.validator.format("Please enter a value between {0} and {1} characters long."),
    range: jQuery.validator.format("Please enter a value between {0} and {1}."),
    max: jQuery.validator.format("Please enter a value less than or equal to {0}."),
    min: jQuery.validator.format("Please enter a value greater than or equal to {0}.")
  });
  
});