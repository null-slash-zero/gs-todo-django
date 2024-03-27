const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const path = require('path');
const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  context: __dirname,
  entry: './apps/frontend/src/index',
  output: {
    path: path.resolve(__dirname, 'apps/frontend/dist'),
    publicPath: '/static/dist/',
    filename: '[name]-[contenthash].js',
  },
  plugins: [
    new CleanWebpackPlugin(),
    new BundleTracker({ path: __dirname, filename: 'webpack-stats.json' }),
  ],
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: ['babel-loader'],
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader'],
      },
    ],
  },
};
