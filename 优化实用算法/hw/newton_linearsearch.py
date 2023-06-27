'''
第四题中带线搜索的newton法的代码
'''
import numpy as np
import math
from sympy import symbols, diff, hessian, Matrix
sigma = 10000
x1, x2, x3, x4 = symbols('x1 x2 x3 x4')
# 计算在(x1,x2)处的偏导数值
X = Matrix([x1, x2, x3, x4])
A = Matrix([[5, 1, 0,1], [1,4,0.5,0], [0,0.5,3,0],[0.5,0,0,2]])
f = 0.5*X.T*X+0.25*sigma*(X.T*A*X)**2
def partial_fx(x_k):
    a = x_k[0];b = x_k[1];c = x_k[2];d= x_k[3]
    df_da = diff(f, x1)
    df_db = diff(f, x2)
    df_dc = diff(f, x3)
    df_dd = diff(f, x4)
    df_da_value = df_da.subs({x1: a, x2: b,x3:c,x4:d}).tolist()
    df_db_value = df_db.subs({x1: a, x2: b,x3:c,x4:d}).tolist()
    df_dc_value = df_dc.subs({x1: a, x2: b,x3:c,x4:d}).tolist()
    df_dd_value = df_dd.subs({x1: a, x2: b,x3:c,x4:d}).tolist()
    return np.array([df_da_value[0][0],df_db_value[0][0],df_dc_value[0][0],df_dd_value[0][0]])
    
# 计算海森矩阵
def hes_fx(x_k):
    H = hessian(f, [x1, x2,x3,x4])
    H_value = H.subs({x1: x_k[0], x2: x_k[1],x3:x_k[2],x4:x_k[3]})
    H_value = np.array(H_value).astype(np.float64)
    return H_value
x0 = np.array([math.cos(math.radians(50)),math.sin(math.radians(50)),math.cos(math.radians(50)),math.sin(math.radians(50))])
x_k = x0
for i in range(1,200):
    print("iter:",i," ",x_k)
    H_T = np.linalg.inv(hes_fx(x_k))
    g_k = partial_fx(x_k)
    t = 1
    # 使用Armijo规则进行一维线搜索
    while f.subs({x1: x_k[0]-t*g_k[0], x2: x_k[1]-t*g_k[1],x3: x_k[2]-t*g_k[2],x4: x_k[3]-t*g_k[3]}).tolist()[0][0] > (f.subs({x1: x_k[0], x2: x_k[1],x3: x_k[2],x4: x_k[3]}).tolist()[0][0] - 0.1*t*np.dot(g_k.T, g_k)):
        t *= 0.5
        # 防止步长过小导致无限循环
        if t <  1e-6:
            break
    print(t)
    x_k = x_k - t*np.dot(H_T,g_k)
