#!/usr/bin/node

const request = require('request');

film_url = 'https://swapi-api.alx-tools.com/api/films/';
request(film_url, function (err, response, body) {
	if (err) {
		console.error(err);
	} else {
		body = JSON.parse(body)['result'];
		console.log(body);
	}
});
