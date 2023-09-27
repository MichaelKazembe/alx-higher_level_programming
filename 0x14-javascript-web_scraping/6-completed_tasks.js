#!/usr/bin/node
/*
Computes the number of tasks completed by user ID.
*/

const request = require('request');

const apiUrl = 'https://jsonplaceholder.typicode.com/todos';

request(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const todos = JSON.parse(body);
    const userTasks = {};

    todos.forEach((task) => {
      if (task.completed) {
        if (userTasks[task.userId]) {
          userTasks[task.userId]++;
        } else {
          userTasks[task.userId] = 1;
        }
      }
    });

    console.log(userTasks);
  }
});
