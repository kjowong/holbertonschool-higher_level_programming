#!/usr/bin/node
// script that prints "My number: " if first argument can be converted to an integer
if (!isNaN(process.argv[2])) {
  console.log('My number: ' + process.argv[2]);
} else {
  console.log('Not a number');
}
