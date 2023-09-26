#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      const filmData = JSON.parse(body);
      const wedgeAntillesFilms = filmData.results.filter((film) =>
        film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
      );
      console.log(wedgeAntillesFilms.length);
    } catch (parseError) {
      console.error(parseError);
    }
  }
});
