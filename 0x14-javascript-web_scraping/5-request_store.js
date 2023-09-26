#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

if (!url || !filePath) {
  console.error('Usage: ./5-request_store.js <URL> <output file path>');
  process.exit(1);
}

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  } else {
    try {
      fs.writeFile(filePath, body, 'utf-8', (writeError) => {
        if (writeError) {
          console.error(writeError);
          process.exit(1);
        } else {
          // No additional output, just exit
          process.exit(0);
        }
      });
    } catch (parseError) {
      console.error(parseError);
      process.exit(1);
    }
  }
});
