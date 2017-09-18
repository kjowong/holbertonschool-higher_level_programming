#!/usr/bin/node
// script that prints the title of a Star Wars movie where the episode
// number matches a given integer
const request = require('request');
const options = {
  url: process.argv[2],
  method: 'GET'
};
request(options, function (error, response, body) {
  if (error) {
    return console.log(error);
  } else {
    let count = 0;
    for (let item of JSON.parse(body).results) {
      for (let character of item.characters) {
        if (character.includes(18)) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
