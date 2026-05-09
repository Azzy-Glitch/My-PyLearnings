import matplotlib.pyplot as plt
import numpy as np

# Bar Charts = A bar chart is a graph that represents categorical data with rectangular bars with heights or lengths proportional to the values that they represent.

categories = np.array(['Fruits', 'Vegetables', 'Proteins', 'Dairy', 'Sweets'])
values = [3, 5, 7, 9, 11]

plt.bar(categories, values, color = 'blue') # To create a bar chart
# plt.barh(categories, values, color = 'orange') # To create a horizontal bar chart

plt.xlabel('Categories') # To set the x-axis label
plt.ylabel('Values') # To set the y-axis label
plt.title('Bar Chart Example') # To set the title of the bar chart

plt.show() # To show the bar chart