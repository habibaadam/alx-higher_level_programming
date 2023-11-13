#!/usr/bin/node

const arg = process.argv.slice(2);

const sizeofsquare = parseInt(arg[0]);

if (isNaN(sizeofsquare)) {
  console.log('Missing size');
} else {
  for (let h = 0; h < sizeofsquare; h++) {
    console.log('X'.repeat(sizeofsquare));
  }
}
