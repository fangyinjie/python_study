import numpy as np
from sko.GA import GA
import matplotlib.pyplot as plt


def schaffer(p):
    # This function has plenty of local minimum, with strong shocks global minimum at (0,0) with value 0
    x = p[0]
    return 5 * np.sin(np.log(x))


ga = GA(func=schaffer, n_dim=1, size_pop=100, max_iter=800, lb=0, ub=10, precision=1e-7)
best_x, best_y = ga.run()
print('best_x:', best_x, '\n', 'best_y:', best_y)
x = np.arange(0, 10, 0.01)
y = 5 * np.sin(np.log(x))
plt.plot(x, y)
plt.show()
