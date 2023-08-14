#!/usr/bin/node

/*
  This script computes and prints the factorial of an integer.
*/

function factorial (n) {
  if (n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

const num = parseInt(process.argv[2]);

if (!Number.isNaN(num)) {
  const result = factorial(num);
  console.log(result);
} else {
  console.log(factorial(num));
}
