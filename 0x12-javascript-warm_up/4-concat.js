#!/usr/bin/node

/*
Prints two arguments passed to it,
in the following format: “ is ”
*/

const argOne = process.argv[2];
const argTwo = process.argv[3];
console.log(argOne + ' is ' + argTwo);
