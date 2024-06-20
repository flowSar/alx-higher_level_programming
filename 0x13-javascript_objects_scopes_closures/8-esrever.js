#!/usr/bin/node

exports.esrever = function (list) {
  const middle = list.length / 2;
  let j = list.length - 1;
  for (let i = 0; i < middle; i++) {
    const tmp = list[i];
    list[i] = list[j];
    list[j] = tmp;
    j--;
  }
  return list;
};
