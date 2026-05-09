import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 5, 7, 11])
z = np.array([1, 4, 9, 16, 25])
g = np.array([1, 8, 27, 64, 125])

# plt.plot(x, y, marker='o',
#             markersize=20, 
#             mfc="cyan",
#             linestyle='--',
#             linewidth=4,
#             color='cyan')
 
line_style = dict(marker='o',
            markersize=20, 
            mfc="cyan",
            linestyle='--',
            linewidth=4,)

plt.plot(x, y, color= "red", **line_style)
plt.plot(x, z, color= "blue", **line_style)
plt.plot(x, g, color= "green", **line_style)

plt.show()