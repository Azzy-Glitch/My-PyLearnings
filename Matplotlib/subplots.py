import matplotlib.pyplot as plt
import numpy as np

# Figure = The Entire Window or Page the graph is on
# Axes = The area on which the data is plotted (can have multiple axes on a figure)

# print(plt.subplots(2, 2))  # returns a tuple containing a figure and axes object(s)
x = np.array([1, 2, 3, 4])
fig, axs = plt.subplots(2, 2)
# axs[0, 0].plot(np.random.rand(10))
# axs[0, 1].plot(np.random.rand(10))

axs[0, 0].plot(x, x**2, color='red', label='x^2')
axs[0, 1].plot(x, x**3, color='blue', label='x^3')
axs[1, 0].plot(x, np.sqrt(x), color='green', label='sqrt(x)')
axs[1, 1].plot(x, np.log(x), color='orange', label='log(x)')

plt.tight_layout()  # Adjusts the spacing between subplots to prevent overlap
plt.legend()  # Add a legend to each subplot
# plt.suptitle('Multiple Subplots Example')  # Add a title to the entire figure
# plt.style.use('ggplot')  # Use a predefined style for better aesthetics

plt.show()