## 随机模拟正态总体下样本峰度的抽样分布

> 顾格非 3210103528

### 模拟步骤

1. 产生 $n$ 个$N(0,1)$的随记数。（本实验中依次进行了n=10,15,20,25的实验）

2. 计算此样本的样本峰度值$b_k$。
3. 重复上两步 $N$ 次。(本实验中取了$N=10000$)
4.  将 $b_k$ 中的值排序后，计算经验分布函数并画图。

### 使用的软件：

Python编写，具体的代码见附录及文件夹中的`kurtoris.py`。

需要的第三方包：

```
matplotlib==3.5.1
numpy==1.21.4
```

### 模拟结果

每次模拟的随机数数量设置了`10,15,20,25`，每次模拟`10000`次，得到样本峰度的经验分布函数的图像：

<img src="C:\Users\阿漆\Desktop\大二下\数理统计\Figure_1.png" alt="Figure_1" style="zoom:72%;" />

## 附录

```python
import numpy as np
import matplotlib.pyplot as plt

# 计算峰度的函数
def Kurtosis(a):
    a = a-np.mean(a)
    up = 0;down = 0;
    for i in a:
        up+=i**4
        down+=i**2
    up = up/len(a)
    down = pow(down/len(a),2)
    return up/down-3

N = 10000 # 重复次数
n = [10,15,20,25] # 随机数个数
X_n = []
for k in n:
    result = []
    for i in range(N):
        a = np.random.normal(0,1,k)
        result.append(Kurtosis(a))
    X = sorted(result)
    Y = [i/N for i in range(N)]
    X_n.append(X)

# 画图
fig, ax = plt.subplots()
ax.plot(X_n[0], Y, label='n = 10')
ax.plot(X_n[1], Y, label='n = 15')
ax.plot(X_n[2], Y, label='n = 20')
ax.plot(X_n[3], Y, label='n = 25')
plt.title("Empirical CDF for Kurtotis with N={}".format(N))
plt.ylim(0,1)
plt.xlim(-2.5,6)
plt.xticks(np.arange(-2,6,1))
plt.yticks(np.linspace(0,1,11))
plt.xlabel("X")
plt.ylabel("F(x)")
plt.grid(linestyle='-.')
ax.legend(loc="lower right",prop={'size': 12})
plt.show()
```

