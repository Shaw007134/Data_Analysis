import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("./data/HR.csv")
df = df[df["last_evaluation"]<=1][df["salary"]!="nme"][df["department"]!="sale"]
sns.set_style(style="darkgrid")
sns.set_context(context="poster", font_scale=0.8)
sns.set_palette(sns.color_palette("RdBu", n_colors=7))
# BAR GRAPH 柱状图
# sns.countplot(x="salary", hue="department", data=df)
# plt.title("Salary")
# plt.xlabel("salary")
# plt.ylabel("number")
# salary = df["salary"].value_counts()
# plt.xticks(np.arange(len(salary))+0.5, salary.index)
# plt.axis([0, 4, 0, 10000])
# plt.bar(np.arange(len(salary))+0.5, salary, width=0.5)
# for x, y in zip(np.arange(len(salary))+0.5, salary):
#     plt.text(x, y, y, ha="center", va="bottom")
plt.show()

#HISTOGRAM 直方图
# satisfaction = df["satisfaction_level"]
# last_eva = df["last_evaluation"]
# avg_mhs = df["average_monthly_hours"]
# f = plt.figure()
# f.add_subplot(1, 3, 1)
# #kde分布，hist直方
# sns.distplot(satisfaction, bins=10)
# f.add_subplot(1, 3, 2)
# sns.distplot(last_eva, bins=10)
# f.add_subplot(1, 3, 3)
# sns.distplot(avg_mhs, bins=10)
# plt.show()

#BOX PLOT箱线图
#saturation, whis
# tsc = df["time_spend_company"]
# sns.boxplot(x=tsc,saturation=0.75,whis=3)
# plt.show()

#LINE PLOT (POINT PLOT) 折线图
# sub_df = df.groupby("time_spend_company").mean()
# # sns.pointplot(sub_df.index, sub_df["left"])
# sns.pointplot(x="time_spend_company", y="left", data=df)
# plt.show()

# PIE 饼图
lbs = df["department"].value_counts().index
explodes = [0.1 if i =="sales" else 0 for i in lbs]
plt.pie(df["department"].value_counts(normalize=True), explode=explodes, labels=lbs, autopct="%1.1f%%", colors=sns.color_palette("Reds"))
plt.show()
