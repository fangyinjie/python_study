import numpy as np
import timeit


# 创建一个包含1到5的numpy数组
arr1 = np.random.choice(a=range(100), size=(1000))
arr2 = arr1.tolist()
# print("原始数组1：", arr1)
# print("原始数组2：", arr2)

# 定义一个自定义函数，将每个元素平方后返回
def square_func(x):
    return x ** 2


# 使用map()函数对数组进行操作
st1 = timeit.default_timer()
np.vectorize(square_func)(arr1)
# result1 = map(square_func, arr1)
et1 = timeit.default_timer()

st2 = timeit.default_timer()
result2 = list(map(square_func, arr2))
et2 = timeit.default_timer()
print(result2)

result3 = []
st3 = timeit.default_timer()
for i in arr2:
    i = square_func(i)
# result2 = map(square_func, arr2)
et3 = timeit.default_timer()

print(f"t1:{1000 * 1000 * (et1 - st1):.2f}, "
      f"t2:{1000 * 1000 * (et2 - st2):.2f}, "
      f"t3:{1000 * 1000 * (et3 - st3):.2f}, ")
# 转换为列表并打印输出
# output = list(result)
# print("处理后的数组：", output)