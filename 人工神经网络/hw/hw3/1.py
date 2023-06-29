import numpy as np
import matplotlib.pyplot as plt

lr = np.ones(500)
epoch = np.arange(1,501)

for i in range(len(lr)):
    if i<200:
        lr[i] = 1e-3
    elif 200<=i<300:
        lr[i] = 5e-4
    elif 300<=i<400:
        lr[i] = 1e-4
    elif 400<=i<500:
        lr[i] = 1e-5
plt.xlabel("epoch")
plt.ylabel("Learning_Rate")
plt.title("Learning_Rate---epoch")
plt.plot(epoch,lr)
plt.show()
