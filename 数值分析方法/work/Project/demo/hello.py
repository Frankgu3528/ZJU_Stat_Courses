from tkinter import *
from tkinter import ttk
from tkinter import simpledialog 
from tkinter import messagebox
from tkinter import filedialog
import numpy as np
import os
import math
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# 调用Tk()创建主窗口
window =Tk()
# 给主窗口起一个名字，也就是窗口的名字
window.title('Curve Fitting')

# 菜单
# 绑定一个执行函数，当点击菜单项的时候会显示一个消息对话框
def menuCommand() :
    messagebox.showinfo("说明","本拟合器可以通过手动输入或添加txt文件传入数据\n \n注意:每个数据值直接请用空格隔开!\n txt文件第一行为x值，第二行为y值")
# 创建一个主目录菜单，也被称为顶级菜单
main_menu = Menu (window)
#新增命令菜单项，使用 add_command() 实现
main_menu.add_command (label="说明",command=menuCommand)
#显示菜单
window.config (menu=main_menu)
# 标题
label_name =Label(window, text="Curve Fitting Box",font=('宋体',20, 'bold italic'),bg="#7CCD7C",
                 # 设置标签内容区大小
                 width=30,height=3,
                 # 设置填充区距离、边框宽度和其样式（凹陷式）
                 padx=1, pady=1, borderwidth=1, relief="sunken")
label_name.grid(row=0,rowspan=4)

# 设置窗口大小，让其居中
width = 560
height = 700
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
size_geo = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2)
window.geometry(size_geo)

# 文本框
label_0 =Label(window,text="添加要拟合的数据点",font='10').grid(row=4,sticky="w",padx=5,pady=5)
labe1 = Label(window,text="x值").grid(row=5,sticky="w",padx=5,pady=5)
x_text = Text(window, width=50, height=1, undo=True, autoseparators=False)
x_text.grid(row=5)
labe2 = Label(window,text="y值").grid(row=6,sticky="w",padx=5)
y_text = Text(window, width=50, height=1, undo=True, autoseparators=False)
y_text.grid(row=6)


# 选择文件

def select_file():
    # 单个文件选择
    selected_file_path = filedialog.askopenfilename()  # 使用askopenfilename函数选择单个文件
    select_path.set(selected_file_path) 
select_path = StringVar()

# 布局控件
Label(window, text="文件路径：").grid(row=7)
path = Entry(window, textvariable = select_path)
path.grid(row=7)
Button(window, text="或选择文件导入", command=select_file).grid(row=7,sticky="w",padx=2,pady=2)


# 选择拟合方式
mode = 1
labe3 = Label(window,text="选择拟合方式",font=5)
labe3.grid(row = 8,sticky="w",padx=3)
cbox = ttk.Combobox(window)
cbox.grid(row = 8,sticky="w",padx=200)
# 设置下拉菜单中的值
cbox['value'] = ('拉格朗日内插','三次样条插值(自然)','三次样条插值(夹逼)','多项式拟合','线性拟合')
#通过 current() 设置下拉菜单选项的默认值
cbox.current(0)


# 开始拟合按钮
x_data = []
y_data = []
# Lagrange 插值
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

# 线性拟合
def linear_fitting(data_x,data_y):
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
 
# 多项式拟合

def get_augmented_matrix(matrix, b):
    row, col = np.shape(matrix)
    matrix = np.insert(matrix, col, values=b, axis=1)
    return matrix
# 取出增广矩阵的系数矩阵（第一列到倒数第二列）
def get_matrix(a_matrix):
    return a_matrix[:, :a_matrix.shape[1] - 1]
# 选列主元，在第k行后的矩阵里，找出最大值和其对应的行号和列号
def get_pos_j_max(matrix, k):
    max_v = np.max(matrix[k:, :])
    pos = np.argwhere(matrix == max_v)
    i, _ = pos[0]
    return i, max_v
# 矩阵的第k行后，行交换
def exchange_row(matrix, r1, r2, k):
    matrix[[r1, r2], k:] = matrix[[r2, r1], k:]
    return matrix
# 消元计算(初等变化)
def elimination(matrix, k):
    row, col = np.shape(matrix)
    for i in range(k + 1, row):
        m_ik = matrix[i][k] / matrix[k][k]
        matrix[i] = -m_ik * matrix[k] + matrix[i]
    return matrix
