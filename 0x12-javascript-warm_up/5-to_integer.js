#!/usr/bin/node
firstArg = parseInt(process.argv[2]);
if (isNaN(firstArg)) {
  console.log('Not a number');
} else {
  console.log('My number: ',process.argv[2]);
}
