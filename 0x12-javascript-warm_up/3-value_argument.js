#!/usr/bin/node

/*
Prints Value of my argument
*/

const args = process.argv[2];

if (args === undefined) {
  console.log('No argument');
} else {
  console.log(args);
}

