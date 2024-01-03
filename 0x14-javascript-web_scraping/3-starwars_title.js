#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.error(err);
  } else if (body) {
    const mapping = JSON.parse(body);
    console.log(mapping.title);
  }
});
