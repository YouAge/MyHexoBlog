---
title: Coding加域名部署
date: 2020-04-13 18:49:00
author: M.
img: false
cover: true
coverImg: false
password: false
toc: true
mathjax: false
summary: false 
categories: 网站建设
tags:
  - 博客
---


# 注册Coding账号密码

- [Coding注册](https://coding.net/)

- 注册完成后，登入创建 `DevOpos` 类型项目，

- 项目名称,项目表示，自己随定义取名， 跟Github一样

- 创建项目后，点击项目，找到代码创库，点击克隆项目，复制链接，跟github一样的操作

- 添加密钥，加本地git生成的公钥添加到Coding中， `个人中心- ssh公钥` 中， 
windows下面的git一般存放再C盘用户名下的.ssh文件`id_rsa.pub`文件中

- 再Hexo博客项目根目录下 _config.yml 中设置,

```yaml
deploy:
  type: git
  # repo: git@github.com:YouAge/youage.github.com.git
  repository:
    # 刚创建coding的项目的地址
    coding: git@e.coding.net:facade/hexo-blog-matery.git
  branch: master
```

- 使用命令

```shell script
hexo clean
hexo g 
hexo deploy
```

- 提交上去后， 点开项目，看到已更新了， 在点击构建与部署，点击静态网站
创建静态网站，
![](/images/Coding1.jpg)
网站名字自定义， 项目和仓库选址刚创建的，点击保存，它会生产一个随机访问地址，这样就可以访问了


## 绑定域名

### 域名设置，绑定 DNS 设置中添加 CNAME 记录指向

- 打开你购买的域名网站，找到域名，点击解析，点击添加记录，设置添加即可，
![](/images/Coding3.jpg)


- 点击静态网站，点击右边的设置， 拉到最下面，找到 自定义域名
![](/images/Coding2.jpg)

输入域名，点击绑定。 

- 需要HTTPS, 开启即可，
