#!/usr/bin/node

const request = require('request-promise-native');
const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

if (!movieId) {
  console.log('Usage: ./0-starwars_characters.js <movieId>');
  process.exit(1);
}

async function getCharacters() {
  try {
    const response = await request(apiUrl);
    const data = JSON.parse(response);
    const characters = data.characters;

    for (const characterUrl of characters) {
      const characterResponse = await request(characterUrl);
      const characterData = JSON.parse(characterResponse);
      console.log(characterData.name);
    }
  } catch (error) {
    console.error(error);
  }
}

getCharacters();
