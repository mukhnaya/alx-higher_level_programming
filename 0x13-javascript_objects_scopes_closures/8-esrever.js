#!/usr/bin/node
exports.esrever = function (list) {
  const list1 = [];
  for (let k = list.length - 1; k >= 0; k--) {
    list1.push(list[k]);
  }
  return list1;
};
