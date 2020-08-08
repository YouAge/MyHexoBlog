---
title: nodejs环境配置
date: 2020-06-12 23:49:00
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
  - node.js
  - 环境配置
---




node.js 相关配置



### node.js Windons安装配置

```python
官网下载直接安装（选择路径安装）
找到安装路径，下创建2个文件
node_cache, node_gloal
然后在cmd中输入
npm config set prefix "D:\Program Files\nodejs\node_global"
npm config set cache "D:\Program Files\nodejs\node_cache"

在在环境配置中修改
系统变量中 添加 
NODE_PATH   D:\Program Files\nodejs\node_cache
个人变量中path 中把原来的npm路径修改 成 D:\Program Files\nodejs\node_global
这样下载的全局安装就会在node_global 文件中 
```




### npm 修改源
```javascript
// 设置 淘宝镜像源
npm config set registry https://registry.npm.taobao.org

// 查看 使用的 镜像源
npm config get registry

// 安装 淘宝镜像源
npm install -g cnpm --registry=https://registry.npm.taobao.org
```




### centos下安装

```shell script
稳定版：
1. 软件预存：
$ yum clean all && yum makecache fast
$ yum install -y gcc-c++ make
$ curl -sL https://rpm.nodesource.com/setup_10.x | sudo -E bash -

2. sudo yum install nodejs -y

3. node -v， npm -v

最新版安装：
$ yum clean all && yum makecache fast
$ yum install -y gcc-c++ make
$ curl -sL https://rpm.nodesource.com/setup_12.x | sudo -E bash -
```




### 相关包安装

```python
一. nrm 安装
	1. npm i nrm -g全局安装`nrm`包；
	2. nrm ls查看当前所有可用的镜像源地址以及当前所使用的镜像源地址；
	3. nrm use npm 或nrm use taobao`切换不同的镜像源地址；
```




### js动画库

1. Three.js
2. Anime.js
3. Mo.js
4. Velocity.js
5. Popmotion
6. Vivus
7. GreenSock js
8. Scroll Reveal
9. Hover(css)
10. Kute.js
11. Typed.js
12. echarts



<http://jxhx2.yangqq.com/blog/#>
<https://www.yangqq.com/link.html>
<http://ww.aliwen.vip/>
<https://shawnzeng.com/>
<https://blog.csdn.net/weixin_44387725/article/details/90904191>


<https://www.bilibili.com/video/av83101450?p=26>

<https://www.bilibili.com/video/av88732281?p=46>

<https://www.cnblogs.com/AlexanderZhao/p/LearnCSSGrid.html>  css









