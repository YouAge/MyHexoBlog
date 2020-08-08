---
title: Mysql数据库的配置安装
author: M.
img: false
cover: false
coverImg: false
password: false
toc: true
top: false
mathjax: false
summary: false
categories: 工具
tags:
  - MySql
abbrlink: 27a7b644
date: 2019-04-26 19:11:00
---



>在安装mysql和使用，中出现的一些的问题， 
自己找到并实际解决的方法做一下记录


### MySQL数据库安装

## --windows下安装，下一步

> 或者下载 直接下载  [phpstudy_pro](https://www.xp.cn/) 管理工具，带`redis`库

## --liunx下安装--
```python
## 网上资料 
yum install mysql
yum install mysql-server
yum install mysql-devel
### 在安装mysql-server是出现报错 
"""
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
 * base: mirrors.sina.cn
 * extras: mirrors.sina.cn
 * updates: mirrors.sina.cn
No package mysql-server available.
Error: Nothing to do"""
方法一 安装 yum install mariadb-server mariadb 
"""
mariadb数据库的相关命令是：
systemctl start mariadb  #启动MariaDB
systemctl stop mariadb  #停止MariaDB
systemctl restart mariadb  #重启MariaDB
systemctl enable mariadb  #设置开机启动
所以先启动数据库
"""
## 启动数据库，进入后感觉怪怪 的 mysql -u root -p

放法二 官网下载mysql-server 
## 下载地址  https://dev.mysql.com/downloads/repo/yum/ 找到适合版本的liunx
rpm -ivh（安装软件包并显示安装进度） 版本 .rpn
yum -y install mysql-community-server

"""
service mysqld start (5.0版本是mysqld) 启动
service mysql start (5.5.7版本是mysql)
----停止----
service mysqld stop
----重启----
service mysqld restart 
service mysql restart (5.5.7版本命令)
----查看MySQL运行状态--
systemctl status mysqld.service

2、使用 mysqld 脚本启动：
/etc/inint.d/mysqld stop
"""

------------------初始登入------->
## 如果首次登入不上，需要查看一下零时密码
## 查看临时密码 grep "password" /var/log/mysqld.log 
"""
使用临死密码登入， 成功后
ALTER USER 'root'@'localhost' IDENTIFIED BY 'Root_12root';
只能先修改密码 不能进行任何操作，设置密码也有规范不能太简单
先修改一个符合条件的密码 Root_12root
查看密码设置条件 SHOW VARIABLES LIKE 'validate_password%';
通过设置 
set global validate_password.policy=0;
set global validate_password.length=1;
这样就可以修改简单密码了，在重置一下密码

ALTER USER 'root'@'localhost' IDENTIFIED BY 'mysql';
"""

----------------注-----
如果使用方法二去覆盖方法一的安装， 此时会出现MySQL 服务器开不起来的解决方法
出现错误 Failed to start MySQL Server
"""
查看 cat /etc/my.cnf
datadir=/var/lib/mysql
socket=/var/lib/mysql/mysql.sock

删除--   rm -rf /var/lib/mysql/*
在启动mysql服务器， 安装方法二的操作

"""
```

<!-- more -->

### 解决Navicat 连接MySQL 8.0.11 出现2059错误	

```python
mysql -uroot -ppassword #登录

use mysql; #选择数据库

## --->  select user,plugin from user where user='root';   查看加密方式
ALTER USER 'root'@'localhost' IDENTIFIED BY 'password' PASSWORD EXPIRE NEVER; #更改加密方式

ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password'; #更新用户密码

FLUSH PRIVILEGES; #刷新权限

-----------注-------------
"""
修改时出现 ERROR 1819 (HY000): Your password does not satisfy the current policy requirements 错误
需要修改数据库的策略

查看mysql 初始的密码策略  SHOW VARIABLES LIKE 'validate_password%';
需要设置密码的验证强度等级，设置 validate_password_policy 的全局参数为 LOW 即可
set global validate_password.policy=LOW;
当前密码长度为 8 ，如果不介意的话就不用修改了
 set global validate_password.length=6; 

update user set password=('123.com') where user='root';

关于 mysql 密码策略相关参数；
1）、validate_password_length  固定密码的总长度；
2）、validate_password_dictionary_file 指定密码验证的文件路径；
3）、validate_password_mixed_case_count  整个密码中至少要包含大/小写字母的总个数；
4）、validate_password_number_count  整个密码中至少要包含阿拉伯数字的个数；
5）、validate_password_policy 指定密码的强度验证等级，默认为 MEDIUM；
关于 validate_password_policy 的取值：
0/LOW：只验证长度；
1/MEDIUM：验证长度、数字、大小写、特殊字符；
2/STRONG：验证长度、数字、大小写、特殊字符、字典文件；
6）、validate_password_special_char_count 整个密码中至少要包含特殊字符的个数；
--------------------- 
"""

-------------（liunx）如果mysql登入密码忘记，--------------------
首先 vim /etc/my.cnf 
在[mysql] 下面增加一行  skip-grant-tables
重启mysql重新登入不用输入密码
更具网上的重置更新密码的语法 update user set authentication_string=password('123.com') where user='root'; 如果报语法错误就使用下面一条，密码已经是加密过的 为mysql  （先查看一样，密码的加密方式是否是 mysql_native_password）是的就是可行的，
update mysql.user set authentication_string='*E74858DB86EBA20BC33D0AECAE8A8108C56B17FA where user'='root';


-----查看密码---
select host,user,authentication_string from user;

------------更改mysql远程连接---------------
方式一 直接修改修改  update user set host = '%' where user = 'root';
 

------查看修改后的状态---
select host, user from user;

```
