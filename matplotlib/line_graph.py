import matplotlib;
import matplotlib.pyplot as plt;
import numpy as np
arr=np.array([2020,2021,2022,2023,2024]);
arr1=np.array([7.0,6.5,6.0,8.5,5.0]);
plt.plot(arr,arr1,marker='o',linestyle=':',color='r');
dicttitle={"fontsize": 20, "color": 'b', "fontweight": 'bold'};
plt.title("Line Graph", dicttitle);
plt.xlabel("years");
plt.ylabel("float");
plt.grid(axis="y",linestyle='--',color='g');
plt.show();

