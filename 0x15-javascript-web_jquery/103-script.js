
n() {
	  function fetchTranslation() {
		      var languageCode = $('#language_code').val();
		      var apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + languageCode;
		      $.get(apiUrl, function(data) {
			            $('#hello').text(data.hello);
			          });
		    }
	  $('INPUT#btn_translate').click(function() {
		      fetchTranslation();
		    });

	  $('#language_code').keydown(function(event) {
		      if (event.keyCode === 13) { // 13 corresponds to the ENTER key
			            fetchTranslation();
			          }
		    });
});
