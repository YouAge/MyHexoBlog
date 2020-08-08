---
title: js中数组常用方法
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
abbrlink: 98ca42b0
date: 2020-05-02 12:49:00
---



## filter

> 用来过滤数组，返回一个新的数组，filter方法需要在循环的时候判断一下是true还是false，是true才会返回这个元素；
>接收一个方法，该方法可传入三个参数，第一个为数组的一个元素，第二位为该元素的下标，第三个为原数组。

```javascript
let ary = [1,2,3,4,22,44,22,1,90];
let ary2 = ary.filter((value,key,arr)=>{ 
        console.log(value); //=> 值
        console.log(key);  // => 索引
        console.log(arr); // => ary数组
       return value >10? true:false;
    });
console.log(ary); // 不变
console.log(ary2) //[22, 44, 22, 90]
```
**去重**

```javascript
let ary= [2,3,23,12,3,1,2,3,4,56,4];
let new_ary = ary.filter((x,index,self)=>self.indexOf(x)===index)
//new_ary =>[2, 3, 23, 12, 1, 4, 56]
```

<!-- more -->
## map

>map()根据当前数组映射出一个新的数组,可以改变当前循环的值，返回一个新的被改变过值之后的数组（map需return）
>接收一个方法，该方法可传入三个参数，第一个为数组的一个元素，第二位为该元素的下标，第三个为原数组

**一般用来处理需要修改某一个数组的值**
```javascript
let arr = [1,2,3,4,5,6];
let newArr= arr.map((value, index, array)=>value*10)
// newArr => [10, 20, 30, 40, 50, 60]
```


## forEach

>forEach遍历方式遍历数组全部元素，利用回调函数对数组进行操作，自动遍历数组.length次，且无法break中途跳出循环，不可控、不支持return操作输出，return只用于控制循环是否跳出当前循环
>接收一个方法，该方法可传入三个参数，第一个为数组的一个元素，第二位为该元素的下标，第三个为原数组。

**循环**
```javascript
[3,2,4,6].forEach(item=>console.log(item))

```


## some

> 返回 布尔值， true，false，  遍历数组并使用传入参数方法，如果参数方法返回值为false，则继续循环，如果参数方法返回值为true，则终止循环，都不满足为false
>接收一个方法，该方法可传入三个参数，第一个为数组的一个元素，第二位为该元素的下标，第三个为原数组。

```javascript
[1,2,3,4].some(item=>item>3);//>true
[1,2,3,4].some(item=>item<0) // false
```



## reduce





> 数组常用的一些方法
- [].indexOf(item) => 半段该元素是否存在，返回下标，否则 -1 
>**添加新元素**
- [].push(item) => 将一个或多个元素加入数组，返回新数组的长度 
- [].unshift(item) =>将一个或多个元素加入到数组的开始位置，原有元素位置自动后移，返回 新数组的长度
- [].splice(start,delCount,item...) =>从start的位置开始向后删除delCount个元素，然后从start的位置开始插入一个或多个新元素 
**删除元素**
- [].pop()  => 删除最后一个元素，并返回该元素 
- [].shift() => 删除第一个元素，数组元素位置自动前移，返回被删除的元素 
- [].splice(start,delCount) => 从start的位置开始向后删除delCount个元素 
**数组的合并，截取**
- [].slice(start,end) =>  以数组的形式返回数组的一部分，注意不包括 end 对应的元素，如果省略 end 将复制 start 之后的所有元素 
- [].concat(array1,array2) => 将多个数组拼接成一个数组 
**排序**
- [].reverse() => 数组反转 
- [].sort() => 数组排序，返回数组地址 
**拼接成字符串**
- [].join(',') =>  安什么拼接，返回字符串
**根据下标删除元素**
- 使用`splice()` 方法，写道 Array的原型链接上

```javascript
Array.prototype.del =function(index) {
  if (isNaN(index)||index>this.length)return false;
  this.splice(index,1)
};
let a = [1,2,3,4,5];
a.del(3);
console.log(a) //=> [1,2,3,5]
```