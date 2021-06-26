import path from 'path'
import webpack from 'webpack'
// import ExtractTextPlugin from 'extract-text-webpack-plugin'

module.exports = {
  entry: './src/index.js',

  output: {
    filename: 'dist.js',
    path: path.resolve(__dirname, 'server/app/static')
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
        use: ['style-loader', 'css-loader', 'less-loader' ]
      },

      {
        test: /\.ts$/,
        use: 'ts-loader'
      }
    ]
  },

  mode: 'development'
}
