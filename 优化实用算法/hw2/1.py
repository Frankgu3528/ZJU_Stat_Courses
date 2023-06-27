import numpy as np
def hilbert_matrix(n):
    """
    生成一个nxn的希尔伯特矩阵
    """
    x, y_k = np.meshgrid(np.arange(1, n+1), np.arange(1, n+1))
    h = 1 / (x + y_k - 1)
    return h

def conjugate_gradient(A, b, x0, max_iter=1000, tol=1e-6):
    """
    使用共轭梯度法求解线性方程组 Ax=b
    :param A: 系数矩阵
    :param b: 右侧向量
    :param x0: 初始猜测解
    :param max_iter: 最大迭代次数
    :param tol: 收敛精度
    :return: 解向量
    """
    r0 = np.dot(A, x0) - b
    p0 = -r0
    x = x0
    i = 0
    while (i<max_iter):
        alpha = np.dot(r0.T, r0) / np.dot(p0.T, np.dot(A, p0))
        x = x + alpha * p0
        r1 = r0 + alpha * np.dot(A, p0)
        i+=1
        if np.linalg.norm(r1) < tol:
            print(np.linalg.norm(r1))
            break
        beta = np.dot(r1.T, r1) / np.dot(r0.T, r0)
        p0 = -r1 + beta * p0
        r0 = r1
    return x,i

# 测试
n = 12
A = hilbert_matrix(n)
b = np.ones(n)
x0 = np.zeros_like(b)
x,iter = conjugate_gradient(A, b, x0)
print(np.linalg.solve(A,b)) # 作为对照
print(iter,x)

