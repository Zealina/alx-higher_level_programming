#!/usr/bin/node
let maxPrint = parseInt(process.argv[2]);
if (!isNaN(maxPrint)) {
  while (maxPrint > 0) {
    console.log('C is fun');
    maxPrint--;
  }
} else {
  console.log('Missing number of occurrences');
}
