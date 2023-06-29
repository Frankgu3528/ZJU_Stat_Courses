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