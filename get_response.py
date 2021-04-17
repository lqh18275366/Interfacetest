"""
response.status_code 状态码
response.url 请求url
response.encoding 查看响应头部字符编码
response.text 文本形式的响应内容
response.json() JSON形式的响应内容
"""
#1.导包
import requests
#2.请求百度地址,并生成实例对象
response = requests.get("https://www.baidu.com/")
#3.response.encoding 查看响应头部字符编码
# (1)查看返回的编码格式
print(response.encoding)
# (2)设置编码格式
response.encoding = 'utf-8'
#4.查看url
print("查看url：",response.url)
# #5.输出百度网页页面：text
# print(response.text)
