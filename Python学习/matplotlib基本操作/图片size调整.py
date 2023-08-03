import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

x = [1, 2, 3, 4, 5]

y = [10, 5, 15, 10, 20]

figure(num=None, figsize=(128, 6), dpi=80, facecolor='w', edgecolor='k')

# plt.plot(x, y, 'ro-', color='blue')
plt.plot(x, y, 'ro-')

plt.savefig('testblueline.jpg')

plt.savefig('testblueline.pdf')

plt.show()

