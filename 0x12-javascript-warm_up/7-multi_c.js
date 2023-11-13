#!/usr/bin/node

const arg = process.argv.slice(2);

if (arg.length !== 1) {
  console.log('Missing number of occurrences');
} else {
  const h = parseInt(arg[0]);
  if (isNaN(h)) {
    console.log('Missing number of occurrences');
  } else {
    for (let j = 0; j < h; j++) {
      console.log('C is fun');
    }
  }
}
