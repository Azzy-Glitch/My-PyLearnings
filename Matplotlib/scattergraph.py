import matplotlib.pyplot as plt
import numpy as np

# Scatter graphs = A type of graph that uses dots to represent values for two different numeric variables.
# The position of each dot on the horizontal and vertical axis indicates values for an individual data point.

x1 = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])#Hours Studied
y1 = np.array([99, 86, 87, 88, 100, 86, 103, 87, 94, 78, 77, 85, 86])#Marks Scored

x2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])#Hours Studied
y2 = np.array([86, 85, 88, 90, 95, 80, 100, 85, 92, 78, 75, 80, 82])#Marks Scored

plt.scatter(x1, y1, color="skyblue",
                  edgecolor='black',
                  alpha=0.75,
                  s=100,
                  label='Class A')

plt.scatter(x2, y2, color="salmon",
                  edgecolor='black',
                  alpha=0.75,
                  s=100,
                  label='Class B')

plt.title('Class A vs Class B')
plt.xlabel('Hours Studied')
plt.ylabel('Marks Scored')
plt.legend()
plt.show()
