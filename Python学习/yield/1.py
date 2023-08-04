# def create_counter(n):
#  print ("create counter")
#  while True:
#   yield n
#   print ('increment n')
#   n += 1
#
# cnt = create_counter(2)
# print (cnt)
# print (next(cnt))
# print (next(cnt))
def func(x):
 print(x)
 return x * x

print(list(map(func, range(10))))
