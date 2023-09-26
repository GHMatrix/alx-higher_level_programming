#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Usage: ./6-completed-tasks.js <API URL>');
  process.exit(1);
}

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  } else {
    try {
      const tasks = JSON.parse(body);
      const completedTasksByUser = {};

      // Loop through tasks and count completed tasks by user
      for (const task of tasks) {
        if (task.completed) {
          if (completedTasksByUser[task.userId]) {
            completedTasksByUser[task.userId]++;
          } else {
            completedTasksByUser[task.userId] = 1;
          }
        }
      }

      // Print the result in the desired format with single quotes
      const formattedResult = {};
      for (const userId in completedTasksByUser) {
        formattedResult[userId] = completedTasksByUser[userId];
      }
      console.log(JSON.stringify(formattedResult, null, 2).replace(/"/g, "'"));
    } catch (parseError) {
      console.error(parseError);
      process.exit(1);
    }
  }
});
