## Problem1

> 代码见`pro1.cpp`

```
1: -0.880333
2: -0.865684
3: -0.865474
4: -0.865474
final root: -0.865474
```

不能取$p_0=0$，因为$f'(x)=-3x^2-sin(x),f'(0)=0$，代入迭代公式中分母为0，不可取。

## Problem2

1. 由**Newton-Raphson方法**，有：

$$
x_{k+1}=x_k-\frac{f(x_k)}{f'(x_k)}=x_k-\frac{b-\frac{1}{x_k}}{\frac{1}{x_k^2}}=2x_k-bx_k^2\\
于是|\epsilon_{k+1}|=|\frac{\frac{1}{b}-x_{k+1}}{\frac{1}{b}}|=|\frac{(\frac{1}{b}-x_k)^2}{\frac{1}{b^2}}|=\epsilon_k^2
$$

2. 当$0<x_0<\frac{2}{b}$时，有$|\epsilon_0|<1$,而：
   $$
   \epsilon_0=(\epsilon_1)^\frac{1}{2}=(\epsilon_2)^\frac{1}{2^2}=…=(\epsilon_k
   )^\frac{1}{2^k}\\
   {\lim_{k \to +\infty}}\epsilon_k = {\lim_{k \to +\infty}}(\epsilon_0)^\frac{1}{2^k}=0\\
   故最后会收敛到\frac{1}{b}
   $$

## Problem3

### A.

$$
J(x_1,x_2,x_3)=
\left(
\begin{matrix}
3&x_3sin(x_2x_3)&x_2sin(x_2x_3)\\
8x_1&-1250x_2+2&0\\
-x_2e^{-x_1x_2}&-x_1e^{-x_1x_2}&20
\end{matrix}
\right)\\
x^{(0)}=0 \Rightarrow
J(x^{(0)})=
\left(
\begin{matrix}
3&0&0\\
0&2&0\\
0&0&20
\end{matrix}
\right)\\
解 \quad J^{x(0)}y^{(0)}=-F(x^{(0)})\\
得到 \quad y^{(0)}=(\frac{1}{2},\frac{1}{2},\frac{-1\pi}{6})^t\\
则 \quad x^{(1)}=x^{(0)}+y^{(0)}=(\frac{1}{2},\frac{1}{2},\frac{-1\pi}{6})^t\\
同样解 \quad J^{x(1)}y^{(1)}=-F(x^{(1)})\\
x^{(2)}= y^{(1)}+x^{(1)}\\
最终得到 \quad x^{(2)}=(0.50016669,0.25080364,-0.51738743)
$$

### B.

$$
J(x_1,x_2,x_3)=
\left(
\begin{matrix}
2x_1&1&0\\
1&2x_2&0\\
1&1&1\\
\end{matrix}
\right)\\
x^{(0)}=0 \Rightarrow
J(x^{(0)}) = 
\left(
\begin{matrix}
0&1&0\\
1&0&0\\
1&1&1\\
\end{matrix}
\right)\\
J^{x(0)}y^{(0)}=-F(x^{(0)}) \Rightarrow y^{(0)} = (5,37,-39)^t\\
x^{(1)} = x^{(0)}+y^{(0)}\Rightarrow x^{(1)} = (5,37,-39)^t\\
同样解 \quad J^{x(1)}y^{(1)}=-F(x^{(1)})\\
x^{(2)}= y^{(1)}+x^{(1)}\\
最终得到 \quad x^{(2)} = (4.35087719,18.49122807,-19.84210526)
$$

## Problem4

>  这俩题的程序见压缩包里的Python文件~

代码的思路主要参考课本P658,659的伪代码，其中矩阵的运算采用Python中常用的模块`numpy`操作。$\nabla g(x_1,x_2,x_3)$的计算较为繁琐，展开再合并后可以用$2J'(x)F(x)$来计算，能较为简便的得到结果。最后通过$x^{(k+1)}=x^k-\alpha \nabla g(x_1,x_2,x_3)$不断迭代得到结果。

### (a)


$$
f_1(x_1,x_2,x_3)=15x_1+x_2^2-4x_3-13\\
f_2(x_1,x_2,x_3)=x_1^2+10x_2-x_3-11\\
f_3(x_1,x_2,x_3)=x_2^3-25x_3+22\\
g(x_1,x_2,x_3)=\sum_{i=1}^{n}f_i^2(x_1,x_2,x_3)\\
J(x_1,x_2,x_3)= \left(
\begin{matrix}
15&2x_2&-4\\
2x_1&10&-1\\
0&3x_2^2&-25
\end{matrix}
\right)\\
\\
\nabla g(x_1,x_2,x_3) = 2J'(x_1,x_2,x_3)
\left(
\begin{array}
df_1(x_1,x_2,x_3)\\
f_2(x_1,x_2,x_3)\\
f_3(x_1,x_2,x_3)\\
\end{array}
\right)\\
x^{(k+1)}=x^k-\alpha \nabla g(x_1,x_2,x_3)
$$
以上是数学部分

**结果展示**

```
x1 =  1.043465654410717
x2 =  1.063646526417548
x3 =  0.9256954364554192
```

### (b)

$$
f_1(x_1,x_2,x_3)=10x_1-2x_2^2+x_2-2x_3-5\\
f_2(x_1,x_2,x_3)=8x_2^2+x_3^2-9\\
f_3(x_1,x_2,x_3)=8x_2x_3+4\\
$$

**结果展示**

```
x1 =  0.8996604615655656
x2 =  -0.9791330381049683
x3 =  0.5364333126942094
```



## Problem5

### (a)

<img src="C:\Users\阿漆\AppData\Roaming\Typora\typora-user-images\image-20221016162026117.png" alt="image-20221016162026117" style="zoom:33%;" />
$$
J(x_1,x_2)=\left(
\begin{matrix}
\frac{x_1}{5}&\frac{x_2}{5}\\
\frac{1+x_2^2}{10}&\frac{x_1x_2}{5}
\end{matrix}
\right)\\ 
取K=0.95，则：\\
当x_i \in D时，|\frac{\partial g_i(x)}{\partial x_j}|\leq|\frac{\partial g_2(x)}{\partial x_2}|=|\frac{x_1x_2}{5}|\leq \frac{9}{20}<\frac{0.95}{2}\\
由上述定理，在D上不动点唯一。
$$


### (b)

直接代入计算：
$$
x^{(0)}=[0,1]^t \\
x^{(1)}=[\frac{9}{10},\frac{8}{10}]^t \\
x^{(2)}=[1.045,0.9046]^t \\
$$
