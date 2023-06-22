import numpy as np

D = np.diag([4,3,5])
L = np.array([[0,0,0],
              [1,0,0],
              [-2,-2,0]])
U = np.array([[0,-1,1],
              [0,0,-1],
              [0,0,0]])
M = np.dot(np.linalg.inv(D),(L+U))
b = np.array([5,-4,1])
x1 = 0;x2 = 0;x3 = 0
x = np.array([x1,x2,x3])
for i in range(20):
    x = np.dot(M,x.T)+np.dot(np.linalg.inv(D),b.T)
    if (i<3):
        print(x)
print("final: ",x)