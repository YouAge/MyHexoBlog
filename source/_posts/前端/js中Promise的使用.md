---
title: js中Promise的用法
date: 2020-04-14 14:55:00
author: M.
img: false
cover: false
coverImg: false
password: false
toc: true
mathjax: false
summary: false 
categories: 前端
tags: 
  - JavaScript
---

## Promise 的定义

`Promise` 是异步编程的一种解决方案，比传统的解决方案——回调函数和事件——更合理和更强大。它由社区最早提出和实现，`ES6` 将其写进了语言标准，统一了用法，原生提供了`Promise`对象。
所谓`Promise`，简单说就是一个容器，里面保存着某个未来才会结束的事件（通常是一个异步操作）的结果。从语法上说，`Promise` 是一个对象，从它可以获取异步操作的消息。`Promise` 提供统一的 `API`，各种异步操作都可以用同样的方法进行处理。
`Promise`对象有以下两个特点。
（1）对象的状态不受外界影响。`Promise`对象代表一个异步操作，有三种状态：`pending`（进行中）、`fulfilled`（已成功）和 `rejected`（已失败）。只有异步操作的结果，可以决定当前是哪一种状态，任何其他操作都无法改变这个状态。这也是`Promise`这个名字的由来，它的英语意思就是“承诺”，表示其他手段无法改变。
（2）一旦状态改变，就不会再变，任何时候都可以得到这个结果。`Promise`对象的状态改变，只有两种可能：从`pending`变为`fulfilled`和从`pending`变为 `rejected`。只要这两种情况发生，状态就凝固了，不会再变了，会一直保持这个结果，这时就称为 `resolved`（已定型）。如果改变已经发生了，你再对`Promise`对象添加回调函数，也会立即得到这个结果。这与事件（`Event`）完全不同，事件的特点是，如果你错过了它，再去监听，是得不到结果的。
>有了`Promise`对象，就可以将异步操作以同步操作的流程表达出来，避免了层层嵌套的回调函数。此外，Promise对象提供统一的接口，使得控制异步操作更加容易。
## Promise缺点。
>1. 无法取消`Promise`，一旦新建它就会立即执行，无法中途取消。
>2. 如果不设置回调函数，`Promise`内部抛出的错误，不会反应到外部。
>3. 当处于`pending`状态时，无法得知目前进展到哪一个阶段（刚刚开始还是即将完成）。


## Promise 的用法

```javascript
const promise = new Promise((resolve, reject) => {
  let status = true;
  if (status) {
    resolve('操作成功!');
  } else {
    reject('操作失败!');
  }
});

promise.then(res => {
  console.log('成功结果：' + res);
}, error => {
  console.log('失败结果：' + error);
  
});

```

`Promise`构造函数接受一个函数作为参数，该函数的两个参数分别是`resolve`和`reject`。它们是两个函数，由 `JavaScript` 引擎提供，不用自己部署

>`resolve`函数的作用是，将`Promise`对象的状态从“未完成”变为“成功”
>`reject`函数的作用是，将`Promise`对象的状态从“未完成”变为“失败”（即从 `pending` 变为 `rejected`）
在异步操作失败时调用，并将异步操作报出的错误，作为参数传递出去。

`Promise`实例生成以后，可以用`then`方法分别指定`resolved`状态和`rejected`状态的回调函数。
`then`方法可以接受两个回调函数作为参数。
>第一个回调函数是`Promise`对象的状态变为`resolved`时调用，
>第二个回调函数是`Promise`对象的状态变为`rejected`时调用。(可选)

```javascript
const promise = new Promise((resolve, reject) => {
  console.log('new Promise()');
  resolve();
});

promise.then(() => {
  console.log('resolve()');
});
console.log('End');

// 输出结果
//new Promise()
// End
// resolve()
```
上面代码中，`Promise` 新建后立即执行，所以首先输出的是`Promise`。然后，`then`方法指定的回调函数，将在当前脚本所有同步任务执行完才会执行，所以`resolved`最后输出。




### Promise.prototype.then() 

`Promise` 实例具有`then`方法，也就是说，`then`方法是定义在原型对象`Promise`.`prototype`上的。它的作用是为 `Promise` 实例添加状态改变时的回调函数。前面说过，`then`方法的第一个参数是`resolved`状态的回调函数，第二个参数（可选）是`rejected`状态的回调函数。

>then方法返回的是一个新的Promise实例（注意，不是原来那个Promise实例）。因此可以采用链式写法，即then方法后面再调用另一个then方法

```javascript
new Promise((resolve, reject) => {
  resolve('成功返回');
}).then(res => {
  console.log(res); // 成功返回
});
```
then方法的基础调用写法，可以写一个回调方法，来执行成功后的回调。then方法返回一个的是一个新的Promise实例，因此我们可以采用链式写法，即then方法后面再调用一个then方法。
```javascript
new Promise((resolve, reject) => {
  resolve('成功返回');
}).then(res => {
  return res // 成功返回
}).then(res=>res).then(res=>{console.log(res)})// 成功返回
```

### Promise.prototype.catch() 

> 发生错误的回调函数,
>`Promise`实例当状态改变为`rejected`状态或者操作失败抛出异常错误，就会被`catch`方法捕获。所以在`Promise`实例中`reject`方法等同于抛出错误。如果`Promise`的状态已经变成了`resolved`，再抛出错误无效

```javascript
new Promise((resolve, reject) => {
  reject('失败');
}).catch(error => {
  console.log(error); // 失败
});

new Promise((resolve, reject) => {
  reject('失败');
  throw new Error('抛出异常'); // 这行无效
}).catch(error => {
  console.log(error); // 失败
});
```

### Promise的finally方法

> 不管`Promise`最后状态如何，都会回调执行

```javascript
new Promise((resolve, reject) => {
  resolve();
}).then(res => {
  console.log('success');
}).catch(error => {
  console.log('error');
}).finally(() =>{
  console.log('finally');
})
```

### Promise的all方法
>`Promise.all`方法用于将多个`Promise`实例，包装成一个新的`Promise`实例。在`all`方法中可以传递多个`Promise`对象，当所有的Promise对象状态都返回`fufilled`，才会返回`fulfilled`，否则返回`rejected`。

```javascript
const promise1 = new Promise((resolve, reject) => {
  resolve();
});
const promise2 = new Promise((resolve, reject) => {
  resolve();
});
const promise3 = new Promise((resolve, reject) => {
  resolve();
});
const promiseAll = Promise.all([promise1, promise2, promise3]).then(res => {
  console.log('all');
})

```


### Promise的race方法

> 和`all` 差不多， 只是， **只要有一个有一个实例率先改变状态，那么race的状态就会跟着改变**

```javascript
const promise1 = new Promise((resolve, reject) => {
  reject();
});
const promise2 = new Promise((resolve, reject) => {
  resolve();
});
const promise3 = new Promise((resolve, reject) => {
  reject();
});

const promiseRace = Promise.race([promise1, promise2, promise3]).then(res => {
  console.log('race then');
}).catch(error => {
  console.log('race catch');
})
```


[ECM6](https://es6.ruanyifeng.com/#docs/promise#Promise-all)



