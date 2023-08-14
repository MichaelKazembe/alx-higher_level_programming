#!/usr/bin/node

/*
  This script searches for the second biggest integer
  among the command-line arguments.
  If there are no arguments or only one argument, it prints 0.
*/

const args = process.argv.slice(2);
const num = args.length;

if (num <= 1) {
  console.log(0);
} else {
  let numArray = [];
  for (let i = 0; i < num; i++) {
    numArray.push(parseInt(args[i]));
  }
  numArray = numArray.sort((a, b) => b - a);
  console.log(numArray[1]);
}
