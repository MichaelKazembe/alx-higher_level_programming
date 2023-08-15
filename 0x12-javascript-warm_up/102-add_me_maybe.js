#!/usr/bin/node

/*
Function that increments and calls a function
*/

exports.addMeMaybe = function (number, theFunction) {
  const newNumber = number + 1;
  theFunction(newNumber);
};
