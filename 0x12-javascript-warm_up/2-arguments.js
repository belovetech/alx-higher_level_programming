#!/usr/bin/node

const argc = process.argv.length;

if (argc <= 2) console.log('No arguement');
if (argc === 3) console.log('Arguement found');
if (argc > 3) console.log('Arguements found');
