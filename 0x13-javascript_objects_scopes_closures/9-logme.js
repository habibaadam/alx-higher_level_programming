#!/usr/bin/node

let presentArgs = 0;

exports.logMe = function (newArgs) {
  console.log(presentArgs + ': ' + newArgs);
  presentArgs++;
};
