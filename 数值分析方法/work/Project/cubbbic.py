import matplotlib.pyplot as plt
import numpy as np
x_data = [3,5,7,8]
y_data = [5,3,6,8]
def f(x):
    # return 1 / (1 + x**2)
    # y_list=[0,0.79,1.53,2.19,2.71,3.03,3.27,2.89,3.06,3.19,3.29]   #车门曲线绘图
    return y_data[x_data.index(x)]

def first_difference(x_1, x_2):
    return (f(x_1) - f(x_2)) / (x_1 - x_2)

def second_difference(x_1, x_2, x_3):
    return (first_difference(x_1, x_2) - first_difference(x_2, x_3)) / (x_1 - x_3)

def chasing_method(a_list, b_list, c_list, f_list):   #追赶法解方程
    n = len(b_list)
    beta_list = []
    beta_list.append(c_list[0] / b_list[0])
    for i in range(2, n):
        beta_list.append(
            c_list[i - 1] / (b_list[i - 1] - a_list[i - 2] * beta_list[i - 2]))
    y_list = []
    y_list.append(f_list[0] / b_list[0])
    for i in range(2, n + 1):
        y_list.append((f_list[i - 1] - a_list[i - 2] * y_list[i - 2]) /
                      (b_list[i - 1] - a_list[i - 2] * beta_list[i - 2]))
    x_list = []
    x_list.append(y_list[-1])
    for i in range(n - 1, 0, -1):
        x_list.insert(0, (y_list[i - 1] - beta_list[i - 1] * x_list[0]))
    return x_list


def cubic_spline_interpolation(x,x_list, fx_list, left_derivative, right_derivative):   #三次样条插值
    if len(x_list) != len(fx_list):
        print("please check the x_list and f(x)_list!")
        return 1

    length = len(x_list)

    h_list = [x_list[i] - x_list[i - 1] for i in range(1, length)]

    lambda_list = [h_list[j] / (h_list[j - 1] + h_list[j])
                   for j in range(1, length - 1)]

    mu_list = [h_list[j - 1] / (h_list[j - 1] + h_list[j])
               for j in range(1, length - 1)]

    d_list = [6 * second_difference(x_list[j - 1], x_list[j], x_list[j + 1])
              for j in range(1, length - 1)]

    b_list = [2 for i in range(length)]

    lambda_list.insert(0, 1)
    d_list.insert(0,
                  (6 / h_list[0]) * (first_difference(x_list[0], x_list[1]) - left_derivative))
    d_list.append((6 / h_list[-1]) * (right_derivative -
                                      first_difference(x_list[-2], x_list[-1])))
    mu_list.append(1)

    M_list = chasing_method(mu_list, b_list, lambda_list, d_list)

    
    for j in range(0, length - 1):
        x = np.linspace(x_list[j], x_list[j + 1], 10)
        y = M_list[j] * (x_list[j + 1] - x)**3 / (6 * h_list[j]) + M_list[j + 1] * (x - x_list[j])**3 / (6 * h_list[j]) + (fx_list[j] - M_list[j]
                                                                                                                              * h_list[j]**2 / 6) * (x_list[j + 1] - x) / h_list[j] + (fx_list[j + 1] - M_list[j + 1] * h_list[j]**2 / 6) * (x - x_list[j]) / h_list[j]
        plt.plot(x, M_list[j] * (x_list[j + 1] - x)**3 / (6 * h_list[j]) + M_list[j + 1] * (x - x_list[j])**3 / (6 * h_list[j]) + (fx_list[j] - M_list[j]
                                                                                                                                * h_list[j]**2 / 6) * (x_list[j + 1] - x) / h_list[j] + (fx_list[j + 1] - M_list[j + 1] * h_list[j]**2 / 6) * (x - x_list[j]) / h_list[j], label="{0}< x <{1}".format(x_list[j],x_list[j+1]))
    plt.show()
            
    


def main():
    
    # x_list = [-5 + i for i in range(11)]
    # fx_list = [f(x) for x in x_list]
    left_derivative = 10 / 26**2
    right_derivative = -10 / 26**2
    #三次样条插值绘图
    cubic_spline_interpolation(1,x_data,y_data, left_derivative, right_derivative)


if __name__ == '__main__':
    main()
