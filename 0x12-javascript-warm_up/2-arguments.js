#!/usr/bin/node

/*
Prints message depending of the number of arguments passed
*/
const args = process.argv.slice(2);
const numOfArgs = args.length;

if (numOfArgs === 0) {
  console.log('No argument');
} else if (numOfArgs === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
