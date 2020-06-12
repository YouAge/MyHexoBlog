---
title: js-数组和对象类型判断
date: 2020-05-18 15:07:00
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
  - javaScript
---


### js 如何判断数组和对象的类型


在使用 `typeOf` 判断的时候 都是 `Object`


> 在es6中 可以使用 `instanceof` `Array.isArray(ary)` `constructor `

```javascript
let art = [1,2,3]
console.log(art instanceof Array)
console.log(art.constructor === Array)
console.log(Array.isArray(art))
```

>考虑兼容性问题可以使用 `Object.prototype.toString.call()`来判断

```javascript
Object.prototype.toString.call(art) === "[object Array]"

// 如果是对象{}
Object.prototype.toString.call(art) === "[object object]"
```