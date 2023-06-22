import numpy as np
import matplotlib.pyplot as plt
import math
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


class Ployfit:
    def __init__(self, x_data, y_data, n, label_list=None):
        if label_list is None:
            label_list = ['x', 'y']
        self.x = x_data
        self.y = y_data
        self.n = n  # 多项式阶数
        self.x_label = label_list[0]  # 自变量名称
        self.y_label = label_list[1]  # 因变量名称
        self.m = len(self.x)  # 样本量
        self.w = np.zeros((self.n, 1))
        self.y_hat = np.zeros((self.m, 1))
        self.sst = 0.0
        self.sse = 0.0
        self.ssr = 0.0
        self.r2 = 0.0

    def n_ploy_fit_formula(self):
        """
        n次多项式拟合,公式法
        :return:
        """
        _x = self.x.reshape(self.m, 1)
        _y = self.y.reshape(self.m, 1)
        X = _x ** self.n
        for i in range(self.n - 1):
            X = np.hstack((X, _x ** (self.n - i - 1)))
        X = np.hstack((X, np.ones((self.m, 1))))
        self.w = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(_y)
        self.y_hat = X.dot(self.w)
        plt.plot(self.x, self.y, '+', label='original data')
        plt.plot(self.x, self.y_hat, 'r-', lw=2, label='Polynomial Curve Fitting')

        plt.show()
    def plot_PF(self):
        _w = []
        for i in range(len(self.w)):
            _w.append(round(float(self.w[i]), 5))
        title = 'y = '
        w = list(map(str, _w))
        for i in range(len(w)):
            if i != 0 and float(w[i]) > 0:
                w[i] = '+' + w[i]
        for i in range(len(w) - 2):
            title = title + w[i] + '$x^{}$'.format(len(w) - i - 1)
        title = title + w[-2] + '$x$'
        title = title + w[-1]
        plt.figure(figsize=(8, 6))
        plt.plot(self.x, self.y, '+', label='original data')
        plt.plot(self.x, self.y_hat, 'r-', lw=2, label='Polynomial Curve Fitting')
        # plt.xlabel('${}$'.format(self.x_label), fontdict={'fontsize': 13})
        # plt.ylabel('${}$'.format(self.y_label), fontdict={'fontsize': 13})
        # plt.legend(fontsize=12)
        # plt.grid(alpha=0.5)
        # plt.title(title ,
        #           fontdict={'fontsize': 14})
        plt.show()


if __name__ == '__main__':
    np.random.seed(100)
    x = np.linspace(-10, 10, 40).reshape(40, 1)
    y = [math.sin(i) for i in x]
    y = np.array(y) 
    PF = Ployfit(x, y, 20)
    PF.n_ploy_fit_formula()
    