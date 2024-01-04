#!/usr/bin/node

const request = require('request');

url = 'https://jsonplaceholder.typicode.com/todos';
request(url, function (err, response, body) {
	body = JSON.parse(body);
	let dict = {};
	for (let i = 0; i < body.length; i++) {
		if (!dict[body[i]['userId']]) {
			dict[body[i]['userId']] = 1;
		} else {
			dict[body[i]['userId']] += 1;
		}
	}
	console.log(dict);
});
