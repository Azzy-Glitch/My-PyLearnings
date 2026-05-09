import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 5, 7, 11])
z = np.array([1, 4, 9, 16, 25])
g = np.array([1, 8, 27, 64, 125])

plt.title('Simple Plot', fontsize=20,
                         color='red',
                         family='serif',
                         weight='bold',
                         style='italic')

plt.xlabel('X-axis', fontsize=15,
                     color='cyan',
                     family='Arial',
                     weight='bold')

plt.ylabel('Y-axis', fontsize=15,
                     color='green',
                     family='Times New Roman',
                     weight='bold')

plt.xticks(x, fontsize=12,
           color='blue',
           family='Comic Sans MS',
           weight='bold')

plt.yticks(y, fontsize=12,
           color='magenta',
           family='Verdana',
           weight='bold')

# plt.tick_params(axis='both', which='major', labelsize=10,
#                 color='orange', width=2, length=10)

plt.plot(x, y)
plt.plot(x, z)
plt.plot(x, g)

plt.show()