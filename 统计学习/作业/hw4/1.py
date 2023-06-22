import numpy as np
import math 
import matplotlib.pylab as plt
p = np.linspace(0.0001,0.9999,1000)

jini = np.array([2*x*(1-x) for x in p])
claerror = np.array([1- max(x,(1-x)) for x in p])
entropy = np.array([-x*math.log(x)-(1-x)*math.log(1-x) for x in p])
plt.xlabel("$\hat{p}_{m1}$")
plt.ylabel("classification error")
plt.title("classification error")
plt.plot(p,jini,label="Gini index")
plt.plot(p,claerror,label = "classification error")
plt.plot(p,entropy,label = "entropy")
plt.legend()
plt.show()
