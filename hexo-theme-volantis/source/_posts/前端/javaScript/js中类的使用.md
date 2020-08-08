---
title: js中类的使用
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
abbrlink: bec7cdca
date: 2020-04-15 20:29:00
---

## 类的原理

>在面向对象编程中，类（class）是对象（object）的模板，定义了同一组对象（又称"实例"）共有的属性和方法。
Javascript语言不支持"类"，但是可以用一些变通的方法，模拟出"类"。
> 在 javaScript中， 类的所有实例对象都是从通一个原型对象上继承属性，因此，原型对象是类的核心

<!-- more -->
## 原型链类的继承

