#!/usr/bin/node

const myArg = parseInt(process.argv[2]);
if (!myArg) {
  console.log('Missing size');
} else if (myArg > 0) {
  for (let i = 0; i < myArg; i++) {
    for (let j = 0; j < myArg; j++) {
      process.stdout.write('X');
    }
    console.log('');
  }
}
