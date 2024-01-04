#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    body = JSON.parse(body);
    const dict = {};
    for (let i = 0; i < body.length; i++) {
      if (body[i].completed) {
        if (!dict[body[i].userId]) {
          dict[body[i].userId] = 1;
        } else {
          dict[body[i].userId] += 1;
        }
      }
    }
    console.log(dict);
  }
});
