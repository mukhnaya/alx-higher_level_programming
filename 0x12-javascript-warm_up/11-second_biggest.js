#!/usr/bin/node
const argLen = process.argv.length;
const array1 = [];
if (argLen === 1) {
  console.log(0);
} else {
  for (let x = 0; x < argLen; x++) {
    const argInt = parseInt(process.argv[x]);
    if (isNaN(argInt)) {
      continue;
    } else {
      array1.push(argInt);
    }
    array1.sort(function (a, b) { return b - a; });
    console.log(array1[1]);
  }
}
