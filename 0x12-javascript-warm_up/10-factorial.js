#!/usr//bin/node

function factorial (n) {
  if (isNaN(n)) {
    return 1;
  }
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const arg = process.argv[2];
const input = parseInt(arg);
console.log(factorial(input));
