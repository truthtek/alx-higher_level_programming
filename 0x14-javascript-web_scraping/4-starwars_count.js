#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18; // Wedge Antilles character ID

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const moviesWithCharacter = data.results.filter((movie) => {
      return movie.characters.some((charUrl) => charUrl.endsWith(`/${characterId}/`));
    });
    console.log(moviesWithCharacter.length);
  }
});
