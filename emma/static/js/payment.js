$(document).ready(function() {
  OpenPay.setId('mg0kzdwsiduimlfaudun');
  OpenPay.setApiKey('pk_106c640a77f94dd49bae11cf94937075');
  OpenPay.setSandboxMode(true);
	var deviceSessionId = OpenPay.deviceData.setup("addcard-form", "devsessionid");
});

$('#pay-button').on('click', function(event) {
  event.preventDefault();
  $("#pay-button").prop("disabled", true);
  OpenPay.token.extractFormAndCreate(
    'addcard-form', success_callbak, error_callbak
  );
});

	var success_callbak = function(response) {
		var token_id = response.data.id;
		$('#token_id').val(token_id);
		$('#addcard-form').submit();
		console.log("Bien Hecho");
	};

	var error_callbak = function(response) {
		$('.addcard-alert').show();
		$("#pay-button").prop("disabled", false);
		var desc = response.data.description != undefined ? response.data.description : response.message;
		console.log(desc);
		console.log("Mal Hecho");
	};