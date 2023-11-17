#!/usr/bin/node

const myArg = parseInt(process.argv[2]);
let i = 0;
if (myArg) {
  while (i < myArg) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
