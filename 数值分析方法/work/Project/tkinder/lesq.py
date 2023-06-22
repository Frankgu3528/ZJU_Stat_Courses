
import matplotlib.pyplot as plt
from pylab import mpl
"""一元线性拟合
采用的拟合数据为xi=1,2,3,4,5,6,7
对应的相应函数值yi=0.5,2.5,2,4,3.5,6,5.5
"""
 
x = [1, 2, 3, 4, 5, 6, 7];
y = [0.5, 2.5, 2, 4, 3.5, 6, 5.5]
 
 
"""完成拟合曲线参数计算"""
def liner_fitting(data_x,data_y):
      size = len(data_x);
      i=0
      sum_xy=0
      sum_y=0
      sum_x=0
      sum_sqare_x=0
      average_x=0;
      average_y=0;
      while i<size:
          sum_xy+=data_x[i]*data_y[i];
          sum_y+=data_y[i]
          sum_x+=data_x[i]
          sum_sqare_x+=data_x[i]*data_x[i]
          i+=1
      average_x=sum_x/size
      average_y=sum_y/size
      return_k=(size*sum_xy-sum_x*sum_y)/(size*sum_sqare_x-sum_x*sum_x)
      return_b=average_y-average_x*return_k
      return [return_k,return_b]
 
 
"""完成完后曲线上相应的函数值的计算"""
def calculate(data_x,k,b):
    datay=[]
    for x in data_x:
        datay.append(k*x+b)
    return datay
 
 
"""完成函数的绘制"""
def draw(data_x,data_y_new,data_y_old):
    plt.plot(data_x,data_y_new,label="拟合曲线",color="black")
    plt.scatter(data_x,data_y_old,label="离散数据")
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    plt.title("一元线性拟合数据")
    plt.legend(loc="upper left")
    plt.show()
 
 
parameter = liner_fitting(x,y)
draw_data = calculate(x,parameter[0],parameter[1])
draw(x,draw_data,y)
