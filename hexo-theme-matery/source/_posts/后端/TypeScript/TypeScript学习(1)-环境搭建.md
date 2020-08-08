---
title: TypeScript学习(1)-环境搭建
date: 2020-07-24 08:45:00
author: Dong
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
  - TypeScript
  - 环境配置
---




## TypeScript环境安装

### 1.全局安装包

```shell script
npm install typescript tslint ts-node  -g
```



### 2. 项目环境包安装

```shell script
npm install typescript ts-loader -s   #ts编译
npm install clean-webpack-plugin cross-env html-webpack-plugin  webpack webpack-cli webpack-dev-server -s
```

### 3. 项目架构创建

```shell script
mkdir client-type
cd client-type

npm init -y # 直接初始化生成项目（注意刚刚创建项目名的名字（最好全小写），否者初始化出错）
# 成功后 就会出现  package.json
tsc --init # 生成ts配置文件
```

```json
{
  "name": "client-side",
  "version": "1.0.0",
  "description": "source code of ts-learning",
  "main": "./src/index.ts",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "cross-env NODE_ENV=development webpack-dev-server --config ./build/webpack.config.js",
    "build": "cross-env NODE_ENV=production webpack --config ./build/webpack.config.js"
  },
  "keywords": [
    "typescript"
  ],
  "author": "cheo",
  "license": "MIT",
  "dependencies": {
    "clean-webpack-plugin": "^3.0.0",
    "cross-env": "^7.0.2",
    "html-webpack-plugin": "^4.3.0",
    "ts-loader": "^8.0.1",
    "typescript": "^3.9.7",
    "webpack": "^4.43.0",
    "webpack-cli": "^3.3.12",
    "webpack-dev-server": "^3.11.0"
  }
}
```


### 项目结构

```angular2
client-type
    -build
        - webpack.config.js
    -src
        - api    /*项目接口*/
        - assets  /*项目静态资源存放*/
        - config  /*项目的配置文件*/
        - components /*项目组件*/
        - example  /*学习ts代码的编写存放*/ 
        - router  /*项目路由*/
        - views  /*项目视图*/
        - template
            -index.html /*静态模板*/
        - tools     /*项目工具*/
        - utils  /*项目公共方法*/
    - index.ts  /*入口文件*/ 
    - typings
    - package.json 
    - tsconfig.json  /*ts配置文件 tsc --init*/
    - tslint.json
    - package-lock.json
```



### webpack.config.js配置设置

#### 1.入口文件配置,编译后生成名

```js
module.exports={
    entry:'./src/index.ts',
    output:{
            filename:"main.js" // 指定，输出文件名称
        }
}
```

#### 2. 文件导包的后缀省略

> 这样 再导入文件时，只要是这样的文件，后缀都可以省略
> `import  './example/interface_.ts'` => `import  './example/interface_'`

```js
 module.exports={
    resolve:{
        extensions:['.ts','.tsx','.js']
    }
}
```
#### 3. module 文件编译处理

> 编译时， 针对不通的文件换换编译成浏览器能识别的， 
> 对ts文件的转换
> 需要下载相应的扩展包

```js
module.exports={
    module:{
        rules:[{
            test:/\.tsx?$/,
            use:'ts-loader',
            exclude:/node_modules/
        }]
    },
}
```

#### 启动配置

```js
const  {CleanWebpackPlugin} = require("clean-webpack-plugin")
const htmlWebpackPlugin = require('html-webpack-plugin')
const webpack = require('webpack')
module.exports={
    devtool:process.env.NODE_ENV ==='production'? false:  'inline-source-map',
    // 启动端口设置， 代理配置
    devServer:{
        contentBase:'./dist',
        stats:'errors-only',
        compress:false,
        host:'localhost',
        port:8088
    },
    // 一些插件配置
    plugins:[
        new webpack.HotModuleReplacementPlugin() ,// new 一个热更新的模块
        new CleanWebpackPlugin(), // 注意更新后的使用方式，
        new htmlWebpackPlugin({
            template:'./src/template/index.html' ,
            filename: 'index.html' // 指定生成页面的名称
        })

    ]
}
```


### 第一行代码

> 配置完成后， 开始写代码吧

```js
// 再example 目录下 创建一个文件， 写入代码
console.log('hello world');

// index.ts 导入该文件 ，运行
import ./example/xxx
```



**个人学习的一些资料， 文档,视频分享**
>
>
>