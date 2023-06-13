#!/usr/bin/node
const firstArg = parseInt(process.argv[2]);
if (isNaN(firstArg)) {
  console.log('Not a number');
} else {
  const arg1 = Math.trunc(process.argv[2]);
  console.log('My number:', arg1);
}
