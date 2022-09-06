#!/usr/bin/node

const fs = require('fs');

const argv = process.argv;

fs.readFile(argv[2], 'utf8', function (err, data1) {
  if (err) throw err;

  fs.readFile(argv[3], 'utf-8', function (err, data2) {
    if (err) throw err;

    fs.writeFile(argv[4], `${data2.toString() + data1.toString()}`, err => {
      if (err) throw err;
    });
  });
});
