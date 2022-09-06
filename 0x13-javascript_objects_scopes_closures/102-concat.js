#!/usr/bin/node

const fs = require('fs');

const argv = process.argv;

fs.readFile(argv[2], function (err, data1) {
  if (err) throw err;

  fs.readFile(argv[3], function (err, data2) {
    if (err) throw err;

    fs.writeFile(argv[4], `${data2 + '\n' + data1 + '\n'}`, err => {
      if (err) throw err;
    });
  });
});
