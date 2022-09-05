#!/usr/bin/node

const argCount = process.argv.length;

if (argCount < 3) {
  console.log('No arguement');
} else if (argCount === 3) {
  console.log('Arguement found');
} else {
  console.log('Arguements found');
}
