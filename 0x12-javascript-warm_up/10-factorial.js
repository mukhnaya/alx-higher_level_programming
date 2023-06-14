#!/usr/bin/node
function factorial1 (n) {
  let fact = 1;
  if (isNaN(n)) {
    console.log(1);
  } else {
    let y = n;
    for (let x = 0; x < n; x++) {
      fact = fact * y;
      y = y - 1;
    }
    console.log(fact);
  }
}
factorial1(parseInt(process.argv[2]));
