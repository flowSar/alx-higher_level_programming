#!/usr/bin/node
// count number of movies where the character “Wedge Antilles” is present.

const request = require('request');

const args = process.argv.slice(2);
const urlApi = args[0];

let count = 0;
request.get(urlApi, { json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  for (const item of body.results) {
    for (const str of item.characters) {
      if (str.includes('18')) {
        count += 1;
      }
    }
  }
  console.log(count);
});
