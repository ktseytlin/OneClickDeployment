/* eslint no-console: ["error", { allow: ["warn", "error", "log"] }] */

const express = require('express');
const bodyParser = require('body-parser');
const app = express();

// Simulates slow networks
if (process.argv.length >= 2 && (!isNaN(parseInt(process.argv[2], 10)))) {
  app.use((req, res, next) => { setTimeout(next, parseInt(process.argv[2], 10)); });
}

app.use(bodyParser.json()); // support json encoded bodies
app.use(bodyParser.urlencoded({ extended: true }));
app.use('/assets', express.static('assets'));

app.listen(5000, () => {
  console.log('Dev server listening on port 5000!');
});
