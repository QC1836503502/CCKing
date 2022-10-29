import requests
import random
import time
import Mymodule
import Merge
from colorama import init
init(autoreset=True)
Mymodule.zqip()
Merge.hb()
a = open("export/combo.txt","r")
print(b+' 请输入要进行测压的网站网址:')
url = str(input())
pd = input(b+' 是否进行不停歇工作(y/n):')
if pd == "y":
    print("\033[31m[Console]:\033[0m",'开始不停歇工作')
    while True:
        for x in a:
            http_ip = [
                x
            ]
            for i in range(10):
                try:
                    ip_proxy = random.choice(http_ip)
                    proxy_ip = {
                        'http': ip_proxy,
                        'https': ip_proxy,
                    }
                    requests.get(url, proxies=proxy_ip)
                    print("\033[31m[Console]:\033[0m",'发送请求一次,对方已回应')
                    break
                except Exception as e:
                    print("\033[31m[Console]:\033[0m",'发送请求一次,对方未回应')
                    break
else:
    for x in a:
        http_ip = [
            x
        ]
        for i in range(10):
            try:
                ip_proxy = random.choice(http_ip)
                proxy_ip = {
                    'http': ip_proxy,
                    'https': ip_proxy,
                }
                requests.get(url, proxies=proxy_ip)
                print("\033[31m[Console]:\033[0m",'发送请求一次,对方已回应')
                break
            except Exception as e:
                print("\033[31m[Console]:\033[0m",'发送请求一次,对方未回应')
                break

