import matplotlib.pyplot as mlt
import matplotlib.pyplot as plt
import numpy as np  
figure,axes=plt.subplots(2,2) 
axes[0,0].plot([1,2,3],[4,5,6])
axes[0,0].set_title("Subplot1")
axes[0,1].plot([1,2,3],[6,5,4])
axes[0,1].set_title("Subplot2")
axes[1,0].plot([1,2,3],[4,6,5])
axes[1,0].set_title("Subplot3")
axes[1,1].plot([1,2,3],[5,4,6])
axes[1,1].set_title("Subplot4")
plt.tight_layout()
plt.show() 