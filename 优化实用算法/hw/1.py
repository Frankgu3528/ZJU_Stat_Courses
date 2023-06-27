import numpy as np
import matplotlib.pyplot as plt

n = np.arange(1,100000)
f = [1-(1-1/i)**i for i in n]
plt.plot(np.log(n),f)
plt.show()