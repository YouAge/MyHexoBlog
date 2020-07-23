---
title: node-koa.js的post请求
date: 2020-06-15 22:57:00
author: M.
img: false
cover: false
coverImg: false
password: false
toc: true
top: false
mathjax: false
summary: false 
categories: 后端
tags:
  - node
---


## koa.js中路由的理解

```javascript
function router(url){
    let page = '404.html'
    switch(url){
        case '/':
            page='index.html';
        case 'index':
            page='index';
        case '/todo':
            page=''
}   
}
```





1. 方法一

```javascript
router.use('/', async ctx=>{
    if (ctx.method=='GET'){
        ctx.body={msg:"测试成功"}
    }
  
})
```

## Koa-bodyparser 中间件
