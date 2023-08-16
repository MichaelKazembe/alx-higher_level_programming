#!/usr/bin/node

/*
Function returns number of occurrences in a list
*/

exports.nbOccurrences = function (list, searchElement) {
  let occurrences = 0;

  for (let j = 0; j < list.length; j++) {
    if (list[j] === searchElement) {
      occurrences++;
    }
  }
  return occurrences;
};
