#!/usr/bin/node

const request = require('request');

const filmUrl = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(filmUrl, async function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    const chars = JSON.parse(body).characters;
    for (let i = 0; i < chars.length; i++) {
      await request(chars[i], function (err, response, body) {
        if (err) {
          console.error(err);
        } else {
          body = JSON.parse(body);
          console.log(body.name);
        }
      });
    }
  }
});
