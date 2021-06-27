import path from 'path'
import webpack from 'webpack'
import HtmlWebpackPlugin from 'html-webpack-plugin'
import TerserPlugin from "terser-webpack-plugin"
// import ExtractTextPlugin from 'extract-text-webpack-plugin'


const isProduction = process.env.NODE_ENV == 'production'
const isDevelopment = !isProduction

module.exports = {
  context: path.resolve(__dirname, 'src'),
  
  entry: './index.js',

  output: {
    path: path.resolve(__dirname, 'dist'),

    filename: 'index.js',
  },


  module: {
    rules: [
      {
        test: /\.jsx?/,
        include: [
          path.resolve(__dirname, 'src')
        ],
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/react'],
            // plugins: []
          }
        }
      },

      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader']
      },

      {
        test: /\.less$/,
        use: ['style-loader', 'css-loader', 'less-loader']
      },

      {
        test: /\.ts$/,
        use: 'ts-loader'
      }
    ]
  },

  plugins: [].concat(
    isProduction ? [] :
    [
      new HtmlWebpackPlugin({
        title: 'Frontend App',
        template: './mock/index.html'
      }) 
    ]
  ),

  devServer: {
    contentBase: path.join(__dirname, 'dist'),

    port: 9000,

    hot: true,

    proxy: {
      '/api': 'http://localhost:5000',
    },
  },

  optimization: {
    minimize: isProduction,
    
    minimizer: [
      new TerserPlugin({ extractComments: !isProduction })
    ]
  },

  mode: isProduction ? 'production' : 'development'
}
