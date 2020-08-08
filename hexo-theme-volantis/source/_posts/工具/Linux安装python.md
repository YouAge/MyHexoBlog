---
title: Linux安装python
author: M.
img: false
cover: false
coverImg: false
password: false
toc: true
top: false
mathjax: false
summary: false
tags:
  - Linux
  - Python
  - shell
abbrlink: c7c488b9
date: 2019-09-02 13:49:00
categories:
---

> 编写 shell脚本自动安装python环境

```shell
#!/bin/bash
#set -x  # 脚本运行情况输出
## 安装EPEL和IUS软件源
# 获取用户名
username=$(whoami)

yum install epel-release -y
yum install https://centos7.iuscommunity.org/ius-release.rpm -y
##　安装python3.6版本
yum install python36u -y
yum install python36u-devel -y
## 安装python需要的系统环境
yum install -y openssl-devel openssl-static zlib-devel lzma tk-devel xz-devel bzip2-devel ncurses-devel gdbm-devel readline-devel sqlite-devel gcc libffi-devel gcc-c++

# 修改pip下载源， 创建当前用户目录创建使用
mkdir  /$username/.pip

cat > /$username/.pip/pip.conf << eof
[global]
index-url = http://mirrors.aliyun.com/pypi/simple/
[install]
trusted-host=mirrors.aliyun.com
eof

#  mv pip.conf /root/.pip/pip.conf

if [ $username == "root" ]; then
  #supervisor 安装需要 root 权限，
  # 安装supervisor 进程守护
  pip3 install supervisor

  # 【生成supervisor默认配置文件】
  echo_supervisord_conf > /etc/supervisord.conf
  # 启动 supervisord 启动项目
  supervisord -c /etc/supervisord.conf

  # 配置开机自启， 检查一下 whereis supervisord 的路径，修改对应的 ExecStart=/usr/bin/supervisord
  # ExecStart=/usr/bin/supervisord
  #　生成开机自启的配置
  cat > /usr/lib/systemd/system/supervisord.service << eof
[Unit]
Description=Supervisor daemon

[Service]
Type=forking
#
ExecStart=/usr/local/bin/supervisord -c /etc/supervisord.conf
ExecStop=/usr/local/bin/supervisorctl shutdown
ExecReload=/usr/local/bin/supervisorctl reload
KillMode=process
Restart=on-failure
RestartSec=42s

[Install]
WantedBy=multi-user.target

eof
# mv supervisord.service /usr/lib/systemd/system/

  #  启动服务
  systemctl enable supervisord

else
  echo "请在 root权限下安装，supervisor"
fi

```
<!-- more -->
## pip源修改pip.conf 
```shell
[global] 
index-url = http://mirrors.aliyun.com/pypi/simple/ 
[install] 
trusted-host=mirrors.aliyun.com
```

## supervisord.service 文件
```shell
[Unit] 
Description=Supervisor daemon

[Service] 
Type=forking 
ExecStart=/usr/local/bin/supervisord -c /etc/supervisord.conf
ExecStop=/usr/local/bin/supervisorctl shutdown
ExecReload=/usr/local/bin/supervisorctl reload
KillMode=process 
Restart=on-failure 
RestartSec=42s

[Install] 
WantedBy=multi-user.target

```