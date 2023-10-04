// Wait for the document to be fully loaded before manipulating the DOM
$(document).ready(function () {
  // Define the URL to fetch the character data
  const apiUrl = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

  // Make an AJAX GET request to the API
  $.get(apiUrl, function (data) {
    // Extract the character name from the API response
    const characterName = data.name;

    // Display the character name in the HTML tag with id 'character'
    $('#character').text(characterName);
  });
});
