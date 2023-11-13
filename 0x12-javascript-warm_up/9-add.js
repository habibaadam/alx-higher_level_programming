#!/usr/bin/node

function add (a, b) {
  return (a + b);
}

const arg = process.argv.slice(2);
const firstinteger = parseInt(arg[0]);
const secondinteger = parseInt(arg[1]);

if (isNaN(firstinteger) || isNaN(secondinteger)) {
  console.log('NaN');
} else {
  console.log(add(firstinteger, secondinteger));
}
