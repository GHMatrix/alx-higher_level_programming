#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./100-starwars_characters.js <Movie ID>');
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
      const characterUrls = movieData.characters;

      // Function to fetch character names and print them
      function fetchAndPrintCharacters(urls, index) {
        if (index >= urls.length) {
          return;
        }

        request.get(urls[index], (charError, charResponse, charBody) => {
          if (!charError) {
            const characterData = JSON.parse(charBody);
            console.log(characterData.name);
            fetchAndPrintCharacters(urls, index + 1);
          } else {
            console.error(charError);
            process.exit(1);
          }
        });
      }

      fetchAndPrintCharacters(characterUrls, 0);
    } catch (parseError) {
      console.error(parseError);
      process.exit(1);
    }
  }
});
