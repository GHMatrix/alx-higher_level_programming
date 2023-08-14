#!/usr/bin/node

const arg = process.argv[2];

if (!arg || isNaN(arg) || parseInt(arg) <= 0) {
  console.log('Missing size');
} else {
  const size = parseInt(arg);

  for (let i = 0; i < size; i++) {
    let row = '';
    for (let j = 0; j < size; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
