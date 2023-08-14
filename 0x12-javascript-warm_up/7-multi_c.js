#!/usr/bin/node

/*
  This script prints "C is fun" a specified number of times.
  The number of times is determined by the first command-line argument.
  If the argument is not a valid number, it displays an error message.
*/

const num = parseInt(process.argv[2]);

if (!Number.isNaN(num)) {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
