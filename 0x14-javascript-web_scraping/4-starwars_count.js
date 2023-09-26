#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Usage: ./4-starwars_count.js <API URL>');
  process.exit(1);
}

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  } else {
    try {
      const filmData = JSON.parse(body);
      const wedgeAntillesFilms = filmData.results.filter((film) =>
        film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
      );
      console.log(wedgeAntillesFilms.length.toString() + "\n"); // Ensure a newline character is added
    } catch (parseError) {
      console.error(parseError);
      process.exit(1);
    }
  }
});
