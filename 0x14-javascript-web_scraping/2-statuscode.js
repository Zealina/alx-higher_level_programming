#!/usr/bin/node

let request = require('request');

request(process.argv[2], function (err, response, body) {
	console.log('code:' + response.statusCode)
});
