---
title: css权重和属性继承
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
  - css
abbrlink: f4ae9910
date: 2020-05-18 15:02:00
---



### 可继承的样式

1.字体系列属性 font，font-family，font-weight，font-size，font-style，font-variant，font-stretch，font-size-adjust

2.文本系列属性 text-indent，text-align，line-height，word-spacing，letter-spacing，text-transform，direction，color

3.元素可见性 visibility

4.表格布局属性 caption-side，border-collapse，border-spacing，empty-cells，table-layout

5.列表布局属性 list-style-type，list-style-image，list-style-position，list-style

6.生成内容属性 quotes

7.光标属性 cursor

8.页面样式属性 page，page-break-inside，windows，orphans

9.声音样式属性 speak，speak-punctuation，speak-numeral，speak-header，speech-rate，volume，voice-family，pitch，pitch-range，stress，richness，azimuth，elevation

### 优先级算法如何计算

1.优先级就近原则，同权重情况下样式定义最近者为准；

2.载入样式以最后载入的定位为准；

3.!important > id > class > tag；

4.important 比 内联优先级高，但内联比id要高,id比class高

<!-- more -->


### CSS 选择符有哪些

>1.id选择器`（#id）`
2.类选择器`（.class）`
3.标签选择器`（div，h1，p）`
4.相邻选择器`（h1 + p）`
5.子选择器`（ul > li）`
6.后代选择器`（li a）`
7.通配符选择器`（ * ）`
8.属性选择器`（a[title]）`
9.伪类选择器`（a:hover，li:nth-child）`
