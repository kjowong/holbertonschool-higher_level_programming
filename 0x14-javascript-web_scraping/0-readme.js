#!/usr/bin/node
// script that reads and prints the content of a file
const fs = require('fs');

fs.readFile(process.argv[2], function (err, file) {
  if (err) {
    return console.error(err);
  } else {
    process.stdout.write(file.toString());
  }
});
