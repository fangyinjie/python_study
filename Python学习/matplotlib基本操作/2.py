import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y, color='blue', linestyle='-', label='sin(x)')
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.legend(loc='upper left')
ax.grid(True)
# ax.title('Sine Function')
plt.show()
