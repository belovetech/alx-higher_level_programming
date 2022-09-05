#!/usr/bin/node

const argv = process.argv;

argv[0] && argv[1] && !argv[2]
  ? console.log('No argument')
  : console.log(argv[2]);
