import re, requests, random
import time

resp = requests.get('http://www.woniunote.com/')

# 解析网页所有超链接
# links = re.findall('<a href="(.+?)">', resp.text)
# for link in links:
#     print(link)

# 基于一些错误的源内容，对其进行优化，并下载和保存网页
def download_page():
    links = re.findall('<a href="(.+?)"', resp.text)
    for link in links:
        # 先根据页面特性，将一些无用的超链接进行排除
        if 'articleid' in link:
            continue
        if link.startswith('#'):
            continue

        # 对超链接进行处理，拼接出完整的URL地址
        if link.startswith('/'):
            link = 'http://www.woniunote.com' + link

        # 将页面文件保存于本地
        resp = requests.get(link)
        resp.encoding = 'utf-8'
        filename = link.split('/')[-1] + time.strftime("_%Y%m%d_%H%M%S") + '.html'
        with open(f'./woniunote/page/{filename}', mode='w', encoding='utf-8') as file:
            file.write(resp.text)

# 爬取蜗牛笔记首页图片
def download_image():
    resp = requests.get('http://www.woniunote.com/')
    images = re.findall('<img src="(.+?)"', resp.text)
    for image in images:
        # 处理URL地址
        if image.startswith('/'):
            image = 'http://www.woniunote.com' + image

        # 下载图片
        resp = requests.get(image)
        # suffix = image.split('.')[-1]
        filename = time.strftime("%Y%m%d_%H%M%S_") + image.split('/')[-1]
        with open('./woniunote/image/' + filename, mode='wb') as file:
            file.write(resp.content)

if __name__ == '__main__':
    # download_page()
    download_image()
