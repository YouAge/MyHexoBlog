---
title: DOM的增删改查
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
abbrlink: c229250e
date: 2019-05-04 22:12:00
---


## 增

#### 1. createElement

传件自定义标签，IE8以下浏览器不支持自定义标签
```javascript
let cat = document.createElement('cat')
```
>通过createElement创建的元素并不属于html文档，它只是创建出来，并未添加到html文档中，要调用appendChild或insertBefore等方法将其添加到HTML文档树中;


#### 2. createTexNode

创建一个文本节点
```javascript
var textCont = document.createTextNode('一个textCont')
```
>`createTextNode`接收一个参数，这个参数就是文本节点中的文本，和createElement一样，创建后的文本节点也只是独立的一个节点，同样需要append Child将其添加到HTML文档树中

#### 3. cloneNode
`cloneNode`是用来返回调用方法的节点的一个副本，它接收一个bool参数，用来表示是否复制子元素
```javascript
var parent = document.getElementById("parentElement"); 
var parent2 = parent.cloneNode(true);// 传入true
parent2.id = "parent2";
```
<!-- more -->
#### 4. createDocumentFragment

createDocumentFragment方法用来创建一个DocumentFragment。在前面我们说到DocumentFragment表示一种轻量级的文档，它的作用主要是存储临时的节点用来准备添加到文档中
createDocumentFragment方法主要是用于添加大量节点到文档中时会使用到。假设要循环一组数据，然后创建多个节点添加到文档中

```javascript

<ul id="list"></ul>
<input type="button" value="添加多项" id="btnAdd" />

document.getElementById("btnAdd").onclick = function(){
    var list = document.getElementById("list");
    for(var i = 0;i < 100; i++){
        var li = document.createElement("li");
        li.textContent = i;
        list.appendChild(li);
    }
};
/*
这段代码将按钮绑定了一个事件，这个事件创建了100个li节点，然后依次将其添加HTML文档中。
这样做有一个缺点：每次一创建一个新的元素，然后添加到文档树中，这个过程会造成浏览器的回流。
所谓回流简单说就是指元素大小和位置会被重新计算，如果添加的元素太多，会造成性能问题。
*/
// 修改，保存在内存中，  不会造成回流
document.getElementById("btnAdd").onclick = function(){
    var list = document.getElementById("list");    
    var fragment = document.createDocumentFragment();

    for(var i = 0;i < 100; i++){
        var li = document.createElement("li");
        li.textContent = i;
        fragment.appendChild(li);
    }
    list.appendChild(fragment);
}
/*
优化后的代码主要是创建了一个fragment，每次生成的li节点先添加到fragment，最后一次性添加到list
*/
```

>> - 它们创建的节点只是一个孤立的节点，
>> - 要通过appendChild添加到文档中
>> - cloneNode要注意如果被复制的节点是否包含子节点以及事件绑定等问题
>> - 使用createDocumentFragment来解决添加大量节点时的性能问题
 

## 页面修改，删除

#### 1. appendChild(追加为子元素)
#### 2. insertBefore(插入前面)
#### 3. removeChild(删除子元素)
#### 4. replaceChild(替换子元素)



## 查， 选择器

1. `document.getElementById('box')`   
3. `document.getElementsByTagName('div')`
3. `document.getElementsByClassName('cp')`
4. `document.querySelector('#box')`||`document.querySelectorAll('.cp')`;
5. `document.getElementsByName('x')`; // 返回name属性为x的伪数组




## 元素属性型操作（属性节点的操作）


1. `getAttribute(name)`用于获取元素的属性值
2. `createAttribute(name)`方法生成一个新的属性对象节点，并返回它。
3. `setAttribute(name, value)`方法用于设置元素属性
4. `removeAttribute(name)`用于删除元素属性
5. `element.attributes`（将属性生成数组对象）



## innerText和innerHTML（outerHTML）区别？

- innerText返回的是元素内包含的文本内容（只返回文本节点类型）；
- innerHTML返会元素内HTML结构，包括元素节点、注释节点、文本节点；
- outerHTML返回包括元素节点自身和里面的所有元素节点、注释节点、文本节点；



![js-DOM](/images/js/js-DOM.gif)