#!/usr/bin/node

const myArray = process.argv;
if (myArray.length < 4) {
  console.log(0);
} else {
  let biggest = parseInt(myArray[2]);
  let sBiggest = biggest;
  for (let i = 2; myArray[i]; i++) {
    const temp = parseInt(myArray[i]);
    if (temp > biggest) {
      sBiggest = biggest;
      biggest = temp;
    } else if ((temp > sBiggest && temp < biggest) || biggest === sBiggest) {
      sBiggest = temp;
    }
  }
  console.log(sBiggest);
}
