#!/usr/bin/node
const arg = process.argv;
const value = parseInt(arg[2]);

if (isNaN(value)) {
  console.log('Not a number');
} else {
  console.log('My number: ', value);
}
