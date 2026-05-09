import matplotlib.pyplot as plt
import numpy as np

# Grid = Helps to read the values of the graph more easily

x=np.array([1, 2, 3, 4, 5])
y=np.array([2, 3, 5, 7, 11])

plt.plot(x, y)

plt.grid(axis = 'both', # To show the gridlines on both x and y axis
         linewidth = 2,
         color = "black",
         linestyle = 'dashed') # To show the gridlines

plt.show() # To show the graph without gridlines