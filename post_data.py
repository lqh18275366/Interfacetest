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
            data: (可选) 要发送到请求体中的字典、元组、字节或文件对象 ，支持json格式（需要加参数），默认表单格式
            json: (可选) 要发送到请求体中的JSON数据 
            rtype: requests.Response """
#3.打印响应数据（tpshop商城页面）:输出的响应结果为json格式
print(reponse.json())