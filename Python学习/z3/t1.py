from z3 import *
x = Int('x')
y = Int('y')
s = Solver()
print (s)
s.add(x > 10, y == x + 2)
print (s)
print ("Solving constraints in the solver s ...")
print (s.check())                       # 判断是否满足

print ("Create a new scope...")         # 创建一个新的范围
s.push()
s.add(y < 11)
s.add(y+x < 111)


print (s)
print ("Solving updated set of constraints...")
print (s.check())
print ("Restoring state...")
s.pop()
print (s)
print ("Solving restored set of constraints...")
print (s.check())
