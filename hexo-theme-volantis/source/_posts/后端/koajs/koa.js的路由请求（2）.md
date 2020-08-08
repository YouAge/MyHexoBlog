---
title: koa.js的路由请求（2）
author: M.
layout: post 
categories:
  - 后端
  - node
tags:
  - node.js
  - koa.js
abbrlink: 2d20ecd4
date: 2020-06-15 22:57:00
meta:
  header: [title, author, date, category, counter, top]
  footer: [updated, tags, share]
icons: [fas fa-fire red, fas fa-star green]
sidebar: [toc, category, tagcloud,related_posts, qrcode,webinfo]
toc: true
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



<!-- more -->

1. 方法一

```javascript
router.use('/', async ctx=>{
    if (ctx.method=='GET'){
        ctx.body={msg:"测试成功"}
    }
  
})
```

## Koa-bodyparser 中间件
