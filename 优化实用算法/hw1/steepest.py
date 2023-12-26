'''
第三题中steepest descend法的代码
'''
import numpy as np
from sympy import symbols, diff, hessian
x, y = symbols('x y')
# f = 100*(y-x**2)**2 + (1-x)**2
f = (1.5-x+x*y)**2+(2.25-x+x*y*y)**2+(2.625-x+x*y*y*y)**2
# 计算在(x1,x2)处的偏导数值
def partial_fx(x_k):
    x1 = x_k[0];x2 = x_k[1]
    df_dx = diff(f, x)
    df_dy = diff(f, y)
    df_dx_value = df_dx.subs({x: x1, y: x2})
    df_dy_value = df_dy.subs({x: x1, y: x2})
    return np.array([df_dx_value,df_dy_value])

x0 = np.array([-1.2,1])
x_k = x0
for i in range(1,1000):
    g_k = partial_fx(x_k) 
    print("iter:",i," ",x_k)
    t = 1
    # 使用Armijo规则进行一维线搜索
    while f.subs({x: x_k[0]-t*g_k[0], y: x_k[1]-t*g_k[1]}) > (f.subs({x: x_k[0], y: x_k[1]}) - 0.1*t*np.dot(g_k.T, g_k)):
        t *= 0.5
        # 防止步长过小导致无限循环
        if t <  1e-6:
            break
    x_k = x_k - t*g_k

