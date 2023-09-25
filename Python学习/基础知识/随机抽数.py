# from random import seed, randint, random
import random
# 方法一：
#[random.randint(0,100) for _ in range(2)]
# 输出： [34, 44]

#方法二：
#list中随机去取K个数
k =3
list=[[1,2],[3,4],[5,6],[7,8],[9,10]]
# list=[1,2,3,4,5,6,7,8,9,10]
print(random.sample(list, k))
# 数据类型转换：
# print(np.float64(42))     # 浮点型
# print(np.int8(60))        # 整型
# 注意：转换的值不要超出数据类型的范围
# print(np.int8(400))       #-112
# 布尔类型,注意：除了0为false,其他的数字都为true
# print(np.bool(0))         # false
# print(np.bool(1))         # true
# print(np.float64(True))   # 1.0
# print(np.int(False))      # 0
# print(np.int(True))       # 1

# 元组      (数据对象, xxx, ……)         不可变对象
# 列表      [xxx, xxx, ……]              可变对象
# e[x x]
# e.append(x)                         在e的尾部加x
# ascII   ——》 utf-8                   a="xxx"
# g=a.decode('utf-8')                 转换
# Join([x, x, x])                     字符串连接
# 打开文件：           open('x.txt', 'w')  写
# 打开文件：           open('x.txt', 'r')  读
# 打开文件：           open('x.txt', 'a')  尾行添加
#
# 修改字符串        a = "this is word"
#                 b = a.replace("this", "that")       //this改成that
#                 a没变、b为结果
#                 a.find("world")                     输出首字母位置的数字



# （1）         urllib
#              urllib2     网络
# （2）         datetime    time时间
# （3）         OS          系统
# （4）         pickle      对象序列化   常用数据交换格式. isom xml
# （5）         bsddb       数据库     key=》value
# （6）         loging      日志（为系统做日志）
# （7）
# fileObject.read()           从文件读取指定的字节数，如果未给定或为负则读所有
#
# OS.listdir()                用于返回指定的文件夹包含的文件/文件夹的名的list
# os.path.join("xx","xx","xx")    返回  xxx/xxx/xxx 自动添加分隔符

