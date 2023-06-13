#!/usr/bin/node
const firstArg = parseInt(process.argv[2]);
if (isNaN(firstArg)) {
  console.log('Missing size');
} else {
  for (let y = 0; y < firstArg; y++) {
    console.log('X'.repeat(firstArg));
  }
}
