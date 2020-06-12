---
title: vue双向数据绑定原理
date: 2020-04-29 11:13:00
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
  - vue
  - javaScript
---

# vue数据双向绑定

> VUE2.0 双向绑定底层原理  ES5中的 Object.defineProperty

**简单实现**
```html
 <div> 
    姓名： <span id="name"></span>
    <br>
        <input type="text" id="text">
</div>

<script>
    let obj={ name:''};
    let newobj ={...obj};
    Object.defineProperty(obj,'name',{
        get(){
            // 返回数据， 不能使用 this.name , 会造成死循环， this指向defineProperties
            // 换回一个新值， 将值克隆一份返回
            return newobj.name  
        }
        set(value){
            if(value === obj.name) return;
            newobj.name =value;
            observe();
        }
    });
    function observe() {
      name.innerHTML = obj.name;
        text.value = obj.name
    }
    observe();
    //text, 监听输入框的值改变，赋予obj，是现实双向绑定
    text.oninput= function() {
      obj.name = this.name
    }
/*
1. 对原始数据克隆
2. 需要分别给对象中而定每一个属性设置监听
*/

</script>
```






> VUE 3.0 使用的是 ES6中  Proxy

```html
<script>
let obj={};
obj = new Proxy(obj,{
    get(target,prop){
        console.log('get');
        return target[prop]
    },
    set(target, p, value, receiver) {
        console.log('set');
        target[props] = value;
        observe();
    }
});

   function observe() {
      name.innerHTML = obj.name;
        text.value = obj.name
    }
    observe();
    //text, 监听输入框的值改变，赋予obj，是现实双向绑定
    text.oninput= function() {
      obj.name = this.name
    }

</script>
```



## 订阅者和发布者模式

> 订阅者向消息队列中，订阅消息， 发布者只要发布到队列中，就会被订阅者收到
> 如何实现： 
>1. 初始化，发布者，订阅者
>2. 订阅者需要注册到发布者，发布者发布消息的时候，依次向订阅者发布消息










