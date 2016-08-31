/* eslint no-console: ["error", { allow: ["warn", "error", "log"] }] */
/* eslint consistent-return: "off"*/

const webpack = require('webpack');
const WebpackDevServer = require('webpack-dev-server');
const config = require('./webpack.config');
const express = require('express');

const app = new WebpackDevServer(webpack(config), {
  publicPath: config.output.publicPath,
  hot: true,
  historyApiFallback: true,
  proxy: {
    '*': {
      target: 'http://localhost:5000',
      secure: false,
      bypass: function bypass(req) {
        if (req.headers.accept.indexOf('html') !== -1) {
          console.log('Skipping proxy for browser request.');
          return '/index.html';
        }
        if (req.headers.accept.indexOf('image') !== -1) {
          console.log('Skipping proxy for image request.');
          return req.url;
        }
      },
    },
  },
  stats: {
    colors: true,
  },
});

app.use('/assets', express.static('assets'));

app.listen(3000, 'localhost', (err) => {
  if (err) {
    console.error(err);
  }

  console.log('Listening at localhost:3000');
});
