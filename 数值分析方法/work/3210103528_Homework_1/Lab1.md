# 第一次作业

> 本文采用Markdown编写，数学公式均是用Latex手敲而成，代码文件采用`c++`编写，均与本文件一起放在压缩包里。

## Problem1

1. 不妨有$f(x_1)\leq f(x_2)$,构造$g(x)=f(x)-\frac{f(x_1)+f(x_2)}{2}$, 则有，$g(x)$是$[x_1,x_2]$上的连续函数，且$f(x_1) \leq 0,f(x_2)\geq0$,由零点存在定理，必存在$\zeta\in[x_1,x_2]$，满足$f(\zeta)=0,即f(\zeta)=\frac{f(x_1)+f(x_2)}{2}$, 证毕。
2. 不妨有$f(x_1)\leq f(x_2)$,构造$g(x)=f(x)-\frac{c_1f(x_1)+c_2f(x_2)}{c_1+c_2}$, 则有，$g(x)$是$[x_1,x_2]$上的连续函数，且$f(x_1) \leq 0,f(x_2)\geq0$,由零点存在定理，必存在$\zeta\in[x_1,x_2]$，满足$f(\zeta)=0,即\frac{c_1f(x_1)+c_2f(x_2)}{c_1+c_2}$, 证毕。
3. 给出一个例子：$f(x)=x,x_1=-2,x_2=1,c_1=-2,c_2=1,则\frac{c_1f(x_1)+c_2f(x_2)}{c_1+c_2}=\frac{-2f(-2)+1f1)}{-1}=-5$,$而f(x)\in[-2,1]$,显然找不出这样的$ \zeta$。

## Problem2
a. 
1. $|f(x_0)-\tilde{f}(x_0)|=f'(\zeta)(x_0+\epsilon-x_0)=f'(\zeta)\epsilon \quad (\zeta \in[x_0,x_0+\epsilon])$
2. $\frac{|f(x_0)-\tilde{f}(x_0)|}{f(x_0)}=f'(\zeta)(x_0+\epsilon-x_0)/f(x_0)=\frac{f'(\zeta)\epsilon}{f(x_0)}\quad (\zeta \in[x_0,x_0+\epsilon])$

b. 
1. **absolute** = $f'(\zeta)\epsilon\in[5\times10^{-6}e,5\times10^{-6}e^{1+5\times10^{-6}}]$   	

   **ralative** = $\frac{f'(\zeta)\epsilon}{f(x_0)}=\in[5\times10^{-6},5\times10^{-6}e^{5\times10^{-6}}]$

2. **absolute** = $f'(\zeta)\epsilon\in[5\times10^{-6}cos(1+5\times10^{-6}),5\times10^{-6}cos(1)]$   

   **ralative** = $\frac{f'(x_0)\epsilon}{f(x_0)}\in[5\times10^{-6}\frac{cos(1+5\times10^{-6})}{sin(1)},5\times10^{-6}\frac{cos(1)}{sin(1)}]$

## Problem 3

**a.** 

1. exact：  $\frac{17}{15}$

2. chopping: 1.13

3. rounding: 1.13

4. ralative errors: $2.94*10^{-3}$

**b.**

1. exact: $\frac{301}{660}$

2. chopping: 0.333+0.272-0.150=0.455

3. rounding: 0.333+0.273-0.150=0.456

4. relative errors: chopping: $2.33\times10^{-3}$	rounding: $1.33\times10^{-4}$ 

## Problem 4

A.
$$
由于\gamma = min(\alpha,\beta),x趋向于0\\
有：O(x^\alpha)+O(x^\beta)=O(x^\gamma)\\
|F(x)-c_1L_1-c_2L_2|=|c_1(L_1+O(x^\alpha))+c_2(L_2+O(x^\beta))-c_1L_1-c_2L_2|\\=|c_1O(x^\alpha)+c_2O(x^\beta)|=O(x^\alpha)+O(x^\beta)=O(x^\gamma)\\
于是有：F(x)=c_1L_1+c_2L_2+O(x^\gamma)
$$


B.
$$
G(x)=F_1(c_1x)+F_2(c_2x)\\G(x)=L_1+L_2+O(c_1^\alpha x^\alpha)+O(c_2^\beta x^\beta)\\由于:O(c_1^\alpha x^\alpha)=c_1^\alpha O(x^\alpha)=O(x^\alpha)\\得到:G(x)=L_1+L_2+O(x^\alpha)+O(x^\beta)\\=L_1+L_2+O(x^\gamma)
$$



## Problem 5

(相关程序见文件夹中的`cpp`文件)

**a:**

```
i=0 0.5
i=1 0.25
i=2 0.375
i=3 0.3125
i=4 0.28125
i=5 0.265625
i=6 0.257812
i=7 0.253906
i=8 0.255859
i=9 0.256836
i=10 0.257324
i=11 0.257568
i=12 0.257446
i=13 0.257507
i=14 0.257538
i=15 0.257523
i=16 0.25753
```

**b:**

在0.2-0.3之间寻根

```
i=0 0.25
i=1 0.275
i=2 0.2875
i=3 0.29375
i=4 0.296875
i=5 0.298438
i=6 0.297656
i=7 0.297266
i=8 0.297461
i=9 0.297559
i=10 0.29751
i=11 0.297534
i=12 0.297522
i=13 0.297528
```
在1.2-1.3之间寻根
```
i=0 1.25
i=1 1.275
i=2 1.2625
i=3 1.25625
i=4 1.25937
i=5 1.25781
i=6 1.25703
i=7 1.25664
i=8 1.25645
i=9 1.25654
i=10 1.25659
i=11 1.25662
i=12 1.25663
i=13 1.25662
```

## Problem 6

(相关程序见文件夹中的`cpp`文件)

**a.** $2sin\pi x+x = 0 \Rightarrow x = \sqrt{2sin\pi x+x+x^2}$ （将此作为迭代方程）

```
p1 = 1.41421
p2 = 1.21918
p3 = 1.19779
p4 = 1.21169
p5 = 1.20237
```

**b.**$3x^2-e^x=0 \Rightarrow x =\pm \sqrt{\frac{e^x}{3}}$

分别让$p_0=-1和1$，得到以下结果。

```
p1 = 0.95189
p2 = 0.929265
p3 = 0.918812
p4 = 0.914022
```

```
p1 = -0.350181
p2 = -0.484617
p3 = -0.453113
p4 = -0.460307
```

## Problem 7

$$
由中值定理：|P_n-P|=|g(p_{n-1})-g(p)|=g'(\xi)|p_{n-1}-p|\\
由于g'(\xi)>1,|p_n-p|>|p_{n-1}-p|...>|p_0-p|\\
因此无法找到p_0使得不动点迭代收敛
$$

