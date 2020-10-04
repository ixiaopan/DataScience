const path = require('path')
const HtmlWebpackPlugin = require('html-webpack-plugin')
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

const isProduction = process.env.NODE_ENV ==='production'

module.exports = {
  entry: './src/index.js',

  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: isProduction ? 'static/js/[name].js' : '[name].js',
  },

  module: {
    rules: [
      {
        test: /\.less$/,
        loader: [ MiniCssExtractPlugin.loader, 'css-loader', 'less-loader' ]
      },

      {
        test: /\.css$/,
        loader: [ MiniCssExtractPlugin.loader, 'css-loader' ]
      },

      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: ['babel-loader']
      }
    ]
  },

  devtool: isProduction ? false : 'cheap-module-source-map',

  optimization: {
    minimize: isProduction,

    splitChunks: {
      chunks: 'all'
    }
  },

  plugins: [
    
    new HtmlWebpackPlugin({
      template: 'public/index.html',
    }),

    new MiniCssExtractPlugin({
      filename: isProduction ? 'static/css/[name].css' : '[name].css'
    }),

  ]
}
