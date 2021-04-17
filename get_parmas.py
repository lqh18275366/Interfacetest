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