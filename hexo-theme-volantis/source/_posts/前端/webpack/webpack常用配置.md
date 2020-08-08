---
title: webpack常用配置
author: M.
img: false
cover: false
coverImg: false
password: false
toc: true
top: false
mathjax: false
summary: false
categories: 前端
tags:
  - webpack
abbrlink: c36507d3
date: 2020-03-29 16:59:00
---


## webpack创建项目

1. 项目初始化 npm init （再输入项目）  || npm init -y
2. 下载包 `npm i webpack webpack-cli -D` 开发依赖

>配置 webpack.config.js
```javascript
const path = require('path')
const webpack = require('webpack')
module.exports={
    entry: path.join(__dirname,'./src/main.js'),  // 入口文件，要使用webpack打包的文件
    output:{ // 输出文件相关的配置
        path: path.join(__dirname,'./dist'),
        filenname:'bundle.js' //指定， 输出的文件名称
    },
    devServer:{ // 配置 dev-server命令参数
        open:true ,// 自动打开浏览器
        port: 3000,
        contentBase:'src', // 指定托管的 根目录
        hot: true // 启动热更新，再在 plugins中 new一下
    },
    plugins:[ // 配置插件的节点
        new webpack.HotModuleReplacementPlugin() // new 一个热更新的模块        
    ],
    module:{}
}
```
<!-- more -->
3. `npm i webpack-dev-server` 插件 自动打包编译工具（本地必须安装 `webpack webpack-cli`）,配置 `package.json` 启动命令
4.  `npm i html-webpack-plugin -D` 插件 内存中生产html
```javascript
// --host 页面不刷新更新，--contentBace src 启动文件路径， --open 自动打开， 
// webpack-dev-server --open --port 3000 --contentBace src --host
// 第二中，再配置文件中， webpack.config.js 修改
///=》 在  webpack.config.js 配置
// 导入在内存中生产HTML页面的插件
const htmlWebpackPlugin = require('html-webpack-plugin')
plugins:[
    new webpack.HotModuleReplacementPlugin(), // 热更新
    // 自动创建一一个，script引用正确路径
    new htmlWebpackPlugin({ // 创建一个 在内存中生成的 html
        template:path.join(__dirname,'./src/index.html'), // 指定模板页面，根据指定页面生成内存中
        filename:'index.html' // 指定生成页面的名称
    })
]
```

> `webpack` 默认只能初始js文件， 处理不了css， css文件中的url地址，不管图片还是地址库，只要是url地址， 需要安装 `loader`
>  打包`css`文件安装 `less-loader` `css-loader` `style-loader`  
>  `cnpm -i node-sass sass-loader` 安装
>  `npm -i url-loader file-loader` css中 url路径的的处理
> **在配置文件 webpack.config.js 中 `module`配置**
> webpack处理第三方文件类型的过场：
>   1. 发现要处理的文件不是js文件，然后就去配置文件中， 查找有没有对应的第三方loader 规则
>   2. 如果能倒找对应的规则， 就会调用对应的 loader 处理， 这样文件类型
>   3. 在调用loader的时间，是从后往前调用
>   4. 当最后一个 loader 调用完毕，会把处理的结果，直接交给webpack进行打包合并，最终输出到js文件

```javascript
module:{  // 用于配置所有第三方模板，加速器
    rules:[ //所有第三方模板的比配规则， 参数格式和get请求一样
    {test:/\.css$/,use:['style-loader','css-loader']},    
    {test:/\.less$/,use:['style-loader','css-loader','less-loader']}, // 配置.less文件处理   
    {test:/\.scss$/,use:['style-loader','css-loader','sass-loader']}, // 配置.less文件处理   
    // limit=8000，参数，给定的值是图片的大小byte，如果图片大于或等于给定的limt值，则不会被转成base64格式字符串，如果小于给定的limit值，则会被转成baser64格式
    // name=[name].[ext], 修改文件名，[name].[ext] 原名和原后缀未修改,[hash:8]截取hash值前8位 
    {test:/\.(jpg|png|gif|bmp|jpeg)$/,use:'url-loader?limit=8000&name=[hash:8]-[name].[ext]'} // 处理图片的 路径
    {test:/\.(ttf|eot|svg|woff|woff2)$/,use:'url-loader'}, // 处理字体文件
    {test:/\.js$/,use:'babel-loader',exclude:/node_modules/} // ES高级语法转换
  ]
}
```

### bable的配置

> webpack 中 默认只能处理一部分 ES6 的新语法， 一些更高级的ES6或者ES7语言，webpack是处理不了，这时候需要第三方loader，来处理
> 通过 Babel， 可以将高级的语法转成，低级语法
> `npm i babel-core babel-loader babel-plugin-transform-runtime -D`
> `npm i babel-preset-env babel-preset-stage-0 -D`
>  在配置文件中 配置rules
> /exclude （过滤掉） 不编译 node_modules 里第三方都是已经编译好了的，如在在编译，消费cpu过大
`{test:/\.js$/,use:'babel-loader',exclude:/node_modules/}`
> **在项目根目录，创建 `.babelrc`配置文件** 这个配置文件属于JSON

```javascript
{
"presets": ["env","stage-0"], // 语法
"plugins":["transform-runtime"] // 安装插件名字
}
```



> 工作中 webpack 的常用配置

> 配置一

