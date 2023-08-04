"""
===========
Broken Barh
===========
Make a "broken" horizontal bar plot, i.e., one with gaps
Created on Wed Nov  20 16:53:08 2018
@author: jherfson
"""
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.broken_barh([(-257.41, 2333.07)], (0, 0.25), facecolors='pink')  # SnO2 ok
ax.broken_barh([(-257.41, 2019.61)], (0.25, 0.25), facecolors='violet')  # WO3 ok
ax.broken_barh([(-257.41, 642.28)], (0.50, 0.25), facecolors='red')  # MnO2 ok
ax.broken_barh([(384.77, 612.95)], (0.50, 0.25), facecolors='orange')  # Mn2O3 ok
ax.broken_barh([(568.43, 1213.29)], (0.75, 0.25), facecolors='black')  # MnWO4 ok
ax.broken_barh([(997.72, 642.88)], (0.50, 0.25), facecolors='Silver')  # Mn3O4 ok
ax.broken_barh([(1385.01, 725.74)], (1.50, 0.25), facecolors='Brown')  # MnSnO3 ok


#  printing-subscript
SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")

fonte = int(14)

# legend of phase
ax.text(675, 0.330, 'WO3'.translate(SUB), fontsize=fonte)
ax.text(140, 0.60, 'MnO2'.translate(SUB), fontsize=fonte)
ax.text(675, 0.090, 'SnO2'.translate(SUB), fontsize=fonte)
ax.text(660, 0.60, 'Mn2O3'.translate(SUB), fontsize=fonte)
ax.text(900, 0.845, 'MnWO4'.translate(SUB), fontsize=fonte, color='White')
ax.text(1150, 0.60, 'Mn3O4'.translate(SUB), fontsize=fonte)
ax.text(1650, 1.60, 'MnSnO3'.translate(SUB), fontsize=fonte)


ax.set_xlim(0, 13500)
# x = range(0, 1400, 150)
# ax.set_xticks(x)
# ax.set_xticklabels([i for i in x])
ax.set_xlabel('Temperature (°C)')
ax.set_yticks([])

# ax.grid(True)

plt.show()