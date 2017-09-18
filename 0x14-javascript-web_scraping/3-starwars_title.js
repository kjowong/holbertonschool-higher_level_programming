#!/usr/bin/node
// script that prints the title of a Star Wars movie where the episode
// number matches a given integer
const request = require('request');
const options = {
  url: 'http://swapi.co/api/films/' + process.argv[2],
  method: 'GET'
};
request(options, function (error, response, body) {
  if (error) {
    return console.error(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
