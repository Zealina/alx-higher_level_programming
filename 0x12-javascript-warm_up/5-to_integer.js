#!/usr/bin/node
const arg = process.argv;
const value = parseFloat(arg[2]);

if (!isNaN(value) && arg[2] === value.toString()) {
  console.log('My number: ', Math.floor(value));
} else {
  console.log('Not a number');
}
