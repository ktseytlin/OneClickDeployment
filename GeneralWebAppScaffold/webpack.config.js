const HtmlWebpackPlugin = require('html-webpack-plugin');
const htmlWebpackPluginConfig = new HtmlWebpackPlugin({
  template: `${__dirname}/src/index.html`,
  filename: 'index.html',
  inject: 'body',
});
const webpack = require('webpack');

module.exports = {
  entry: [
    'babel-polyfill',
    'webpack-dev-server/client?http://localhost:3000',
    'webpack/hot/only-dev-server',
    'react-hot-loader/patch',
    './src/index.js',
  ],
  output: {
    path: `${__dirname}/dist/`,
    filename: '[hash].athena_webapp.js',
    publicPath: '',
  },
  devtool: '#cheap-module-eval-source-map',
  module: {
    loaders: [
      { test: /\.js$/, exclude: /node_modules/, loader: 'babel-loader' },
      // inline base64 URLs for <=8k images, direct URLs for the rest
      { test: /\.(png|jpg)$/, loader: 'url?limit=8192' },
      {
        test: /\.(jpe?g|png|gif|svg|css)$/i,
        loaders: [
          'file?hash=sha512&digest=hex&name=[hash].[ext]',
          'image-webpack?bypassOnDebug&optimizationLevel=7&interlaced=false',
        ],
      },
    ],
  },
  plugins: [htmlWebpackPluginConfig,
  new webpack.HotModuleReplacementPlugin()],
};
