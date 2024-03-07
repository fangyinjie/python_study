import numpy as np
import time
import random


# dt = np.dtype([('name', 'S20'), ('age', 'i4')])
dt = np.dtype([('name', 'S10'), ('age', 'i8' )])
print(dt)
print()
# a = np.array([('adm', 29), ('wan', 23), ('ade', 21)], dtype=dt)

st = time.time()
for i in range(100000):
    # a = np.random.randint(0, 100, size=100)
    # s = np.sort(a)

    a = [random.randint(0, 100) for _ in range(100)]
    s = a.sort()
    # print(a)
et = time.time()
print(f"rt:{et-st}")

