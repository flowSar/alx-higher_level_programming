#!/usr/bin/node
// get response code

const request = require('request');

const args = process.argv.slice(2);
const url = args[0];


request.get(url, (error, response) => {
  if (error) {
    console.error(error);
  }
  console.log(`code: ${response.statusCode}`);
});
