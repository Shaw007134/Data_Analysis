import pandas as pd
import numpy as np

df=pd.read_csv("./data/HR.csv")

import seaborn as sns
import matplotlib.pyplot as plt
plt.title("Salary")
plt.xlabel("salary")
plt.ylabel("number")

salary = df["salary"].value_counts()
plt.xticks(np.arange(len(salary)), salary.index)
plt.axis([0, 4, 0,10000])
plt.bar(np.arange(len(salary))+0.5, salary)
plt.show()
