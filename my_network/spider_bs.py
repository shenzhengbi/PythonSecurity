import requests,time
from bs4 import BeautifulSoup

resp = requests.get('http://www.woniunote.com')

#初始化解析器
html = BeautifulSoup(resp.text,'lxml')
#查找页面属性
# print(html.head.title)
# print(html.head.title.string)
#print(html.div)
#print(html.div.div.div)

#查找页面元素的通用方法：
#1，find_all:根据标签、属性，xpath等进行查找
#2，select：css选择器，div,#id,.class

#查找页面所有超链接
# links = html.find_all('a')
# for link in links:
#     print(link['href'])
#
#查找页面的图片
# images = html.find_all('img')
# for image in images:
#     print(image['src'])

#更加id或者class属性查找
# keyword = html.find(id='keyword')
# print(keyword)

# titles = html.find_all(class_='title')
# for title in titles:
#     # print(title)
#     # print(title.find('a'))
#     print(title.string)

# title = html.find(text='核心实验：利用UISpy识别Windows界面元素')
# print(title.parent)
# print(title.parent.parent)

# #更加xpath的风格来查找 //div[@class='title']
# titles = html.find_all('div',{'class':'title'})
# for title in titles:
#     print(title.string)


# #css选择器
# titles = html.select('div.title')
# for title in titles:
#     print(title.string)

keyword  = html.select("#keyword")
print(keyword[0]['placeholder'])