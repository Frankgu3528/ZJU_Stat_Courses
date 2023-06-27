# 作业2

###### 顾格非 3210103528

![image-20230427213203939](C:\Users\阿漆\AppData\Roaming\Typora\typora-user-images\image-20230427213203939.png)

首先我们准备好n阶的Hilbert matrix：

```python
def hilbert_matrix(n):
    x, y_k = np.meshgrid(np.arange(1, n+1), np.arange(1, n+1))
    h = 1 / (x + y_k - 1)
    return h
```

然后是共轭梯度法的实现部分, 参照下面的步骤完成下面的代码：
$$
\begin{aligned}
\textsf{Set}r_0& \leftarrow Ax_0-b,p_0\leftarrow-r_0,k\leftarrow0;\\
\alpha_k & \leftarrow \frac{r_k^T r_k}{p_k^T A p_k} \\
x_{k+1} & \leftarrow x_k+\alpha_k p_k \\
r_{k+1} & \leftarrow r_k+\alpha_k A p_k \\
\beta_{k+1} & \leftarrow \frac{r_{k+1}^T r_{k+1}}{r_k^T r_k} \\
p_{k+1} & \leftarrow-r_{k+1}+\beta_{k+1} p_k \\
k & \leftarrow k+1
\end{aligned}
$$

```python
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
```

使用不同的n进行实验，下面是不同n下 $residual ~~norm<10^{-6}$的迭代次数比较：

| n    | 迭代次数 | residual norm          |
| ---- | -------- | ---------------------- |
| 5    | 6        | 2.624726839172203e-09  |
| 8    | 18       | 1.8915472281855566e-08 |
| 12   | 36       | 6.532510855464922e-07  |
| 20   | 74       | 6.77958998367044e-07   |

### 结果分析

* 可以看出，随着n的增大，共轭梯度法需要更多的迭代次数来达到所需的精度。
* 通过输出每次迭代的residential norm，可以看出n增大后迭代会呈现多次的波动，不过最后经过足够的迭代次数后都收敛到了所给的精度范围内。

***

![image-20230430192132658](C:\Users\阿漆\AppData\Roaming\Typora\typora-user-images\image-20230430192132658.png)

Preconditioned CG的主要目的是借用C 来改善原来的A矩阵的特征值分布，从而加速收敛，这里用了$\hat{x}=Cx$, 把其代入后要最小化的函数变成了：

$$
\hat{\phi}(\hat{x})=\dfrac{1}{2}\hat{x}^T(C^{-T}AC^{-1})\hat{x}-(C^{-T}b)^T\hat{x}
$$
所以现在就是解$(C^{-T}AC^{-1})\hat{x}=C^{-T}b $这个方程：方法是把原来标准CG法中的A换成$C^{-T}AC^{-1}$, b 换成$C^{-T}b $计算：
在preconditioned CG中，我们令$p_0 = -y_0, My_0 = r_0$，于是得到下面两个方程：
$$
\begin{gathered}
\hat{r}_0=C^{-T} A C^{-1} \hat{x}_0-C^{-T} b=C^{-T}\left(A x_0-b\right)=C^{-T} r_0 \\
\hat{p}_0=-\hat{r}_0=-C^{-T} r_0
\end{gathered}
$$

