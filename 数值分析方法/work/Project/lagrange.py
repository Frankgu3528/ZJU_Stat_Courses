import numpy as np

x_data = np.array([2,5])
y_data = np.array([4,1])
n = x_data.size
# """
# 用拉格朗日插值法拟合数据。
# """
 
# """
# 功能：计算插值多项式的系数。
# 参数：data_x为数据的x坐标，data_y为数据的y坐标，size为插值基函数的个数。
# 返回值：插值函数的系数。
# """
 
def ParametersOfLagrangeInterpolation(data_x,data_y,size):
    parameters=[]
    #i用来控制参数的个数
    i=0
    while i < size:
        #j用来控制循环的变量做累乘
        j = 0
        temp = 1
        while j < size:
            if(i != j):
                temp*=data_x[i]-data_x[j]
            j+=1
        parameters.append(data_y[i]/temp)
        i += 1
    return parameters
 
# """
# 功能：计算拉格朗日插值法公式的值。
# 参数：data_x为原始数据的横坐标，x为要用拉格朗日插值函数计算数据，parameters为拉格朗日插值函数的系数。
# 返回值：经拉格朗日插值公式计算后的值。
# """
 
def CalculateTheValueOfLarangeInterpolation(data_x,parameters,x):
    returnValue=0
    i = 0
    while i < len(parameters):
        temp = 1
        j = 0
        while j< len(parameters):
            if(i!=j):
                temp *=x-data_x[j]
            j+=1
        returnValue += temp * parameters[i]
        i += 1
    return returnValue

para = []
para = ParametersOfLagrangeInterpolation(x_data,y_data,2)

print(para)
a = CalculateTheValueOfLarangeInterpolation(x_data,para,1)
print(a)