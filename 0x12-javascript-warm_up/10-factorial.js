#!/usr/bin/node

function factorial (n) {
  let Res = 1;
  for (let i = 1; i <= n; i++) {
    Res *= i;
  }
  return (Res);
}
console.log(factorial(parseInt(process.argv[2])));
