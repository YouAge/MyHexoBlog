---
title: npm项目初始化
date: 2020-05-11 00:23:00
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
  - npm
---


## 初始化环境

1. `npm init` 初始化项目， 一值 ent
2. 创建 `scr` 文件夹 `index.js  `  /  `index.html`

3. `npm install webpack  webpack-cli -save-dev`

4.  创建 `webpack.dev.config.js`  配置

```javascript
module.exports ={
    entry: './scr/index.js',  // 入口文件路径
    output:{
        path: __dirname,
        filename:'./releasse/bundle.js'    // 
    }

}
```

5. `npm install webpack-dev-server html-webpack-plugin --save-dev`

6. `npm i bacbel-core babel-loader babel-polyfill babel-preset-es2015 babel-prset-latest`

`.babelrc`
```javascript


```




