# 读取CSV，并动态将第一行处理为字典的Key，返回[{},{}]的格式
def read_csv(csvfile, has_column=True):
    with open(csvfile) as f:
        line_list = f.readlines()

    if not has_column:
        raise Exception('CSV文件必须要使用第一行作为列名')
        # return None

    key_list = line_list[0].strip().split(',')

    list = []
    for i in range(1, len(line_list)):
        # 如果当前行以#开头，则直接绕过，到下一行进行处理
        if line_list[i].startswith("#"):
            continue

        temp_list = line_list[i].strip().split(',')

        dict = {}
        for j in range(len(temp_list)):
            dict[key_list[j]] = temp_list[j]

        list.append(dict)

    return list


# 使用Python的csv模块进行读写
import csv

with open('./user-2.csv') as f:
    # 读取并遍历每一行
    csv_list = csv.reader(f)
    for item in csv_list:
        print(item)

    # 读取并将结果强制转换成 list
    csv_list = csv.reader(f)
    print(list(csv_list))

    # 以字典的格式读取数据
    csv_result = csv.DictReader(f)
    for user in csv_result:
        print(dict(user))

    csv.writer()


    # f.tell()    # 文件当前的指针位置
    # f.seek()    # 将文件指针指向哪个位置


result = read_csv('./user-2.csv')
print(result)


# 通常情况下，利用文本文件来保存数据，有三种数据格式可供使用：
# 1、CSV文件
# 2、XML文件
# 3、JSON文件

