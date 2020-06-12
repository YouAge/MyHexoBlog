---
title: axios请求封装
date: 2020-05-02 20:06:00
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
  - vue
---


> 项目中对 axios 请求的封装 


> axios.js 文件

```javascript
import axios from 'axios'

const baseUrl = process.env.NODE_ENV === 'production' ? '/api/': '/'

class HttpRequest {
   // 参数初始化
  constructor (baseUrl = baseURL) {
    this.baseUrl = baseUrl;
    this.queue = {}
  }
  getInsideConfig () {
    const config = {
      baseURL: this.baseUrl,
      headers: {
        //
      }
    };
    return config
  }
  distroy (url) {
    delete this.queue[url]
    if (!Object.keys(this.queue).length) {
      // Spin.hide()
    }
  }
  interceptors (instance, url) {
    // 请求拦截
    instance.interceptors.request.use(config => {
      // 添加全局的loading...
      if (!Object.keys(this.queue).length) {
        // Spin.show()
      }
      this.queue[url] = true;
      config.headers['Authorization'] = getToken()
      return config
    }, error => {
      return Promise.reject(error)
    })
    // 对请求结果拦截处理
    instance.interceptors.response.use(res => {
      this.distroy(url)
      const { data } = res
      return data
    }, error => {
      this.distroy(url)
      return Promise.reject(error.response.data)
    })
  }
  request (options) {
    const instance = axios.create()
    options = Object.assign(this.getInsideConfig(), options)
    this.interceptors(instance, options.url)
    return instance(options)
  }
}
const axios = new HttpRequest()
export default axios
// export default HttpRequest

```


> 使用

```javascript


```