---
title: js-time时间转换操作
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
abbrlink: 44876dc0
date: 2020-05-06 15:19:00
---


> 将时间戳和时间格式转成，str类型
> 格林尼治2019-03-19T16:00:00.000Z  ==>>  2019-03-20 00:00:00   与北京时间8小时时差

```javascript
let formDate = dateForm=>{
	if (dateForm === '')return '';
	const dateee = new Date(dateForm).toJSON();
	var date = new Date(+new Date(dateee)+ 8 * 3600 * 1000).toISOString().replace(/T/g,' ').replace(/\.[\d]{3}Z/,'');
return date;
}
```
<!-- more -->

```javascript
// 将字符串2019-03-20 00:00:00，转成 Date格式Sat Apr 20 2019 00:00:00 GMT+0800 (中国标准时间)
let getDate= strDate=> { 
  const st = strDate; 
  const a = st.split(" "); 
  const b = a[0].split("-"); 
  const c = a[1].split(":"); 
  const date = new Date(b[0], b[1], b[2], c[0], c[1], c[2]);
  return date; 
}
```



```javascript
// 将时间戳1553547600000  转 //  2019-03-25T21:00:00.000Z
let formatDate = datatime=>{
	let timestamp = datatime;
	let newDate = new Date(datatime)
	// let newDate = new Date(datatime+8*36000*1000)
	newDate.getTime(timestamp*1000)
	// console.log(newDate.toDateString());//Mon Mar 11 2019          
	// console.log(newDate.toGMTString()); //Mon, 11 Mar 2019 06:55:07 GMT 
	// console.log(newDate.toISOString()); //2019-03-11T06:55:07.622Z
	return newDate.toISOString()
}
```


## 时间倒计时


## 时间计时器