import numpy as np
import sympy
from sympy import diff


n = 10 # 指定n
x = sympy.symbols('x:' + str(n))
def extended_rosenbrock_sympy(x):
    """
    计算函数值
    """
    n = len(x)
    f = 0
    for i in range(n-1):
        f += 100 * (x[i+1] - x[i]**2)**2 + (1 - x[i])**2
    return f


def grad(x_k):
    """
    计算导数值
    """
    df = [sympy.diff(extended_rosenbrock_sympy(x), xi).subs(zip(x, x_k)) for xi in x]
    df_func = sympy.lambdify(x, df)
    # 将四个导数拼成一个一维数组
    df_array = np.array(df_func(*x_k))
    return df_array


def BFGS(fun, grad, x0, max_iter=1000, epsilon=1e-5):
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
        if abs(fun(x0)) < epsilon:
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

x_0 = np.array([1 if i%2!=0 else -1.2 for i in range(n)]).astype(float)

print(BFGS(extended_rosenbrock_sympy,grad,x_0))