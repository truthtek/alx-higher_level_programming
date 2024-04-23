#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const charactersUrls = data.characters;

    const getCharacters = (urls, index = 0) => {
      if (index >= urls.length) {
        return;
      }

      const url = urls[index];
      request(url, (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          const character = JSON.parse(body);
          console.log(character.name);
          getCharacters(urls, index + 1);
        }
      });
    };

    getCharacters(charactersUrls);
  }
});
