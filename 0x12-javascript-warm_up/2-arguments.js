#!/usr/bin/node

const argc = process.argv.length;

if (argc < 3) console.log('No arguement');
else if (argc === 3) console.log('Arguement found');
else console.log('Arguements found');
