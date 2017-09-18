#!/usr/bin/node
// script that computes the number of tasks completed by user id
const request = require('request');
const options = {
  url: process.argv[2],
  method: 'GET'
};
request(options, function (error, response, body) {
  let countObj = {};
  if (error) {
    return console.error(error);
  } else {
    for (let i = 0; i < JSON.parse(body).length; i++) {
      if (JSON.parse(body)[i].completed) {
        let count = JSON.parse(body)[i].userId;
        countObj[count] = (countObj[count] || 0) + 1;
      }
    }
  }
  console.log(countObj);
});
