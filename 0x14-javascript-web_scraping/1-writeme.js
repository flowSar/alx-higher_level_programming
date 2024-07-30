#!/usr/bin/node
// write string to a file

const fs = require('fs');
const args = process.argv.slice(2);
const fileName = args[0];
const stringContent = args[1];

fs.writeFile(fileName, stringContent, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
