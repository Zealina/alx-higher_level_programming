#!/usr/bin/node

const request = require('request');
const fs = require('fs');

request(process.argv[2], function (err, response, body) {
  if (err) {
    console.err(err);
  } else {
    fs.writeFile(process.argv[3], body, 'utf-8', function (writeErr) {
      if (writeErr) {
        console.error(writeErr);
      }
    });
  }
});
