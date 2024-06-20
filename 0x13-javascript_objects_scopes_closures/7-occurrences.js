#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let repeated = 0;
  for (const number of list) {
    if (number === searchElement) {
      repeated += 1;
    }
  }
  return repeated;
};
