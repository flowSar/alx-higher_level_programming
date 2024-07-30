#!/usr/bin/node
// read from a file bt using node

const fs = require('fs');
const fileName = process.argv.slice(2)[0];

fs.readFile(fileName, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
