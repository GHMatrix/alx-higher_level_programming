// Wait for the document to be fully loaded before manipulating the DOM
$(document).ready(function () {
  // Define the URL to fetch the movies data
  const apiUrl = 'https://swapi-api.alx-tools.com/api/films/?format=json';

  // Make an AJAX GET request to the API
  $.get(apiUrl, function (data) {
    // Select the <ul> element with id 'list_movies'
    const listElement = $('#list_movies');

    // Loop through the movies and add each title to the list
    data.results.forEach(function (movie) {
      // Create a new <li> element with the movie title
      const listItem = $('<li>').text(movie.title);

      // Append the <li> element to the <ul> element
      listElement.append(listItem);
    });
  });
});
