// Define the URL to fetch the translation data
const apiUrl = 'https://fourtonfish.com/hellosalut/?lang=fr';

// Make an AJAX GET request to the API
$.get(apiUrl, function (data) {
  // Select the <div> element with id 'hello' and display the translation
  $('#hello').text(data.hello);
});
