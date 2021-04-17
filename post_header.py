"""
需求：
1. 请求IHRM项目的登录接口，URL： http://121.196.13.152:8080/admin/auth/login
2. 请求头： Content-Type: application/json
3. 请求体： {"username":"admin123", "password":"admin123"}
"""
#1.导包
import requests
#2.登陆接口且含有请求头
url = "http://121.196.13.152:8080/admin/auth/login"
#json格式
login_data = {"username":"admin123", "password":"admin123"}
header_data = {"Content-Type":"application/json"}

#1).标准写法
#response = requests.post(url,json=login_data,headers=header_data)

# #2）.json默认数据类型为json
# response = requests.post(url,json=login_data)

#3).data默认数据类型为表单，如果数据类型为json，需要headers
response = requests.post(url,data=login_data,headers=header_data)
#3.打印请求结果
print(response.text)

#4.获取响应体中键的值
json_data = response.json()
print(json_data.get('errno'))