#!/usr/bin/node

const arg = process.argv[2];
if (isNaN(arg) === true) {
  console.log('Missing number of occurrences');
} else {
  for (let j = 0; j < arg; j++) {
    console.log('C is fun');
  }
}
