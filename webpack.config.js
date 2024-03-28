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
        test: /\.tsx?$/,
        exclude: /node_modules/,
        loader: 'babel-loader',
      },
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: ['source-map-loader'],
        enforce: 'pre',
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader'],
      },
    ],
  },
  resolve: {
    extensions: ['.tsx', '.ts', '.js'],
  },
};