```javascript
const path = require('path')
const htmlWebpackPlugin = require('html-webpack-plugin')
// 导入每次删除文件夹的插件
const cleanWebpackPlugin = require('clean-webpack-plugin')
const webpack = require('webpack')
// 导入抽取CSS的插件
const ExtractTextPlugin = require("extract-text-webpack-plugin")
// 导入压缩CSS的插件
const OptimizeCssAssetsPlugin = require('optimize-css-assets-webpack-plugin')

module.exports = {
  entry: { // 配置入口节点
    app: path.join(__dirname, './src/main.js'),
    vendors1: ['jquery'] // 把要抽离的第三方包的名称，放到这个数组中
  },
  output: {
    path: path.join(__dirname, './dist'),
    filename: 'js/bundle.js'
  },
  plugins: [ // 插件
    new htmlWebpackPlugin({
      template: path.join(__dirname, './src/index.html'),
      filename: 'index.html',
      minify: {
        collapseWhitespace: true, // 合并多余的空格
        removeComments: true, // 移除注释
        removeAttributeQuotes: true // 移除 属性上的双引号
      }
    }),
    new cleanWebpackPlugin(['dist']),
    new webpack.optimize.CommonsChunkPlugin({
      name: 'vendors1', // 指定要抽离的入口名称
      filename: 'js/vendors.js' // 将来再发布的时候，除了会有一个 bundle.js ，还会多一个 vendors.js 的文件，里面存放了所有的第三方包
    }),
    new webpack.optimize.UglifyJsPlugin({
      compress: { // 配置压缩选项
        warnings: false // 移除警告
      }
    }),
    new webpack.optimize.DedupePlugin({ // 设置为产品上线环境，进一步压缩JS代码
      'process.env.NODE_ENV': '"production"'
    }),
    new ExtractTextPlugin("css/styles.css"), // 抽取CSS文件
    new OptimizeCssAssetsPlugin()// 压缩CSS的插件
  ],
  module: {
    rules: [
      {
        test: /\.css$/, use: ExtractTextPlugin.extract({
          fallback: "style-loader",
          use: "css-loader",
          publicPath: '../' // 指定抽取的时候，自动为我们的路径加上 ../ 前缀
        })
      },
      {
        test: /\.scss$/, use: ExtractTextPlugin.extract({
          fallback: 'style-loader',
          use: ['css-loader', 'sass-loader'],
          publicPath: '../' // 指定抽取的时候，自动为我们的路径加上 ../ 前缀
        })
      },
      { test: /\.(png|gif|bmp|jpg)$/, use: 'url-loader?limit=5000&name=images/[hash:8]-[name].[ext]' },
      { test: /\.js$/, use: 'babel-loader', exclude: /node_modules/ }
    ]
  },
  // 打包时不生成.map文件
  productionSourceMap: false,
  devServer: {
    proxy: 'http://localhost:3000' // 代理
  }
}
```



##  配置2

```javascript
'use strict'
const path = require('path')
const utils = require('./utils')
const config = require('../config')
const vueLoaderConfig = require('./vue-loader.conf')

function resolve (dir) {
  return path.join(__dirname, '..', dir)
}

const createLintingRule = () => ({
  test: /\.(js|vue)$/,
  loader: 'eslint-loader',
  enforce: 'pre',
  include: [resolve('src'), resolve('test')],
  options: {
    formatter: require('eslint-friendly-formatter'),
    emitWarning: !config.dev.showEslintErrorsInOverlay
  }
})

module.exports = {
  context: path.resolve(__dirname, '../'),
  entry: {
    app: ["babel-polyfill", './src/main.js']
  },
  externals: {
    'BMap': 'BMap',
    'BMap_Symbol_SHAPE_POINT': 'BMap_Symbol_SHAPE_POINT'
  },
  output: {
    path: config.build.assetsRoot,
    filename: '[name].js',
    publicPath: process.env.NODE_ENV === 'production'
      ? config.build.assetsPublicPath
      : config.dev.assetsPublicPath
  },
  resolve: {
    extensions: ['.js', '.vue', '.json'],
    alias: {
      'vue$': 'vue/dist/vue.esm.js',
      '@': resolve('src'),
    }
  },
  module: {
    rules: [
      ...(config.dev.useEslint ? [createLintingRule()] : []),
      {
        test: /\.vue$/,
        loader: 'vue-loader',
        options: vueLoaderConfig
      },
      {
        test: /\.js$/,
        loader: 'babel-loader',
        include: [resolve('src'), resolve('test'), resolve('node_modules/webpack-dev-server/client')]
      },
      {
        test: /\.(png|jpe?g|gif|svg)(\?.*)?$/,
        loader: 'url-loader',
        options: {
          limit: 10000,
          name: utils.assetsPath('img/[name].[hash:7].[ext]')
        }
      },
      {
        test: /\.(mp4|webm|ogg|mp3|wav|flac|aac)(\?.*)?$/,
        loader: 'url-loader',
        options: {
          limit: 10000,
          name: utils.assetsPath('media/[name].[hash:7].[ext]')
        }
      },
      {
        test: /\.(woff2?|eot|ttf|otf)(\?.*)?$/,
        loader: 'url-loader',
        options: {
          limit: 10000,
          name: utils.assetsPath('fonts/[name].[hash:7].[ext]')
        }
      }
    ]
  },
  node: {
    // prevent webpack from injecting useless setImmediate polyfill because Vue
    // source contains it (although only uses it if it's native).
    setImmediate: false,
    // prevent webpack from injecting mocks to Node native modules
    // that does not make sense for the client
    dgram: 'empty',
    fs: 'empty',
    net: 'empty',
    tls: 'empty',
    child_process: 'empty'
  }
}
```