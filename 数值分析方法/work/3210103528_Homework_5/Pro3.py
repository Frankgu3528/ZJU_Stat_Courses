import math
def a(x):
    return (math.cos(x))**2
def b(x):
    return x*math.log(x+1)
def c(x):
    return (math.sin(x)*math.sin(x)-2*x*math.sin(x)+1)
def d(x):
    return 1/(x*math.log(x))

# 读入积分上下限
x0,x2 = input().split()
x0 = float(x0)
x2 = float(x2)
h = (x2-x0)/2
x1 = (x2+x0)/2

# 为了避免提交太多个py程序，我把几次都写在一个文件里
# 运行哪个就直接取消哪行的注释即可

# print((a(x0)+a(x2))*(x2-x0)/2) # a题 Trapezoidal rule
# print(h/3*(a(x0)+4*a(x1)+a(x2))) # a题 Simpon's Rule

# print((b(x0)+b(x2))*(x2-x0)/2) # b题 Trapezoidal rule
# print(h/3*(b(x0)+4*b(x1)+b(x2))) # b题 Simpon's Rule

# print((c(x0)+c(x2))*(x2-x0)/2) # c题 Trapezoidal rule
# print(h/3*(c(x0)+4*c(x1)+c(x2))) # c题 Simpon's Rule

# print((d(x0)+d(x2))*(x2-x0)/2) # d题 Trapezoidal rule
# print(h/3*(d(x0)+4*d(x1)+d(x2))) # d题 Simpon's Rule
