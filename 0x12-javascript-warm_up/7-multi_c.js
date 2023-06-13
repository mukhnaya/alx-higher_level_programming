#!/usr/bin/node
x = parseInt(process.argv[2]);
if (isNaN(x)){
  console.log('Missing number of occurrences');
} else {
  for (y = 0; y < x; y++){
    console.log('C is fun');
  }
}
