#!/usr/bin/node
let maxPrint = parseInt(process.argv[2]);
if (!isNaN(maxPrint)) {
  const numOfTimes = maxPrint;
  let output = '';
  for (let i = 0; i < numOfTimes; i++) {
    output += 'X';
  }
  while (maxPrint > 0) {
    console.log(output);
    maxPrint--;
  }
} else {
  console.log('Missing size');
}
