var path = require('path');
var webpack = require('webpack');
const MiniCssPlugin = require('mini-css-extract-plugin');

module.exports = {
  entry: './src/main.ts',
  output: {
    path: path.resolve(__dirname, './public/js/'),
    publicPath: '/public/js/',
    filename: 'bundle.js'
  },
  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: 'vue-loader',
        options: {
          loaders: {
			      ts:  [
				      {
					      loader: 'ts-loader',
					      options: {
					        appendTsSuffixTo: [/\.vue$/]
			      	   }
			        }
            ]
          },
          // other vue-loader options go here
          transpileDependencies: ['vuex-module-decorators']
        }
      },
      {
        test: /\.js$/,
        loader: 'babel-loader',
        exclude: /node_modules/
      },
    //   {
    //     test: /\.(png|jpg|gif|svg)$/,
    //     loader: 'file-loader',
    //     options: {
	// 		name: 'assets/[folder]/[name].[ext]',
	// 		esModule: false,
    //     }
	//   },
	  {
		test: /\.(png|jpg|gif|svg)$/,
		use: {
			loader: 'url-loader',
			options: {
				esModule: false,
			},
		},
	  },
	  {
        test: /\.(css)$/,
        use: ['vue-style-loader',
			{
		  	loader: 'css-loader',
		  	options: {
				// enable CSS Modules
				modules: true,
				// customize generated class names
				localIdentName: '[local]_[hash:base64:8]'
		  	}
			}
		],
      },
	  {
        test: /\.ts$/,
        use: 'ts-loader',
        exclude: /node_modules/,
	  },
    ]
  },
  plugins: [
  ],
  performance: {
    hints: false
  },
  devtool: '#eval-source-map'
}

if (process.env.NODE_ENV === 'production')
{
  module.exports.devtool = '#source-map'

  module.exports.plugins = (module.exports.plugins || []).concat([
    new webpack.DefinePlugin({
      'process.env': {
        NODE_ENV: '"production"'
      }
    }),
    new webpack.optimize.UglifyJsPlugin({
      sourceMap: true,
      compress: {
        warnings: false
      }
    }),
    new webpack.LoaderOptionsPlugin({
      minimize: true
    })
  ])
}