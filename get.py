#1.导包
import requests
#2.请求百度地址,并生成实例对象
response = requests.get("https://www.baidu.com/")
#3.输出百度网页页面：text
print(response.text)
