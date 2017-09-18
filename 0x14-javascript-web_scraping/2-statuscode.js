#!/usr/bin/node
// script that displays the status code of a GET request
const request = require('request');
request(process.argv[2], function (err, response, body) {
  if (err) {
    return console.log(err);
  }
  console.log('code:', response.statusCode);
});
