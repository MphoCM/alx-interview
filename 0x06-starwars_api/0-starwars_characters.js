#!/usr/bin/node

const request = require('request');

/**
 * Fetches and prints the names of actors in a Star Wars movie.
 * @param {string} movieId - The ID of the Star Wars movie.
 */
const printActors = (movieId) => {
  // Making a request to the Star Wars API to get information about the movie
  request('https://swapi-api.hbtn.io/api/films/' + movieId, function (err, res, body) {
    if (err) throw err;
    // Parsing the response body to extract the list of actors in the movie
    const actors = JSON.parse(body).characters;
    // Calling the function to print actors in the exact order
    exactOrder(actors, 0);
  });
};

/**
 * Recursively fetches and prints the names of actors in exact order.
 * @param {string[]} actors - An array of URLs representing the actors in the movie.
 * @param {number} x - The current index in the actors array.
 */
const exactOrder = (actors, x) => {
  // Base case: if x reaches the end of the actors array, return
  if (x === actors.length) return;
  // Making a request to get information about the actor at the current index
  request(actors[x], function (err, res, body) {
    if (err) throw err;
    // Parsing the response body to extract the name of the actor
    console.log(JSON.parse(body).name);
    // Calling exactOrder recursively to process the next actor
    exactOrder(actors, x + 1);
  });
};

// Calling the printActors function with the movie ID provided as a command-line argument
printActors(process.argv[2]);
