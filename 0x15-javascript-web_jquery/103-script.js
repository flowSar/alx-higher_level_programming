
$(function () {
  $('INPUT#language_code').keydown(function (event) {
    const lang = $('INPUT#language_code').val();
    if (event.key === 'Enter') {
      $.getJSON(`https://hellosalut.stefanbohacek.dev/?lang=${lang}`, function (data) {
        $('DIV#hello').text(data.hello);
      });
    }
  });

  $('INPUT#btn_translate').click(function () {
    const lang = $('INPUT#language_code').val();
    $.getJSON(`https://hellosalut.stefanbohacek.dev/?lang=${lang}`, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
