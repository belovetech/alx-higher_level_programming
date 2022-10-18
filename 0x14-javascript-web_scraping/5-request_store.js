#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) console.log(err);

  fs.writeFile(process.argv[3], body, 'utf-8', (err) => {
    if (err) console.log(err);
  });
});
