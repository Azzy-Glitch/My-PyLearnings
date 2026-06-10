import matplotlib.pyplot as plt
import numpy as np

# Histograms = A type of graph that uses bars to represent the frequency of data points in successive numerical intervals.
#              The taller the bar, the more data points fall in that range of values.
#              Histograms look similar to bar graphs, but they group numbers into ranges. If you have ten data points that fall between 0 and 10, they are all represented by a single bar.
#              They Group values into bins and are used to plot the frequency of the data points in each bin.

x = np.random.normal(loc=50, scale=15, size=1000) # Data Points
x = np.clip(x, 0, 100) # Clipping the data points to be between 0 and 100

# x = np.array([22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27]) # Data Points

plt.hist(x, bins=10, color="skyblue",
         edgecolor='black',
          alpha=0.75) # bins = Number of bars in the histogram, alpha = Transparency of the bars

plt.title('Data Points Distribution')
plt.xlabel('Value Ranges')
plt.ylabel('Frequency')
plt.show()
