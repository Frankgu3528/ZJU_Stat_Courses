'''
第三题中newton法的代码
'''
import math 
import numpy as np
from sympy import symbols, diff, hessian
from sympy import sqrt
x, y = symbols('x y')
# f = 100*(y-x**2)**2 + (1-x)**2
f = (x-sqrt(4-4*y**2))**2+(4/x-y)**2
# 计算在(x1,x2)处的偏导数值
def partial_fx(x_k):
    x1 = x_k[0];x2 = x_k[1]
    df_dx = diff(f, x)
    df_dy = diff(f, y)
    df_dx_value = df_dx.subs({x: x1, y: x2})
    df_dy_value = df_dy.subs({x: x1, y: x2})
    return np.array([df_dx_value,df_dy_value]).astype(np.float64)
# 计算在(x1,x2)处的海森矩阵
def hes_fx(x_k):
    x1 = x_k[0];x2 = x_k[1]
    H = hessian(f, [x, y])
    H_value = H.subs({x: x1, y: x2})
    H_value = np.array(H_value).astype(np.float64)
    return H_value
x0 = np.array([2,0.7])
x_k = x0
for i in range(1,20):
    print("iter:",i," ",x_k," f: ",f.subs({x: x_k[0], y: x_k[1]}))
    H_T = np.linalg.inv(hes_fx(x_k))
    g_k = partial_fx(x_k)
    x_k = x_k - np.dot(H_T,g_k)

q = float(f.subs({x: x_k[0], y: x_k[1]}))
print(np.sqrt(q))
