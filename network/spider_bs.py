from bs4 import BeautifulSoup
import requests

resp = requests.get('http://www.woniunote.com/')

# 初始化解析器
html = BeautifulSoup(resp.text, 'lxml')

# 查找页面元素(根据标签层次进行查找）
# print(html.head.title)      # 根据标签的层次找页面标题
# print(html.head.title.string)       # 获取页面标题的文本内容
# print(html.div)             # 查找页面中的第一个DIV元素
# print(html.div.div.div)

# 查找页面元素的通用方法：
# 1、find_all：根据标签，属性，XPath等进行查找
# 2、select：CSS选择器，div, #id, .class

# 查找页面所有超链接
links = html.find_all('a')
for link in links:
    print(link['href'])

# 查找页面的图片
images = html.find_all('img')
for image in images:
    print(image['src'])

# 根据id或class等属性查找
keyword = html.find(id='keyword')
print(keyword)
print(keyword['placeholder'])
#
titles = html.find_all(class_='title')
for title in titles:
    # print(title)
    print(title.string)
    # print(title.find('a'))
    # print(title.find('a').string
#
# print('=========================================')
title = html.find(text='揭秘：带你了解学员眼中真实的阿多比！')
print(title.parent)
print(title.parent.parent)
#
# print('=========================================')
# # 根据xpath的风格进行查找 //div[@class='title']
titles = html.find_all('div', {'class':'title'})
for title in titles:
    print(title.string)
#
# print('=========================================')

# CSS选择器
# titles = html.select('div.title')
titles = html.select('.title')
for title in titles:
    print(title.string)

keyword = html.select('#keyword')
print(keyword[0]['placeholder'])

lis = html.select('ul li')
print(lis)