#!/usr/bin/node
exports.esrever = function (list) {
  const reversedlist = [];

  for (let h = list.length - 1; h >= 0; h--) {
    reversedlist.push(list[h]);
  }
  return reversedlist;
};
