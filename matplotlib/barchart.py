import matplotlib as mpl;
import matplotlib.pyplot as plt;
import numpy as np;
scores=np.random.normal(loc=80, scale=10, size=100);
plt.hist(scores);
plt.show();
          