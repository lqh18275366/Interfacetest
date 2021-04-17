# requests库
安装：pip install requests

ctrl +f：搜索

ctrl+p：查看get/post参数提示

ctrl+点击get/post：查看request库的源码

## get请求
### url：无查询参数
```python
#1.导包
import requests
#2.请求百度地址
response = requests.get("https://www.baidu.com/")
#3.输出百度网页页面：text
print(response.text)
```
### url_paramas:查询参数
```python
#get请求带参数
#需求：访问TPshop搜索商品的接口，通过查询字符串的方式传递搜索的关键字 iPhone ，并查看响 应数据

#1.导包
import requests
#2.发送请求

# #1）.将查询参数作为url的一部分传递
# requests.get(url=" http://localhost/Home/Goods/search.html?q=iPhone")

# #2）.查询参数（paramas）作为字符串格式传递
# url = " http://localhost/Home/Goods/search.html"
# response = requests.get(url,params="q=iPhone")

#3）.查询参数（paramas）作为字典格式传递
paramas_dict = {"q":"iPhone"}
url = " http://localhost/Home/Goods/search.html"
response = requests.get(url,paramas_dict)

#3.打印响应结果
print(response.text)
```
## post请求tpshop商城
请求体数据类型可以是字典、元组、字节或文件对象
### 表单格式：data
```python
# 登陆tpshop商城：post——表单类型
#1.导包
import requests
#2.实现请求登陆接口
url = "http://localhost/index.php?m=Home&c=User&a=do_login"
#表单定义为字典格式
login_data = {"username": "13088888888", "password": "123456","verify_code": "1234"}
reponse = requests.post(url=url,data=login_data)
""" 
    代码格式：response = requests.post(url, data=None, json=None)
        参数说明：
            url: 请求的URL 
            data: (可选) 支持json格式（需要加参数），默认表单格式
            json: (可选) 要发送到请求体中的JSON数据 
            rtype: requests.Response """
#3.打印响应数据（tpshop商城页面）:输出的响应结果为json格式
print(reponse.json())
```
### json格式
```python
#微商城的登陆：post请求-json数据类型
#1.导包
import requests
#2.登陆接口
url = "http://121.196.13.152:8080/admin/auth/login"
#定义字典类型的json数据
login_data =  {"username":"admin123", "password":"admin123"}
response = requests.post(url,json=login_data)
#3.查看输出结果
print(response.json())
```
## 响应
### 响应内容
```python
"""
response.status_code 状态码
response.url 请求url
response.encoding 查看响应头部字符编码
response.text 文本形式的响应内容
response.json() JSON形式的响应内容
"""
```
实例
```python
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
```
### json响应
如果请求响应的内容为JSON格式的数据，则可以直接调用 response.json() 方法获取数据，因为
requests中内置了JSON解码器，帮助我们处理JSON数据。
```python
#1.导包
import requests
#2.登陆接口且含有请求头
url = "http://121.196.13.152:8080/admin/auth/login"
#json格式
login_data = {"username":"admin123", "password":"admin123"}
header_data = {"Content-Type":"application/json"}
response = requests.post(url,data=login_data,headers=header_data)
json_data = response.json()
print(json_data.get('errno'))
```

注：如果 JSON 解码失败，response.json() 就会抛出一个异常