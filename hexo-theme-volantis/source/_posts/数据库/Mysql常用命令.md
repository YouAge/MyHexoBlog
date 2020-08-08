---
title: Mysql常用命令
author: M.
img: false
cover: false
coverImg: false
password: false
toc: true
mathjax: false
summary: false
categories: 数据库
tags:
  - MySql
abbrlink: 64129a24
date: 2019-04-14 00:46:00
---


# MySql 常用命令的基本使用篇章


## 初始操作


```sql
-- 查看所有数据库 
show databases;
-- 选择数据库
use db;
-- 查看到但钱使用的数据库
select database();
-- 创建数据库
create database dbname charset=utf8;
-- 查看当前数据库中所有的表
show tables;
-- 查看表结构
desc 表名;

-- sql格式数据导入数据
insert into 表名 values (数据)

-- 创建数据表
-- 创建班级表 -----
create table classes (
    id int unsigned auto_increment primary key not null,
    name varchar(30) not null
);
-- students表
create table students(
    id int unsigned primary key auto_increment not null,
    name varchar(20) default '',
    age tinyint unsigned default 0,
    height decimal(5,2),
    gender enum('男','女','中性','保密') default '保密',
    cls_id int unsigned default 0,
    is_delete bit default 0
);
```
<!-- more -->

## 查

```sql
-- 基础查询---
--查询表格所以字段
>> select * from 表名;
-- 指定字段查询
>> select 字1,字2,.. from 表名;
-- 对于表名 跟字段名长的可以通过 as 别名
>> select id as 标号, name as 名字, gender as 性别 from students;
-- 跟表名起别名
>> select s.id,s.name,s.gender from students as s;
-- 在select后面列前使用distinct可以消除重复的行
>> select distinct 列1,... from 表名;
	例：
	>> select distinct gender from students;
```
**条件查询**

```sql
-- 使用where子句对表中的数据筛选，结果为true的行会出现在结果集中
>> select * from 表名 where 条件;
	例：
	>> select * from students where id=1;
----where后面支持多重运算符，进行比较
	>> 比较运算符 | 逻辑运算符| 模糊查询| 范围查询 | 空判断
---比较运行符 
	-- 等于: = | 大于: > |大于等于: >= |小于: < | 小于等于: <= | 不等于: != 或 <>
>> 例如：
	-- 例1：查询编号大于3的学生
	>> select * from students where id > 3;
	--例2：查询编号不大于4的学生
	>> select * from students where id <= 4;
	--例3：查询姓名不是“黄蓉”的学生
	>> select * from students where name != '黄蓉';
	--例4：查询没被删除的学生
	>> select * from students where is_delete=0;

--- 逻辑运算符、
	>> and | or | not
>> 例如：
	--例5：查询编号大于3的女同学
	>> select * from students where id > 3 and gender=0;
	--例6：查询编号小于4或没被删除的学生
	>> select * from students where id < 4 or is_delete=0;

-- 模糊查询
	like | %表示任意多个任意字符 | _表示一个任意字符
>> 例如：
	--例7：查询姓黄的学生
	select * from students where name like '黄%';
	--例8：查询姓黄并且名字是一个字的学生
	select * from students where name like '黄_';
	--例9：查询姓黄或叫靖的学生
	select * from students where name like '黄%' or name like '%靖';

-- 范围查询
	in 表示在一个非连续的范围内 | between ... and ...表示在一个连续的范围内
>> 例如：
	--例10：查询编号是1或3或8的学生
	select * from students where id in(1,3,8);
	--例11：查询编号为3至8的学生
	select * from students where id between 3 and 8;
	--例12：查询学生是3至8的男生
	select * from students where id between 3 and 8 and gender=1;

-- 空判断
	判空 is null  | 判非空is not null
>> 例如：
	--例13：查询没有填写身高的学生
	select * from students where height is null;
	--例14：查询填写了身高的学生
	select * from students where height is not null;
	--例15：查询填写了身高的男生
	select * from students where height is not null and gender=1;

-- 优先级
	--优先级由高到低的顺序为：小括号，not，比较运算符，逻辑运算符
	--and比or先运算，如果同时出现并希望先算or，需要结合()使用

```





## 增

## 删

```sql
>> delete from 表名 where 条件
如：
>> delete from students where id=5;

--逻辑删除，本质就是修改操作,表中有逻辑删除的字段is_delete
>> update students set is_delete=1 where id=1;

```


## 改



## 备份
```sql
--- 在未登入mysql下进行
mysqldump -uroot -p 库名 > python.sql; 
-- 提示输入mysql密码， 在
-- 导入备份数据
-- 库名
mysql -uroot -p 库名 < python.sql
```