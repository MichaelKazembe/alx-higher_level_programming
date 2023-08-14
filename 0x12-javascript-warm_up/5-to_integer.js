#!/usr/bin/node

/*
An Integer
*/

const argOne = process.argv[2];
const num = parseInt(argOne);

if (!isNaN(num)) {
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
