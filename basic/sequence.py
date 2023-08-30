import random

source = ['H','e','I','i','o','W','o','i','u']
print("".join(source)) #将列表拼接，中间什么都不插入

list = ['张三','李四','王五','赵六',True,13245]
print(list[2]) #王五
print(list[1:3])#不包含赵六
print(list[-1]) #13245

#对元组的操作完全一样
tup = ('张三','李四','王五','赵六',True,13245)
print(random.choice(tup)) #在元组随机选择

#遍历列表
print(list) #直接打印
#下标方式
for i in range(0, len(list)):
    print(i, end='\t')
    print(list[i])

for i in range(0, len(list),2):#2是步长
    print(i, end='\t')
    print(list[i])

#直接用for ..in 直接取值
for item in list:
    print(item)

#其他用法
list = []
list.append(111)
list.append(222)
list.append(333)
list.append(444)
list.append(555)
list.append(666)
print(list)

list.remove(444)
print(list)

list.sort(reverse=True)
print(list)

tup = tuple(list)
print(tup) #将列表变成元组

#list = list(tup)#有问题，list被定义为了变量，不能在用于函数

list[2] = 444
print(list)

#tup[2] = 444,不能修改元素值
#print(tup)

#字典
student = {'name':'小沈','age':'22','sex':'男','phone':'13817771897','addr':'南京'}
#字典取值
print(student['name'])
print(student.get('phone'))
#字典更新，通过key值修改，如果key不存在，则会新增到字典中
student['sex'] = '女'
print(student) #{'name': '小沈', 'age': '22', 'sex': '女', 'phone': '13817771897', 'addr': '南京'}
student['sexy'] = '未知'
print(student) #{'name': '小沈', 'age': '22', 'sex': '女', 'phone': '13817771897', 'addr': '南京', 'sexy': '未知'}
student.update({'sexy':'知道','age':24})
print(student)

#字典删除
student.pop('sexy')
print(student)

#字典遍历，按照key遍历
for key in student:
    print('Key:%s,Value:%s'%(key,student[key]))

#遍历k
for key in student:
    print(key)
#直接遍历值
for v in student.values():
    print(v)
print("=========")
#key ,value一起遍历，student.items()返回元组，可以直接按照顺序赋值给k和v变量
for kv in student.items():
    print(kv)
# ('name', '小沈')
# ('age', 24)
# ('sex', '女')
# ('phone', '13817771897')
# ('addr', '南京')
print("========")
for k,v in student.items():
    print(k,v)
else:
    print("=======") #上面循环结束执行这个，不用else，直接print效果一样，这样就是为了优雅
    #while循环一样，也可以在最后加个else，效果一样
# name 小沈
# age 24
# sex 女
# phone 13817771897
# addr 南京





