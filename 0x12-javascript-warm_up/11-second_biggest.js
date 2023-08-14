#!/usr/bin/node
const arg = process.argv;
let biggest = 0;
let sBiggest = 0;

for (let i = 2; arg[i]; i++) {
  const temp = parseInt(arg[i]);
  if (temp > biggest) {
    sBiggest = biggest;
    biggest = temp;
  }
}
if (!arg[3]) {
  sBiggest = 0;
}
console.log(sBiggest);
