---
title: hexo博客主题
date: 2018-09-07 09:25:00
author: M.
img: /images/matery.jpg
cover: true
coverImg: /medias/featureimages/3.jpg
password: false
toc: true
mathjax: false
summary: false 
categories: 博客
tags:
  - Hexo
---


# 快的构建博客




**首先准备工作**：  

1.  安装node.js, 
    
2.  安装git,  
    
3.  配置好node.js 后安装hexo环境
    

```shell script
npm install hexo
npm install -g hexo-cli
```

  

**开始创建blog：**  

1. 创建一个空的文件夹， 再使用命令，  
	wind使用管理权限打开cmd，或者使用git 使用


```shell script
hexo init blog
cd blog
npm install
```


2. 运行博客,再blog根目录下

```shell script
hexo s
```

3. 运行成功后，初始的博客就搭建完成了，再部署github上面,先需要再GitHub上面创建一个仓库，

```yaml
#  先再然后再blog根目录下配置
deploy:
  type: git
  repo: git@github.com:YouAge/youage.github.com.git  # git ssh地址
# 再执行下列命令，编译，提交

hexo g
hexo d
```




3. 下列hexo主题参考使用

	- [next主题](http://theme-next.iissnan.com/getting-started.html)
	- [next第三方插件](http://theme-next.iissnan.com/third-party-services.html)
	- [next深度优化定制](https://bestzuo.cn/posts/blog-establish.html)

	- [本站主题-matery](https://github.com/blinkfox/hexo-theme-matery)

	- [butterfly主题](https://github.com/jerryc127/hexo-theme-butterfly.git)



##  豆瓣插件的使用

-  根目录下安装 `npm install hexo-douban --save`
-  再根目录下配置_config.xml 文件
- [插件地址](https://github.com/mythsman/hexo-douban)

```yaml
douban: 
  user: # 你的豆瓣ID，个人中心 url中的 people/xxxx
  builtin: false  # true 
  book:
    title: '书香满园'  # 页面标题
    quote: '学如逆水行舟，不进则退' # 写在页面前面的化
  movie:
    title: '影视基地' 
    quote: '一场电影，一部人生' 
  timeout: 20000  # 请求超时
```

   - 启动命令:` hexo clean && hexo douban -bgm && hexo g && hexo s ` 注意其中开启hexo-douban的命令中，-bgm代表的是book、game、movie三个参数，如果只需要其中的一部分就只带你想要的那些参数

![插入图片](/images/17.jpg)

![matery文章设置](/images/matery.jpg)


## 关于Markdown 的使用和好的编译器


### 前期可以使用 IDEA的工具来编写文章，相对很方便，
- [PyCharm](https://www.jetbrains.com/pycharm/download/)
- [WebStorm](https://www.jetbrains.com/webstorm/)

- 在设置中添加创建初始模板，

![](/images/hexo/pycharm1.jpg)

- 相关语法
```angular2html
可用的预定义文件模板变量为：
$ {PROJECT_NAME} - 当前项目的名称。
$ {NAME} - 在文件创建过程中在“新建文件”对话框中指定的新文件的名称。
$ {USER} - 当前用户的登录名。
$ {DATE} - 当前的系统日期。
$ {TIME} - 当前系统时间。
$ {YEAR} - 今年。
$ {MONTH} - 当月。
$ {DAY} - 当月的当天。
$ {HOUR} - 目前的小时。
$ {MINUTE} - 当前分钟。
$ {PRODUCT_NAME} - 将在其中创建文件的IDE的名称。
$ {MONTH_NAME_SHORT} - 月份名称的前3个字母。 示例：1月，2月等
$ {MONTH_NAME_FULL} - 一个月的全名。 示例：1月，2月等
```

****
### Markdown语法记入点常用的
---
#### 字体设置
```markdown
*加粗*
*这是倾斜的文字*`
***这是斜体加粗***
~~这是加删除线的文字~~
```
- 这是效果
**这是加粗的文字**
*这是倾斜的文字*`
***这是斜体加粗的文字***
~~这是加删除线的文字~~

---
#### 引用

```markdown
>这是引用的内容
>>这是引用的内容
>>>>>>>>>>这是引用的内容
```
>这是引用的内容
>>这是引用的内容
>>>>>>>>>>这是引用的内容

---
#### 分割线

```markdown
---
----
***
*****
```
---
----
***
*****


#### 图片

```markdown
![插入图片](/images/17.jpg "图片title")
```
![插入图片](/images/17.jpg "图片title")


#### 链接
```markdown
[超链接名](超链接地址 "超链接title")
- 超链接title 可以不写
- 或者使用html <a>标签
<a href="https://www.dongzhu.ink/" target="本站">本站</a>
<http://baidu.com>
```
[小站](https://www.dongzhu.ink/)
[百度](http://baidu.com)

<http://baidu.com>
<a href="https://www.dongzhu.ink/" target="本站">本站</a>


#### 列表

```markdown
无需列表

- 列表内容
+ 列表内存
* 列表内存

有序列表
1. 列表内容
2. 列表内容
3. 列表内容
...
- + * 1. 2. 3. 跟内容之间都要有一个空格

#### 列表嵌套
  在上一个和下一个敲一个 tab 键

```


#### 表格

```markdown
表头|表头|表头
---|:--:|---:
内容|内容|内容
内容|内容|内容

第二行分割表头和内容。
- 有一个就行，为了对齐，多加了几个
文字默认居左
-两边加：表示文字居中
-右边加：表示文字居右
注：原生的语法两边都要用 | 包起来。此处省略


```
栏目一|栏目二|栏目三
--|:--:|--:
1|1|1
2|2|2
3|3|3