# 回代求解
def backToSolve(a_matrix):
    matrix = a_matrix[:, :a_matrix.shape[1] - 1]  # 得到系数矩阵
    b_matrix = a_matrix[:, -1]  # 得到值矩阵
    row, col = np.shape(matrix)
    x = [None] * col  # 待求解空间X
    # 先计算上三角矩阵对应的最后一个分量
    x[-1] = b_matrix[col - 1] / matrix[col - 1][col - 1]
    # 从倒数第二行开始回代x分量
    for _ in range(col - 1, 0, -1):
        i = _ - 1
        sij = 0
        xidx = len(x) - 1
        for j in range(col - 1, i, -1):
            sij += matrix[i][j] * x[xidx]
            xidx -= 1
        x[xidx] = (b_matrix[i] - sij) / matrix[i][i]
    return x
# 求解非齐次线性方程组：ax=b
def solve_NLQ(a, b):
    a_matrix = get_augmented_matrix(a, b)
    for k in range(len(a_matrix) - 1):
        # 选列主元
        max_i, max_v = get_pos_j_max(get_matrix(a_matrix), k=k)
        # 如果A[ik][k]=0，则矩阵奇异退出
        if a_matrix[max_i][k] == 0:
            print('矩阵A奇异')
            return None, []
        if max_i != k:
            a_matrix = exchange_row(a_matrix, k, max_i, k=k)
        # 消元计算
        a_matrix = elimination(a_matrix, k=k)
    # 回代求解
    X = backToSolve(a_matrix)
    return a_matrix, X
# 数学解法：最小二乘法+求解线性方程组
def last_square_fit_curve_Gauss(xs, ys, order):
    X, Y = [], []
    # 求解偏导数矩阵里，含有xi的系数矩阵X
    for i in range(0, order + 1):
        X_line = []
        for j in range(0, order + 1):
            sum_xi = 0.0
            for xi in xs:
                sum_xi += xi ** (j + i)
            X_line.append(sum_xi)
        X.append(X_line)
    # 求解偏导数矩阵里，含有yi的系数矩阵Y
    for i in range(0, order + 1):
        Y_line = 0.0
        for j in range(0, order + 1):
            sum_xi_yi = 0.0
            for k in range(len(xs)):
                sum_xi_yi += (xs[k] ** i * ys[k])
            Y_line = sum_xi_yi
        Y.append(Y_line)
    a_matrix, A = solve_NLQ(np.array(X), Y)  # 高斯消元：求解XA=Y的A
    return A
# 可视化多项式曲线拟合结果
def draw_fit_curve(xs, ys, A, order):
    fit_xs, fit_ys = np.arange(min(xs) * 0.8, max(xs) * 1.2, 0.01), []
    for i in range(0, len(fit_xs)):
        y = 0.0
        for k in range(0, order + 1):
            y += (A[k] * fit_xs[i] ** k)
        fit_ys.append(y)
    token = 'f(x)='
    for k in range(0,order+1):
        A[k] = "{:.2f}".format(A[k])
        token+="({0})$x^{1}$+".format(A[k],k)
    token = token[:-1]
    window.ax.plot(fit_xs, fit_ys, color='g', linestyle='-', marker='')
    window.ax.plot(xs, ys, color='m', linestyle='', marker='.')
    window.ax.grid()
    window.ax.set_title(token,fontsize = 10)
    

# 三次样条

    # print(x_data.index(x))
    # return y_data[x_data.index(x)]

   
