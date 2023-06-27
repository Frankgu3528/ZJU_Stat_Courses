import numpy as np
from sympy import symbols, diff, hessian, Matrix

x1, x2, x3, x4 = symbols('x1 x2 x3 x4')
f = (x1+10*x2)**2+5*(x3-x4)**2+(x2-2*x3)**4+10*(x1-x4)**4
def fun(x):
    return (x[0]+10*x[1])**2+5*(x[2]-x[3])**2+(x[1]-2*x[2])**4+10*(x[0]-x[3])**4

def grad(x_k):
    """
    计算f在x_k点的导数值
    """
    a = x_k[0];b = x_k[1];c = x_k[2];d= x_k[3]
    df_da = diff(f, x1)
    df_db = diff(f, x2)
    df_dc = diff(f, x3)
    df_dd = diff(f, x4)
    df_da_value = df_da.subs({x1: a, x2: b,x3:c,x4:d})
    df_db_value = df_db.subs({x1: a, x2: b,x3:c,x4:d})
    df_dc_value = df_dc.subs({x1: a, x2: b,x3:c,x4:d})
    df_dd_value = df_dd.subs({x1: a, x2: b,x3:c,x4:d})
    return np.array([df_da_value,df_db_value,df_dc_value,df_dd_value])

def BFGS(fun, grad, x0, max_iter=100, epsilon=1e-5):
    """
    fun: 目标函数
    grad: 目标函数的梯度
    x0: 初始点
    max_iter: 最大迭代次数
    epsilon: 收敛精度
    """
    n = len(x0)
    I = np.identity(n)
    H = I
    k = 0
    while (k<max_iter):
        # 计算梯度
        g = grad(x0)

        # 判断是否收敛
        if fun(x0) < epsilon:
            break
        # 更新步长
        p = -np.dot(H, g)

        # 一维搜索求最优步长alpha
        alpha = 1.0
        rho = 0.9
        c = 1e-4
        while fun(x0 + alpha * p) > fun(x0) + c * alpha * np.dot(g, p):
            alpha = rho * alpha

        # 更新x
        s = alpha * p
        x1 = x0 + s

        # 计算梯度差和参数差
        y_k = grad(x1) - g
        s_k = x1 - x0

        # 更新H(这里的H其实是inv(B_k))
        H = np.dot((I - np.outer(s_k, y_k) / np.dot(y_k, s_k)), np.dot(H, (I - np.outer(y_k, s_k) / np.dot(y_k, s_k)))) + np.outer(s_k, s_k) / np.dot(y_k, s_k)

        # 更新x0
        x0 = x1
        k+=1
    # 返回最优解和最优值
    return k,x0, fun(x0)

x_0 = np.array([3,-1,0,1]).astype(float)

print(BFGS(fun,grad,x_0))