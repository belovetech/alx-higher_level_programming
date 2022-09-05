#!/usr/bin/node

const argc = process.argv.length;

if (argc === 3) console.log('Arguement found');
else if (argc > 3) console.log('Arguements found');
else console.log('No arguement');
