#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, response, body) {
	if (err) {
		console.error(err)
	} else {
		console.log('Rspnc: ' + reponse)
		console.log('Body: ' + body)
	}
})
