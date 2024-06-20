#!/usr/bin/node

let list = []
exports.logMe = function (item) {
  list.push(item);
  console.log(`${list.indexOf(item)}: ${item}`);
}
