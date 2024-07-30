#!/usr/bin/node
// fetch urlApi body and calculate completer task for each user

const request = require('request');

const args = process.argv.slice(2);
const urlApi = args[0];

const data = {};

request.get(urlApi, { json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  for (const user of body) {
    if (isNaN(data[user.userId])) {
      data[user.userId] = 0;
    }
    if (user.completed === true) {
      data[user.userId] = data[user.userId] + 1;
    }
  }
  console.log(data);
});
