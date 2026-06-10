import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("D:\Git Repository\My-PyLearnings\Pandas\data.csv")

type_count = df["Type1"].value_counts()

print(df.head())
plt.barh(type_count.index, type_count.values)
plt.xlabel("Type1")
plt.ylabel("Count")
plt.title("Count of Each Type1")
plt.tight_layout()
plt.show()

plt.pie(type_count.values, labels=type_count.index, autopct="%1.1f%%")
plt.title("Distribution of Type1")
plt.axis("equal")
plt.tight_layout()
plt.show()
