#!/usr/bin/node

const argv = process.argv;
console.log(
  `${isNaN(argv[2]) ? 'Not a number' : `My number: ${Math.trunc(argv[2])}`} `
);
