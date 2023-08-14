#!/usr/bin/node

/*
  This script prints "C is fun" a specified number of times.
  The number of times is determined by the first command-line argument.
  If the argument is not a valid number, it displays an error message.
*/

const args = process.argv.slice(2);

if (args.length !== 1) {
  console.log('Missing number of occurrences');
} else {
  const num = parseInt(args[0]);

  if (isNaN(num)) {
    console.log('Missing number of occurrences');
  } else {
    for (let i = 0; i < num; i++) {
      console.log('C is fun');
    }
  }
}
