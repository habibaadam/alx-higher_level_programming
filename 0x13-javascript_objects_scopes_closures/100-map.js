#!/usr/bin/node

const oldL = require('./100-data').list;
const newL = oldL.map((v, i) => v * i);
console.log(oldL);
console.log(newL);