# canvas
def showPlot():
    x_data = []
    y_data = []
    if  (path.get()!=""):
        file1=open(path.get(),'r')
        content1=file1.readlines()               
        t1  = content1[0]
        t2 = content1[1]
        x_data = t1.split()
        x_data = [float(i) for i in x_data]
        y_data = t2.split()
        y_data = [float(i) for i in y_data]
    else:
        x_data.clear()
        y_data.clear()
        window.ax.clear()  # window.fig.clear()
        x_get_import=x_text.get("1.0","end").split()
        y_get_import=y_text.get("1.0","end").split()
        for i in range(len(x_get_import)):
            x_data.append(float(x_get_import[i]))
        for i in range(len(y_get_import)):
            y_data.append(float(y_get_import[i]))
    if (len(x_data)!=len(y_data)):
        messagebox.showerror("错误","请输入匹配的x,y值!")
    if (len(x_data)==0 or len(y_data)==0):
        messagebox.showerror("错误","请输入要拟合的x,y值!")
    xs = np.linspace(min(x_data)-5, max(x_data)+5, 100)
    if (cbox.get()=='拉格朗日内插'): 
        mode = 1
    elif (cbox.get()=='三次样条插值(夹逼)'): 
        mode = 2
    elif (cbox.get()=="三次样条插值(自然)"):
        mode = 6
    elif (cbox.get()=='多项式拟合'):
        order = simpledialog.askstring("输入多项式阶数", "用多少阶的多项式去拟合呢？", initialvalue="3")
        order = int(order)
        mode = 3
    elif (cbox.get()=='线性拟合'):
        mode = 4
    if (mode==1): # 拉格朗日插值
        para = []
        para = ParametersOfLagrangeInterpolation(x_data,y_data,len(x_data))
        y = [CalculateTheValueOfLarangeInterpolation(x_data,para,x) for x in xs]
        window.ax.plot(xs, y, color='red', linewidth=1.0, linestyle='--')
    if (mode==6):
        def f(x):
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


        def cubic_spline_interpolation(x_list, fx_list, left_derivative, right_derivative):   #三次样条插值
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
                window.ax.plot(x, M_list[j] * (x_list[j + 1] - x)**3 / (6 * h_list[j]) + M_list[j + 1] * (x - x_list[j])**3 / (6 * h_list[j]) + (fx_list[j] - M_list[j]
                                                                                                                                        * h_list[j]**2 / 6) * (x_list[j + 1] - x) / h_list[j] + (fx_list[j + 1] - M_list[j + 1] * h_list[j]**2 / 6) * (x - x_list[j]) / h_list[j], label="{0}< x <{1}".format(x_list[j],x_list[j+1]))
            window.ax.legend()
            window.ax.grid()
        cubic_spline_interpolation(x_data,y_data,-1e-6,1e-6)
    if (mode==2): # 三次样条插值
        derive = simpledialog.askstring("夹逼条件", "输入事先指定的左右导数(空格隔开)")
        left,right = map(float,derive.split())
        def f(x):
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


        def cubic_spline_interpolation(x_list, fx_list, left_derivative, right_derivative):   #三次样条插值
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
                window.ax.plot(x, M_list[j] * (x_list[j + 1] - x)**3 / (6 * h_list[j]) + M_list[j + 1] * (x - x_list[j])**3 / (6 * h_list[j]) + (fx_list[j] - M_list[j]
                                                                                                                                        * h_list[j]**2 / 6) * (x_list[j + 1] - x) / h_list[j] + (fx_list[j + 1] - M_list[j + 1] * h_list[j]**2 / 6) * (x - x_list[j]) / h_list[j], label="{0}< x <{1}".format(x_list[j],x_list[j+1]))
            window.ax.legend()
            window.ax.grid()
        cubic_spline_interpolation(x_data,y_data,left,right)

    if (mode==3): # 多项式拟合
        A = last_square_fit_curve_Gauss(xs=x_data, ys=y_data, order=order)
        draw_fit_curve(xs=x_data, ys=y_data, A=A, order=order)  # 可视化多项式曲线拟合结果
    if (mode==4): # 线性拟合
        w,b = linear_fitting(x_data,y_data)
        y = [w*x+b for x in xs]
        window.ax.plot(xs, y, color='red', linewidth=1.0, linestyle='--')
        if b>0:
            window.ax.set_title("$y={:.4f}x+{:.4f}$".format(w,b))
        else:
            b = -b
            window.ax.set_title("$y={:.4f}x+{:.4f}$".format(w,b))
        window.ax.grid()
    window.ax.scatter(x_data,y_data)
    # 5) 子图ax上画完图后，还要cavans.draw()才能刷新显示
    window.canvas.draw()

Button(window, height=2, width=10,text="开始拟合", command=showPlot).grid(row=9, padx=5, pady=5)

window.frmPlot = Frame(window)
# 1) 创建一个matplotlib.pyplot.Figure对象fig
window.fig = plt.Figure(figsize=(5.5, 4), dpi=100)
# 2) 在fig对象上用add_subplot()创建一个子图ax
window.ax = window.fig.add_subplot(111)
# 3) canvas = FigureCanvasTkAgg(fig, master=win)
# 得到一个将fig绑定在win上面的FigureCanvasTkAgg对象canvas
# win可以是窗口，也可以是Frame,LabelFrame
window.canvas = FigureCanvasTkAgg(window.fig, master=window.frmPlot)
# 4) canvas.get_tk_widget().grid(....)将canvas布局到win的合适位置
window.canvas.get_tk_widget().grid(row=13, column=0, sticky="ESNW")
window.frmPlot.grid(row=13, column=0, sticky="ESWN")
#开启主循环，让窗口处于显示状态
window.mainloop()