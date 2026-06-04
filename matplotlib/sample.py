import matplotlib as mpl;
import matplotlib.pyplot as plt;
import numpy as np;
import pandas as pd;
df=pd.read_csv("train.csv");
bar=plt.bar(df["Pclass"],df["Age"]);
print(df["Age"])
print(df["Pclass"])
plt.xlabel("Pclass");   
plt.ylabel("Age");
plt.title("Bar Chart");
plt.show();

