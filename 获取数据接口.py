
import requests
import json



def get_p(stp,name):
    url_bat = 'https://api-hmugo-web.itheima.net/api/public/v1'
    url = url_bat + stp
    s = requests.get(url)
    path = f'./weixin/{name}.json'
    with open(path,'a',encoding='utf-8') as f:
        f.write(s.text)


def func(a,n,m):
    if n == 0:
        return 1
    else:
        num = func(a,n/2,m)
    if n%2 ==0:
        return num*num % n
    else:
        return num*num*a%m

print(func(5,6,7))