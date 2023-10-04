// Wait for the document to be fully loaded before manipulating the DOM
$(document).ready(function () {
  // Attach a click event handler to the 'Translate' button
  $('#btn_translate').click(translateHello);

  // Attach a keyup event handler to the 'Language code' input field
  $('#language_code').keyup(function (event) {
    // Check if Enter key (key code 13) is pressed
    if (event.keyCode === 13) {
      translateHello();
    }
  });

  // Function to fetch and display the translation
  function translateHello () {
    // Get the language code entered in the input field
    const languageCode = $('#language_code').val();

    // Define the URL to fetch the translation
    const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;

    // Make an AJAX GET request to the API
    $.get(apiUrl, function (data) {
      // Display the translation in the HTML tag with id 'hello'
      $('#hello').text(data.hello);
    });
  }
});
