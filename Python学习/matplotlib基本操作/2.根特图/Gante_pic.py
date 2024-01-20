# Importing the matplotlib.pyplot
import matplotlib.pyplot as plt

fig, gnt = plt.subplots()   # Declaring a figure "gnt"

gnt.set_ylim(0, 50)         # Setting Y-axis limits
gnt.set_xlim(0, 160)        # Setting X-axis limits

# Setting labels for x-axis and y-axis
gnt.set_xlabel('seconds since start')
gnt.set_ylabel('Processor')


gnt.set_yticks([15, 25, 35])            # Setting ticks on y-axis
gnt.set_yticklabels(['1', '2', '3'])    # Labelling tickes of y-axis

# Setting graph attribute
# gnt.grid(True)

gnt.broken_barh([(40, 50)], (30, 10), facecolors='tab:orange')    # Declaring a bar in schedule
gnt.broken_barh([(110, 10), (150, 10)], (10, 10), facecolors='tab:blue')
gnt.broken_barh([(130, 10)], (10, 10), facecolors='tab:orange')    # Declaring multiple bars in at same level and same width
gnt.broken_barh([(10, 50), (100, 20), (130, 10)], (20, 10), facecolors='tab:red')

plt.show()      # plt.savefig("gantt1.png")

