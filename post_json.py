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