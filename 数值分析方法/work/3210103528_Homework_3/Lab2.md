## Problem1

### (a)

$$
||x-\tilde{x}||_{\infty}=0.5\\
A\tilde{x}=(1,-1.3,1.8)^t\\
||A\tilde{x}-b||_∞=0.3
$$

### (b)

$$
||x-\tilde{x}||_{\infty}=0.9\\
A\tilde{x}-b=(1.27,-1.16,2.21)^t\\
||A\tilde{x}-b||_∞=0.27
$$

## Problem2

先有引理一：(来自课本的定理)
$$
A是n\times n矩阵，则||A||_2=[\rho(A^TA)]^{\frac{1}{2}}
$$
![image-20221019135640502](C:\Users\阿漆\AppData\Roaming\Typora\typora-user-images\image-20221019135640502.png)

先证明引理二：
$$
A是n\times n矩阵，则\rho(A^2)=[\rho(A)]^2
$$
证明：
$$
设\lambda是A的特征值，则Ax=\lambda x \Rightarrow A^2x=\lambda Ax=\lambda^2 x\\
则\lambda^2是A^2的特征值。\\
那么\rho(A^2)=max(\lambda^2)=[max(\lambda)]^2=[\rho(A)]^2\\
Q.E.D.
$$
因为$A$是对称矩阵，故$A=A^T$, 由引理: 
$$
||A||_2=[\rho(A^TA)]^{\frac{1}{2}}=[\rho(A^2)]^{\frac{1}{2}}=\rho(A)\\
Q.E.D.
$$
**综上，结论证毕**

## Problem3

> 代码见`Pro1.cpp`

### (a)

```
输入：
2
0.03 58.9 59.2
5.31 -6.10 47.0
输出：
10 1
```
### (b)

```
输入：
3
3.03 -12.1 14 -119
-3.03 12.1 -7 120
6.11 -14.2 21 -139
输出：
0 10 0.142857 
```

## Problem4

> 代码见文件夹里的两个Python文件

思路：通过$x^{k}=D^{-1}(L+U)x^{(k-1)}+D^{-1}b$ 迭代。

### (a)

```
[ 1.25       -1.33333333  0.2       ]
[ 1.63333333 -0.98333333  0.23333333]
[ 1.55416667 -0.86666667 -0.06      ]
final:  [ 1.44776124 -0.83582088 -0.04477614]
```

### (b)

```
[-2.  2.  0.]
[-1.  1. -1.]
[-1.75  1.75 -0.5 ]
final:  [-1.45408793  1.45408793 -0.72760766]
```

## Problem5

> 代码见文件夹里的Python文件.

本题分别用两种迭代方法进行寻根，并采用$|x_k-x_{k+1}|_{\infty}<TOL$作为循环的终止的条件。

从结果来看，果然Guass-Seidel比Jacobi快一点诶。

### (a)

**Jacobi Method** : 

```
After 7 iterations,we get the final root:
[ 0.03502399 -0.23732106  0.65737656]
```

**Guass-Seidel Method :**

```
After 5 iterations,we get the final root: 
[ 0.03535107 -0.23678863  0.65775895]
```

### (b)

**Jacobi Method** :

```
After 5 iterations,we get the final root: 
[0.995725 0.957775 0.79145 ]
```

**Guass-Seidel Method :**

```
After 3 iterations,we get the final root: 
[0.9957475  0.95787375 0.79157475]
```



## Problem6

$$
假设有c_1x_1+c_2x_2+…+c_kx_k=0\\
左乘A, 由Ax_i=\rho_ix_i,有：\\
c_1\rho_1x_1+c_2\rho_2x_2+…+c_k\rho_kx_k=0\\
将(1)*\rho_k-(2):\\
c_1(\rho_k-\rho_1)x_1+c_2(\rho_k-\rho_2)x_2+…+c_k(\rho_k-\rho_{k-1})x_{k-1}=0\\
将c_i(\rho_k-\rho_i)记为d_k,则：\\
d_1x_1+d_2x_2+…+d_{k-1}x_{k-1}=0\\
如此操作下去，有：\\
m_1x_1=0 \quad m_1 = 0\\
在代回，可以得到m_1=m_2=…=m_k=0\\
进一步，有c_1 = c_2 = … = c_k = 0 ，即x_1,x_2,…,x_k线性无关。\\
Q.E.D.
$$

## Problem7

> 证明**strictly diagonally dominant matrix**（简记为SDD）阵可逆

回顾SDD阵的定义：$|a_{kk}|> |\sum_{j\neq k}a_{kj}|，k=1，2，…，n$

设$A$为SDD阵，假设A不可逆，即$|A|=0$。那么$AX=0$有非零解，记为$x_1,x_2,…,x_n$。令$|x_k|=max\{|x_i|\}$。

因为$AX=0$，则有
$$
\sum_{j=1}^{n}a_{kj}x_j=0 \Rightarrow \sum_{j\neq k}a_{kj}x_j=-a_{kk}x_k\\
即|\sum_{j\neq k}a_{kj}x_j|=|a_{kk}||x_k|\\
$$

而由SDD阵的定义:
$$
|a_{kk}||x_k|> |\sum_{j\neq k}a_{kj}||x_k|>|\sum_{j\neq k}a_{kj}||x_j|\geq|\sum_{j\neq k}a_{kj}x_j|\\
即|a_{kk}||x_k|>|a_{kk}||x_k|,矛盾。
$$
**故strictly diagonally dominant matrix阵可逆。**
