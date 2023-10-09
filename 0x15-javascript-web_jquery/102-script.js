$(function() {
  $('#btn_translate').click(function() {
    const baseUrl = 'https://www.fourtonfish.com/hellosalut/hello/?lang=';
    var languageCode = $('#language_code').val();
    var apiUrl = baseUrl + languageCode;
    $.get(apiUrl, function(data) { 
      $('#hello').text(data.hello);
    });
  });
});
