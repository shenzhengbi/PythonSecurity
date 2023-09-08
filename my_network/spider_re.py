import re,requests,time

#使用正则表达式爬虫，限制太多

def download_page():
    resp = requests.get('http://www.woniunote.com/')
    #解析网页的所有超链接
    links = re.findall('<a href="(.+?)"',resp.text) #。+？非贪婪模式，找到最近的就行了，贪婪模式一直找到最远的

    #print(links)

    # for link in links:
    #     print(link)

    #基于错误的源内容进行优化，（网页中有些符合代码定义的正则表达式的要求，但不是网址，需要排除这部分内容）
    #仅代表当前页面的毛病
    for link in links:
        #先根据页面特性，将一些无用的超链接排除
        if 'articleid' in link:
            continue
        if link.startswith('#'):
            continue

        #对超链接进行处理，拼接出完整url地址
        if link.startswith('/'):
            link = 'http://www.woniunote.com'+link

        #print(link)
        #将页面文件保存于本地
        resp  = requests.get(link)
        resp.encoding = 'utf-8'
        filename = link.split('/')[-1]+time.strftime("%Y%m%d_%H%M%S")+'.html'
        with open(f'./woniunote/page/{filename}',mode='w',encoding='utf-8') as file:
            file.write(resp.text)

#爬取首页图片
def download_image():
    resp = requests.get('http://www.woniunote.com/')
    images = re.findall('<img src="(.+?)"',resp.text)
    #print(images)
    for image in images:
        if image.startswith('/'):
            image = "http://www.woniunote.com"+image

        print(image)
        #suffix = image.split('.')[-1]
        filename = time.strftime("%Y%m%d_%H%M%S") + image.split('/')[-1]
        #print(filename)
        #下载图片
        resp = requests.get(image)
        with open('./woniunote/image/'+filename,mode='wb') as file:
            file.write(resp.content)

if __name__ == '__main__':
    download_image()