import matplotlib.pyplot as plt
import numpy as np

# pie charts = A type of chart that shows the relationship of parts to a whole.
# The size of each piece is determined by the percentage of the whole that it represents.

categories = np.array(['Python', 'C++', 'Ruby', 'Java'])
percentages = [215, 130, 245, 210]
colors = ["#e02323", "#1D77D1", "#0FB70F", "#dd7c1b"]

plt.pie(percentages, labels=categories, colors=colors,
                     autopct='%1.1f%%')

# plt.pie(percentages, labels=categories, colors=colors,
#                      autopct='%1.1f%%',
#                      startangle=90,
#                      shadow=True, 
#                      explode=(0.1, 0, 0, 0))


plt.title('My Favorite Programming Languages')
plt.xlabel('Programming Languages')
plt.ylabel('Percentages')

plt.show()