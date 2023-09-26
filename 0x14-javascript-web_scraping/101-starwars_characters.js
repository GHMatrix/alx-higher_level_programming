#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./101-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  } else {
    try {
      const movieData = JSON.parse(body);

      // Function to fetch and print characters in the same order
      function fetchAndPrintCharacters(characterUrls, index) {
        if (index >= characterUrls.length) {
          return;
        }

        request.get(characterUrls[index], (charError, charResponse, charBody) => {
          if (!charError) {
            const characterData = JSON.parse(charBody);
            console.log(characterData.name);
            fetchAndPrintCharacters(characterUrls, index + 1);
          } else {
            console.error(charError);
            process.exit(1);
          }
        });
      }

      // Start fetching and printing characters
      fetchAndPrintCharacters(movieData.characters, 0);
    } catch (parseError) {
      console.error(parseError);
      process.exit(1);
    }
  }
});
