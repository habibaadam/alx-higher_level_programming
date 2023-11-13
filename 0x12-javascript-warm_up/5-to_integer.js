#!/usr/bin/node

const inputArgument = process.argv[2];
const convertedNumber = parseInt(inputArgument);

if (!isNaN(convertedNumber)) {
  console.log('My number: ' + convertedNumber);
} else {
  console.log('Not a number');
}
