# 文件的读写，所有的I/O操作主要分三步：打开资源，操作资源，关闭资源

#  基本操作：读取文件内容并输出
f = open('./Test.txt', mode='r')
content = f.read()
print(content)
f.close()

# 写入文件内容
f = open('./Test.txt', mode='a')
f.write("\nHello Woniu !!!")
f.close()

# 写入新文件，并使用GBK的编码
f = open('./Temp.txt', mode='w', encoding='GBK')
f.write("这是一个牛逼的文件\n通过事先设定某个特定场景下的特定问题\n来探求该场景下的各种可能的解决方案\n")
f.close()

# 读取的操作
f = open('./Temp.txt', encoding='GBK')
content = f.read(20)      # 指定读取文件的内容长度
content = f.readline()    # 按行读取文件内容，默认读取第1行
content = f.readlines()     # 按行全部读取并且将每一行保存到列表中
print(content)
# 也可以使用f.read()读取所有内容，使用 \n 作为分隔符，调用split进行列表处理
content = f.read()
list = content.split('\n')
print(list)
f.close()

# CSV文件的读写：逗号分隔符，用于表示二维表的数据结构
# 将CSV文件变成Python的列表+字典的格式 [{},{},{}]
f = open('./userpass.csv')
line_list = f.readlines()

user_list = []
# username, password, expect   # 如何动态读取第一行数据，并且变成列名
for i in range(1, len(line_list)):
    line = line_list[i].strip()

    username = line.split(',')[0]
    password = line.split(',')[1]
    expect = line.split(',')[2]

    user_dict = {}
    user_dict['username'] = username
    user_dict['password'] = password
    user_dict['expect'] = expect

    user_list.append(user_dict)

print(user_list)



# 使用 with 自动处理资源关闭的问题
with open('./Temp.txt') as f:
    content = f.read()
print(content)

# 读取二进制文件时，需要使用 rb
with open('D:/emergency.jpg', mode='rb') as f:
    content = f.read()
print(content)
