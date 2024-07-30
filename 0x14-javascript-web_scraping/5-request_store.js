#!/usr/bin/node
// fetch urlApi body and write it to a file

const request = require('request');
const fs = require('fs');

const args = process.argv.slice(2);
const urlApi = args[0];
const fileName = args[1];

request.get(urlApi, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(fileName, body, 'utf8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
