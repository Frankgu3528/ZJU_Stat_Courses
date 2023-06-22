import matplotlib.pyplot as plt
from pylab import mpl
# """
# 用拉格朗日插值法拟合数据。
# """
 
# """
# 功能：计算插值多项式的系数。
# 参数：data_x为数据的x坐标，data_y为数据的y坐标，size为插值基函数的个数。
# 返回值：插值函数的系数。
# """
x = [100, 121, 144]
y = [10,11, 12]
 
def ParametersOfLagrangeInterpolation(data_x,data_y,size):
    parameters=[]
    #i用来控制参数的个数
    i=0;
    while i < size:
        #j用来控制循环的变量做累乘
        j = 0;
        temp = 1;
        while j < size:
            if(i != j):
                temp*=data_x[i]-data_x[j]
            j+=1;
        parameters.append(data_y[i]/temp)
        i += 1;
    return parameters
 
# """
# 功能：计算拉格朗日插值法公式的值。
# 参数：data_x为原始数据的横坐标，x为要用拉格朗日插值函数计算数据，parameters为拉格朗日插值函数的系数。
# 返回值：经拉格朗日插值公式计算后的值。
# """
 
def CalculateTheValueOfLarangeInterpolation(data_x,parameters,x):
    returnValue=0
    i = 0;
    while i < len(parameters):
        temp = 1
        j = 0;
        while j< len(parameters):
            if(i!=j):
                temp *=x-data_x[j]
            j+=1
        returnValue += temp * parameters[i]
        i += 1
    return returnValue

 
# """
# 功能：将函数绘制成图像
# 参数：data_x,data_y为离散的点.new_data_x,new_data_y为由拉格朗日插值函数计算的值。x为函数的预测值。
# 返回值：空
# """
def  Draw(data_x,data_y,new_data_x,new_data_y):
        plt.plot(new_data_x, new_data_y, label="拟合曲线", color="black")
        plt.scatter(data_x,data_y, label="离散数据",color="red")
        plt.scatter(115, 10.723805294764, label="真实数据", color="green")
        mpl.rcParams['font.sans-serif'] = ['SimHei']
        mpl.rcParams['axes.unicode_minus'] = False
        plt.title("拉格朗日插值拟合数据")
        plt.legend(loc="upper left")
        plt.show()
 
# """
# 由于三个点绘制的拟合曲线效果太差，所以采用这样的方法来进行数据拟合。
# 1>利用原数据计算出拉格朗日插值多项式的函数，分别在10-150区间内，每10个数取一个点，计算相应的值，绘制函数图像。
# 2>将源数据以点的形式画在图像上，
# 3>将115代入拉格朗日函数计算出相应的值，绘制在图像上。点为红色。并将真实的值也绘制在图像上点为绿色。看红色的点和绿色的点是否重合。
# 4>结果证明红色的点和绿色的点重合，说明拉格朗日函数插值效果较好。
# """
parameters=ParametersOfLagrangeInterpolation(x,y,3)
datax=[10,20,30,40,50,60,70,80,90,100,110,120,130,140,150]
datay=[]
for temp in datax:
    datay.append(CalculateTheValueOfLarangeInterpolation(x,parameters,temp))
x.append(115)
y.append(CalculateTheValueOfLarangeInterpolation(x,parameters,115))
Draw(x,y,datax,datay)