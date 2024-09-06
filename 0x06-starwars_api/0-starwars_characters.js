#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

if (!movieId) {
  console.log('Usage: ./0-starwars_characters.js <movieId>');
  process.exit(1);
}

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const data = JSON.parse(body);
  const characters = data.characters;

  const fetchCharacter = (url, callback) => {
    request(url, (error, response, body) => {
      if (error) {
        callback(error);
        return;
      }
      const character = JSON.parse(body);
      callback(null, character.name);
    });
  };

  let count = 0;
  characters.forEach((url) => {
    fetchCharacter(url, (error, name) => {
      if (error) {
        console.error(error);
        return;
      }
      console.log(name);
      count++;
      if (count === characters.length) {
        process.exit(0);
      }
    });
  });
});
