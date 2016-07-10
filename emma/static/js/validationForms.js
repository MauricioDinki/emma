$(document).ready(function () {
  $('.dashboard-special-form').toArray().forEach(function (elem, index) {
    var form = $(elem);

    form.find('.show-as-text').attr('disabled', '');

    form.find('.edit-button').click(function () {
      $(this).addClass('hide');
      $(this).siblings('.cancel-button').removeClass('hide');
      $(this).siblings('.send-button').removeClass('hide');
      form.find('.emma-input.show-as-text')
        .removeClass('show-as-text')
        .addClass('show-as-default');
      form.find('.show-as-default')
        .removeAttr('disabled');
    });

    form.find('.cancel-button').click(function () {
      $(this).addClass('hide');
      $(this).siblings('.edit-button').removeClass('hide');
      $(this).siblings('.send-button').addClass('hide');
      form[0].reset();
      form.find('.emma-input.show-as-default')
        .addClass('show-as-text')
        .removeClass('show-as-default');
      form.find('.show-as-text')
        .attr('disabled', '');
    });
  });

  /* Contract Adult Form
  ---------------------------------------------------------------------------*/
  var $contractAdultForm = $('#contract-adult-form');
  $contractAdultForm.validate({
      rules: {
        name: {
          required:true
        },
        last_name: {
          required:true
        },
        birthday: {
          required:true
        },
        description: {
          required:true
        },
        doctor_name: {
          required:true
        },
        doctor_phone: {
          required:true,
          number:true
        },
        doctor_cp: {
          required:true
        }
      },
      highlight: function(element, errorClass) {
        $(element).removeClass(errorClass);
      },
      submitHandler: function(form)  {
        $('.contract-adult-loader').show();
        form.submit();
      }
    });

  /* Contract Location Form
  ---------------------------------------------------------------------------*/
  var $contractLocationForm = $('#contract-location-form');
  $contractLocationForm.validate({
      rules: {
        street: {
          required:true
        },
        num_ext: {
          required:true,
          number:true
        },
        num_int: {
          required:false,
          number:true
        },
        colony: {
          required:true
        },
        delegation: {
          required:true
        },
        cp: {
          required:true,
          number:true
        },
        address_reference: {
          required:true
        },
        day_1: {
          required:true
        },
        day_1_hour: {
          required:true
        },
        start_date: {
          required:true
        },
        start_time: {
          required:true
        }
      },
      highlight: function(element, errorClass) {
        $(element).removeClass(errorClass);
      },
      submitHandler: function(form)  {
        $('.contract-location-2-loader').show();
        form.submit();
      }
    });

  /* Contract Form
  ---------------------------------------------------------------------------*/
  var $contractForm = $('#contract-form');
  $contractForm.validate({
	    rules: {
        "contract-service-workshop": {
          required: true,
          minlength: 1
        },
		    "contract-service": {
          required: true,
          minlength: 1
        }
	    },
	    messages: {
        "contract-service-workshop": "Selecciona al menos 1 Taller",
		    "contract-service": "Selecciona 1 Servicio"
	    },
			highlight: function(element, errorClass) {
	      $(element).removeClass(errorClass);
	    },
			submitHandler: function(form)  {
	      $('.contract-alert').hide();
	      $('.contract-loader').show();
	      form.submit();
	    }
		});
  
  /* Request Password Form
  ---------------------------------------------------------------------------*/
  var $passwdForm = $('#passwd-form');
  $passwdForm.validate({
    rules: {
      new_password_1: {
        required: true
      },
      new_password_2: {
        required: true,
        equalTo: "#id_new_password_1"
      }
    },
    highlight: function(element, errorClass) {
      $(element).removeClass(errorClass);
    },
    submitHandler: function(form)  {
      $('.passwd-alert').hide();
      $('.passwd-loader').show();
      form.submit();
    }
 });

  /* Request Password Form
  ---------------------------------------------------------------------------*/
  var $passwdReset = $('#passwd-reset-form');
  $passwdReset.validate({
    rules: {
      new_password1: {
        required: true
      },
      new_password2: {
        required: true,
        equalTo: "#id_new_password1"
      }
    },
    highlight: function(element, errorClass) {
      $(element).removeClass(errorClass);
    },
    submitHandler: function(form)  {
      $('.passwd-reset-alert').hide();
      $('.passwd-reset-loader').show();
      form.submit();
    }
 });

  /* Request Password Request Form
  ---------------------------------------------------------------------------*/
  var $passwdResetReq = $('#passwd-reset-req-form');
  $passwdResetReq.validate({
    rules: {
      email: {
        email: true,
        required: true
      }
    },
    highlight: function(element, errorClass) {
      $(element).removeClass(errorClass);
    },
    submitHandler: function(form)  {
      $('.passwd-reset-req-alert').hide();
      $('.passwd-reset-req-loader').show();
      form.submit();
    }
 });

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
    groups: {
        timeGroup: "hour minute"
    },
    rules: {
      hour: {
        number: true,
        maxlength: 12,
        minlength: 1,
        required: true
      },
      minute: {
        checkDateTime: true,
        number: true,
        maxlength: 59,
        minlength: 0,
        required: true
      },
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
  
  /* Pay Form
  ---------------------------------------------------------------------------*/
  var $payForm = $('#pay-form');
  $payForm.validate({
    highlight: function(element, errorClass) {
        $(element).removeClass(errorClass);
    },
    submitHandler: function(form)  {
      $('.pay-loader').show();
      form.submit();
    }
  });
  
  /* Contact Form
  ---------------------------------------------------------------------------*/
  var $contactForm = $('#contactForm');
  $contactForm.validate({
    errorClass: "errorWhite",
    onkeyup: false,
    onfocusout: false,
    highlight: function(element, errorClass) {
        $(element).removeClass(errorClass);
    },
    submitHandler: function(form)  {
      $('.emma-modal-loader').show();
      form.submit();
    }
  });

  /* Contact Form
  ---------------------------------------------------------------------------*/
  var $joinForm = $('#joinForm');
  $joinForm.validate({
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
    },
    submitHandler: function(form)  {
      $('.join-loader').show();
      form.submit();
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
    range: jQuery.validator.format("Inserte un valor entre {0} y {1}."),
    max: jQuery.validator.format("Inserte un valor menor o igual que {0}."),
    min: jQuery.validator.format("Inserte un valor mayor o igual que {0}.")
  });

  jQuery.validator.addMethod("checkDateTime", function(value, element) {

    var date = new Date();
    var actual_time = (date.getHours() *60) + date.getMinutes();
    console.log("El timepo en minutos actuales son: " + actual_time);

    var hours = parseInt($('#hourInput').val());
    var minutes = parseInt($('#timeInput').val());
    var time = $('#reservation-time-button').val();
    var total_minutes = (hours * 60) + minutes;
    if (time == 'PM') {
      total_minutes += 720;
    }
    console.log("Los minutos en la hora de la cita son: " + total_minutes);

    // Validamos que este dentro del horario de servicio
    if (total_minutes > 1200 || total_minutes < 540) {
      console.log("No esta en el horario de atención");
      return false; // No esta dentro del horario
    } else { // Si esta dentro del horario
      if ((actual_time + 45) <  total_minutes) {
        return true
      } else {
        console.log("Esta en un tiempo invalido");
        return false
      }
    }
  }, "La hora no es valida");
  
  jQuery.validator.setDefaults({
    highlight: function(element, errorClass) {
      $(element).removeClass(errorClass);
    },
    submitHandler: function (form) {
      if ($(form).find('.form-loader').length) {
        $(form).find('.form-loader').show();
      }
      if ($(form).find('.form-alert').length) {
        $(form).find('.form-alert').hide();
      }
      form.submit();
    }
  });
  $('#dashboard-user-form').validate();
});