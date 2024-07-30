#!/usr/bin/node
// fetch json data from API

const request = require('request');

const args = process.argv.slice(2);
const id = args[0];

const urlApi = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(urlApi, { json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  console.log(`${body.title}`);
});
