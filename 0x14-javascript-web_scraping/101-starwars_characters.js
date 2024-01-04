#!/usr/bin/node

const request = require('request');
const { promisify } = require('util');

const promisifiedRequest = promisify(request);

const fetchData = async () => {
  const filmUrl = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

  try {
    const filmResponse = await promisifiedRequest(filmUrl);
    const chars = JSON.parse(filmResponse.body).characters;

    for (let i = 0; i < chars.length; i++) {
      const charResponse = await promisifiedRequest(chars[i]);
      const character = JSON.parse(charResponse.body);
      console.log(character.name);
    }
  } catch (err) {
    console.error(err);
  }
};

fetchData();
