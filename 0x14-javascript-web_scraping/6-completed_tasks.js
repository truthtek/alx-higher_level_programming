#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const tasks = JSON.parse(body);
    const completedTasks = {};

    tasks.forEach((task) => {
      if (task.completed) {
        const userId = task.userId;
        if (completedTasks[userId]) {
          completedTasks[userId]++;
        } else {
          completedTasks[userId] = 1;
        }
      }
    });

    console.log(completedTasks);
  }
});
