#!/usr/bin/node
const list = require('./100-data.js').list;
console.log(list);

const newList = list.map((item, index) => {
  return item * index;
});
console.log(newList);
