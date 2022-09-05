#!/usr/bin/node

const argv = process.argv;
console.log(
  `${argv[2] ? `My number: ${Math.trunc(argv[2])}` : 'Not a number'} `
);
