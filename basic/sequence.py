import random

# 列表或元组
source = ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'n', 'i', 'u']
print(''.join(source))
list = ['张三', '李四', '王五', '赵六', True, 13245]
print(list[2])      # 王五
print(list[1:3])    # 从第2个开始，到第4个之前
print(list[-1])     # 12345

# 对元组的操作是完全一样的
tup = ('张三', '李四', '王五', '赵六', True, 13245)
print(tup[-2])

print(random.choice(tup))

# 遍历列表
# list = ['张三', '李四', '王五', '赵六', True, 12345]
# 使用下标的方式进行遍历，注意一下代码的缩进
# for i in range(0, len(list)):     # 从0到6，左闭右开
# for i in range(len(list)):        # 如果range的范围从0开始，则可以活力
for i in range(1, len(list), 2):    # 此时，循环的变量的值为1、3、5
    print(i, end='\t')
    print(list[i])

# 直接用for...in直接取值
for item in list:
    print(item)

# 补充for或while循环的else的用法
# for item in list:
#     print(item)
# else:
#     print('循环结束')

# i=0
# while(i<len(list)):
#     print(list[i])
#     i+=1
# else:
#     print('循环结束')

# r = random.randint(1, 10)
# if r < 5:
#     print("太小了")
# elif r > 5:
#     print("太大了")
# else:
#     print("刚合适")
#
# if "张三" in list and r < 5:
#     print("存在")
# else:
#     print("不存在")


# 列表的其他用法
list = []   # 定义空列表
list.append(222)
list.append(333)
list.append(111)
list.append(444)
list.append(555)
list.append(666)
print(list)

list.remove(444)
print(list)

list.sort(reverse=True)
print(list)

list = [666, 555, 333, 222, 111]
tup = tuple(list)
print(tup)
list = list(tup)    # 注意：list此时被定义成了变量，不能再用于函数

list[2] = 444
print(list)

tup = (666, 555, 333, 222, 111)
tup[2] = 444      # 元组的元素值不能修改
print(tup)

# source = "HelloWoniu"
# print(source)
# print(source[1])
# source[1] = "E"
# print(source)
# source = "你好蜗牛"
# print(source)

# del(tup)
# print(tup)

# tup2 = (111,)       # 如果元组只有一个值，则必须在后加, 否则会变成普通类型
# print(tup2)


# 字典的定义
student = {'name':'张三', 'age': 25, 'sex':'男', 'phone': '13812345678', 'addr':'成都'}
# 字典的取值
print(student['name'])
print(student.get('phone'))
# 字典的更新：直接通过key修改值，如果key不存在，则会新增到字典中
student['sex'] = '女'
print(student)
student['sexy'] = '不知道'
print(student)
student.update({'sexy':'知道', 'age':26})
print(student)
# 字典的删除
student.pop('sexy')
print(student)
# 字典的遍历：按照Key遍历
for k in student:
    print("Key: %s,  Value: %s" % (k, student[k]))
for k in student.keys():
    print(k)
# 直接遍历值
for v in student.values():
    print(v)
# 直接Key和Value一起遍历，student.items()返回元组，可以直接按顺序赋值给k和v变量
for kv in student.items():
    print(kv)
for k, v in student.items():
    print(k, v)