$$
\hat{\alpha}_0=\frac{\left(C^{-T} r_0\right)^T\left(C^{-T} r_0\right)}{\left(C^{-1} \hat{p}_0\right)^T A\left(C^{-1} \hat{p}_0\right)}=\frac{r_0^T \cdot C^{-1} C^{-T} r_0}{\left(C^{-1} \hat{p}_0\right)^T A\left(C^{-1} \hat{p}_0\right)}=\frac{r_0^T y_0}{p_0^T A p_0}
$$
由上面两式，可以推出M：
$$
\left\{\begin{array}{l}C^{-1}C^{-T}r_0=y_0=M^{-1}r_0\\ C^{-1}\hat p_0=-C^{-1}C^{-T}r_0=p_0=-M^{-1}r_0\end{array}\right.\Rightarrow M=C^TC
$$
我们计算剩下的几步：
$$
\hat{\beta}_{k+1}=\dfrac{\hat{r}_{k+1}^T\hat{r}_{k+1}}{\hat{r}_k^T\hat{r}_k}=\dfrac{r_{k+1}^T\left(C^{-1}C^{-T}r_{k+1}\right)}{r_k^T\left(C^{-1}C^{-T}r_k\right)}=\dfrac{r_{k+1}^T y_{k+1}}{r_k^T y_k}
$$
$$
\begin{aligned}
p_{k+1}& =C^{-1}\hat{p}_{k+1}=C^{-1}\left(-C^{-T}r_{k+1}+\hat{\beta}_{k+1}Cp_k\right)  \\
&=-C^{-1}C^{-T}r_{k+1}+\hat{\beta}_{k+1}p_k \\
&=-y_{k+1}+\hat{\beta}_{k+1}p_k
\end{aligned}
$$

于是我们可以不显示的在preconditioned CG中写出C，而是全换成用M表达，得到最终的preconditioned CG：

![image-20230430205850208](C:\Users\阿漆\AppData\Roaming\Typora\typora-user-images\image-20230430205850208.png)


***

### 3

![image-20230430210318258](C:\Users\阿漆\AppData\Roaming\Typora\typora-user-images\image-20230430210318258.png)
$$
\begin{aligned}
\text{det}\left(B_{k+1}\right)& =\det\left(B_{k+1}^{BFGS} + \phi_k\left(s_k^TB_ks_k\right)v_kv_k^T\right)  \\
&=\det\left(B_{k+1}^{BFGS}\right)\det\left(I+\phi_k\left(s_k^TB_ks_k\right)\left(B_{k+1}^{BFGS}\right)^{-1}v_kv_k^T\right) \\
&=\det\left(B_{k+1}^{BFGS}\right)\left(1+\phi_k\left(s_k^TB_ks_k\right)v_k^T\left(B_{k+1}^{BFGS}\right)^{-T}v_k\right) \\
&(其中B_{k+1}^{BFGS}=B_k-\dfrac{B_k s_k s_k^T B_k}{s_k^TB_k s_k}+\dfrac{y_ky_k^T}{y_k^Ts_k})
\end{aligned}
$$


$$
我们接下来证明1+\phi_k\left(s_k^TB_ks_k\right)\cdot v_k^T\left(B_{k+1}^{BFGs}\right)^{-T}v_k=0:\\
\begin{gathered}
1+\phi_k\left(s_k^TB_ks_k\right)\cdot v_k^T\left(B_{k+1}^{BFGs}\right)^{-T}v_k \\

=1+\frac{\left(s_{K}^{T}y_{k}\right)^{2}}{\left(s_{k}^{T}y_{k}\right)^{2}-\left(s_{k}^{T}B_{k}s_{k}\right)\left(y_{k}^{T}H_{k}g_{k}\right)}\cdot v_k^T\left[\left(I-\rho_k s_k y_k^T\right)H_k\left(I-\rho_k y_k s_k^T\right)+\rho_k s_k s_k^T\right]v_k\\这里用到了(B_{k+1}^{BFGS})^{-1}=\left(I-\rho_k s_k y_k^T\right)H_k\left(I-\rho_k y_k s^T\right)+\rho_k s_k s^T\\
=1+\frac{\left(s_{K}^{T}y_{k}\right)^{2}}{\left(s_{k}^{T}y_{k}\right)^{2}-\left(s_{k}^{T}B_{k}s_{k}\right)\left(y_{k}^{T}H_{k}g_{k}\right)}\cdot \left(\dfrac{y_k^T}{y_k^T s_k}-\dfrac{s_k^T B_k}{s_kB_k s_k}\right)H_k\left(\dfrac{y_k}{y_k^T s_k}-\dfrac{B_k s_k}{s_k^T B_k s_k}\right)\\

=1+\frac{\left(s_{K}^{T}y_{k}\right)^{2}}{\left(s_{k}^{T}y_{k}\right)^{2}-\left(s_{k}^{T}B_{k}s_{k}\right)\left(y_{k}^{T}H_{k}g_{k}\right)}\cdot\left(s_{k}^{T}B_{k}s_{k}\right)\cdot\frac{\left(y_{k}^{T}H_{k}y_{k}\right)\left(s_{k}^{T}B_{k}s_{k}\right)-\left(y_{k}^{T}s_{k}\right)^{2}}{\left(y_{k}^{T}s_{k}\right)^{2}\left(s_{k}^{T}B_{k}s_{k}\right)} \\
=1-1=0 \\
故det(B_{k+1})=0，即B_{k+1}是singular的.
\end{gathered}
$$



***

![image-20230427214936717](C:\Users\阿漆\AppData\Roaming\Typora\typora-user-images\image-20230427214936717.png)

首先我们准备好计算$f(x)，grad(f(x))$的计算函数：

```python
def extended_rosenbrock_sympy(x):
    n = len(x)
    f = 0
    for i in range(n-1):
        f += 100 * (x[i+1] - x[i]**2)**2 + (1 - x[i])**2
    return f
def grad(x_k):
    df = [sympy.diff(extended_rosenbrock_sympy(x), xi).subs(zip(x, x_k)) for xi in x]
    df_func = sympy.lambdify(x, df)
    df_array = np.array(df_func(*x_k))
    return df_array
```

然后完成BFGS的主函数：

```python
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
```
$$
B_{k+1}=B_k-\frac{B_k s_k s_k^T B_k}{s_k^T B_k s_k}+\frac{y_k y_k^T}{y_k^T s_k}
$$
这里我不是按上面的公式直接更新$B_{k+1}$，而是选择更新$H_{k+1}=B_{k+1}^{-1}$ , 这样避免求$B_{k+1}$的逆带来的复杂。
$$
H_{k+1}=\left(I_n-\frac{s_k y_k^T}{y_k^T s_k}\right) H_k\left(I_n-\frac{y_k s_k^T}{y_k^T s_k}\right)+\frac{s_k s_k^T}{y_k^T s_k}
$$

### 结果：

| n    | 迭代次数 | 误差                   |
| ---- | -------- | ---------------------- |
| 6    | 75       | 2.966154355880596e-06  |
| 8    | 83       | 1.4750701116694114e-06 |
| 10   | 113      | 1.840508350662231e-06  |

n=6时

$x=(0.99993813, 0.99997309, 1.00005015, 1.00015015, 1.00026079,
       1.00045491)$

n=8 时 $x = (1.00000972, 0.99998852, 1.00001296, 0.99997958, 0.99993918,
       0.99983456, 0.99959476, 0.99921299)$

n=10时

$x=(1.00002206, 1.0000238 , 0.99999981, 0.99998003, 1.00000715,
       0.99998502, 0.99996121, 0.99982655, 0.99962816, 0.99928181)$

### 4-2

minimize the Power singular function, 方法同上（就不帖代码了，可以在提交的文件夹中找到）

**Result：**

经过18次迭代，得到$x=(-0.0383479273638743, 0.00387012863609520, -0.0139938967644757,
       -0.0138523889653648)$, 

此时的误差：4.85543892470445e-6 满足条件。
