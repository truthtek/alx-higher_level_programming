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

    const fetchCharacters = (urls) => {
      const promises = urls.map((url) => {
        return new Promise((resolve, reject) => {
          request(url, (error, response, body) => {
            if (error) {
              reject(error);
            } else {
              const character = JSON.parse(body);
              resolve(character.name);
            }
          });
        });
      });

      Promise.all(promises)
        .then((characterNames) => {
          characterNames.forEach((name) => {
            console.log(name);
          });
        })
        .catch((error) => {
          console.log(error);
        });
    };

    fetchCharacters(charactersUrls);
  }
});
