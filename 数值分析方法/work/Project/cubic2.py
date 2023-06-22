

import numpy as np
from sympy import *
import matplotlib.pyplot as plt

class Spline(object):
    def __init__(self,x,y,k):
        self.x = x
        self.y= y
        self.k = k
        self.n = symbols('n')
    def spline1(self):
    #取-5-5十一个点
        Mat = np.eye(11, 11) * 4
        ds = []
        for i in range(11):
            h = 1
            alaph = 0.5
            if i==0:
                beta = 0
            if 1<=i<10:
                beta = 6*(y[i+1]-2*y[i]+y[i-1])
            if i==10:
                beta = 0
            ds.append(beta)
            if i == 0:
                Mat[i][0] = 2
                Mat[i][1] = 0
            elif i == 10:
                Mat[i][9] = h
                Mat[i][10] = 2
            else:
                Mat[i][i - 1] = h
                Mat[i][i + 1] = alaph
        ds = np.mat(ds)
        Mat = np.mat(Mat)
        Ms = ds * Mat.I
        self.Ms = Ms.tolist()[0]
    #     return Ms.tolist()[0]

    #求三对角方程,核心，自然边界
    def spline(self):
        #取-5-5十一个点
    #     global x,y
        Mat = np.eye(11, 11) * 2
        ds = []
        for i in range(11):
            h = 1
            alaph = 0.5
            if i==0:
                beta = 0
            if 1<=i<10:
                beta = 3*(y[i+1]-y[i-1])/(2*h)
            if i==10:
                beta = 0
            ds.append(beta)
            if i == 0:
                Mat[i][0] = 1
                Mat[i][1] = alaph
            elif i == 10:
                Mat[i][9] = 1 - alaph
            else:
                Mat[i][i - 1] = 1 - alaph
                Mat[i][i]
                Mat[i][i + 1] = alaph
        ds = np.mat(ds)
        Mat = np.mat(Mat)
        Ms = ds * Mat.I
        self.Ms = Ms.tolist()[0]
#         return Ms.tolist()[0]
    #计算每一段的插值函数
    def cal(self,xi, xii, i):
#         Ms = self.spline()
        yi = self.y[i]
        yii = self.y[i+1]
        hi = (1+2*(self.n-xi)/(xii-xi))*((self.n-xii)/(xi-xii))**2
        hii = (1+2*(self.n-xii)/(xi-xii))*((self.n-xi)/(xii-xi))**2
        Hi = (self.n-xi)*((self.n-xii)/(xi-xii))**2
        Hii = (self.n-xii)*((self.n-xi)/(xii-xi))**2
        I = hi*yi+hii*yii+Hi*self.Ms[i]+Hii*self.Ms[i+1]
        return I
    def calnf(self):
        nf = []
        for i in range(len(self.x) - 1):
            nf.append(self.cal(self.x[i], self.x[i + 1], i))
        return nf


    #求值
    # def ff(x):  # f[x0, x1, ..., xk]
    #     ans = 0
    #     for i in range(len(x)):
    #         temp = 1
    #         for j in range(len(x)):
    #             if i != j:
    #                 temp *= (x[i] - x[j])
    #         ans += f(x[i]) / temp
    #     return ans 
    def nfSub(self,x, nf):
        tempx = np.array(range(11)) - 5
        dx = []
        for i in range(10):
            labelx = []
            for j in range(len(x)):
                if x[j] >= tempx[i] and x[j] < tempx[i + 1]:
                    labelx.append(x[j])
                elif i == 9 and x[j] >= tempx[i] and x[j] <= tempx[i + 1]:
                    labelx.append(x[j])
            dx = dx + self.calf(nf[i], labelx)
        return np.array(dx)
    def calf(self,f,x):
        y = []
        for i in x:
            y.append(f.subs(self.n, i))
        return y 
    #画图
    def draw(self,nf):
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        x = np.linspace(-5, 5, 101)
        Ly = self.nfSub(x,nf)
        plt.plot(x, Ly, label='三次样条插值函数')
        plt.scatter(self.x,self.y,label='scatter',color='red')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()

        # plt.savefig('1.png')
        plt.show() 

    def final(self):
        init_printing(use_unicode=True)
        if(self.k==1):
            Ms = self.spline()
        elif(self.k==2):
            Ms = self.spline1()
        self.nf = self.calnf()
        self.draw(self.nf)
        

        
x = np.arange(-5, 5.1, 1)
def func(y):
#     return 1 / (1 + y * y)
#     return np.cos(y)
    return y**2
y = func(x)
print(x)
print(y)
k = np.array([-4,5,7,9,5])
j = np.array([7,5,3,2,5])

a = Spline(k,j,2)
a.final()

