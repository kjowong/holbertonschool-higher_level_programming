#!/usr/bin/node
// script that gets the content of a webpage and stores it in a file
const request = require('request');
const fs = require('fs');

const options = {
  url: process.argv[2],
  method: 'GET'
};
request.get(options).on('error', function (err) {
  console.log(err);
}).pipe(fs.createWriteStream(process.argv[3]));
