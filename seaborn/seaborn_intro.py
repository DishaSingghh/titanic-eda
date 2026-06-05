import seaborn as sns;
import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;
sns.get_dataset_names()
train=pd.read_csv(r"C:\Users\disha\Downloads\train.csv")
df=pd.DataFrame(train)
# print(df["Age"].value_counts())
# print(df.columns)
sns.scatterplot(x="Age",y="Fare",data=df,hue="Sex",palette="dark")
sns.set_context("paper",font_scale=1.5)
plt.xlabel("Age")
plt.ylabel("Fare")

plt.show()
