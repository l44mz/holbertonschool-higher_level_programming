#!/usr/bin/node

const num = parseInt(process.argv[2]);

if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;

  while (i < num) {
    console.log('C is fun');
    i++;
  }
}
