
# (1) 三元运算符
a = 5
b = 10
max = a if a > b else b  # value_if_true if condition else value_if_false

print(max)

# (2) 枚举函数
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(index, fruit)

# (3) 压缩函数
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for x, y in zip(list1, list2):
    print(x, y)
xy = zip(list1, list2)
print(xy)

# (5) 匿名函数
add = lambda x, y: x + y
result = add(3, 4)
print(result)

# (6) any()和all()函数
numbers = [1, 2, 3, 0, 4]
result = any(numbers) # True
print(result)
result = all(numbers) # False。0使结果为False
print(result)

# (7) 迭代模块
print('###################7#################')
import itertools
numbers = [1, 2, 3, 3]

result = list(itertools.chain(numbers))
print(result)
result = list(itertools.product(numbers))
print(result)
result = list(itertools.permutations(numbers))
print(result)

# 8. 生成器
print('###################8#################')
# 使用yield关键字创建生成器
def fibonacci_series(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

# 输出迭代器中的值
for number in fibonacci_series(10):
    print(number)

# 9. 装饰器
print('###################9#################')
def log_function(func):
    def wrapper(*args, **kwargs):
        print(f'Running {func.__name__}')
        result = func(*args, **kwargs)
        print(f'{func.__name__} returned {result}')
        return result
    return wrapper

@log_function
def add(x, y):
    return x + y

print(add(5, 7))
# 运行add函数，返回值为12

# 10 多参数
def print_arguments(*args, **kwargs):
    print(args)
    print(kwargs)

print_arguments(1, 2, 3, name='John', age=30)
# (1, 2, 3)
# {'name': 'John', 'age': 30}


# 11. 动态导入
import importlib
# 当你想根据用户输入或配置导入模块时，可以使用模块动态导入模块importlib。
module_name = 'math'
module = importlib.import_module(module_name)
result = module.sqrt(9)


# 12. 字典生成式
squared_numbers = {x: x**2 for x in range(1, 6)}
print(squared_numbers)


# 13. 可调用对象
print('################### 13 #################')
class Adder:
    def __call__(self, x, y):
        return x + y

adder = Adder()
result = adder(3, 4)

print(result)       # 7

# 14.用下划线分隔大数字/字符
num_test = 100_345_405 # 一个大数字
print(num_test)
# 100345405


# 15.快速合并两个字典
dictionary_one = {"a": 1, "b": 2}
dictionary_two = {"c": 3, "d": 4}

merged = {**dictionary_one, **dictionary_two}

print(merged)       # {'a': 1, 'b': 2, 'c': 3, 'd': 4}


# 16. 列表、集合和字典是可变的
cities = ["Munich", "Zurich", "London"]
print(id(cities))  # 2797174365184
cities.append("Berlin")
print(id(cities))  # 2797174365184

# 集合
my_set = {1, 2, 3}
print(id(my_set))  # 2797172976992
my_set.add(4)
print(id(my_set))  # 2797172976992

# 字典
import gc
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(id(thisdict))  #2797174128256
thisdict["engine"] = "2500cc"
print(id(thisdict))  #2797174128256

# print(dict(id(thisdict)))  #2797174128256

print(gc.get_objects())