#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    let achilles = 0;
    body = JSON.parse(body);
    const episodes = body.results;
    for (let i = 0; i < episodes.length; i++) {
      const chars = episodes[i].characters;
      for (let j = 0; j < chars.length; j++) {
        const id = chars[j].slice(-3, -1);
        if (id === '18') {
          achilles += 1;
        }
      }
    }
    console.log(achilles);
  }
});
