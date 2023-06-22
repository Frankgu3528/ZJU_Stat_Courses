from tkinter import *
from tkinter import ttk
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

# 设置窗口大小，让其居中
width = 700
height = 700
# screenwidth = window.winfo_screenwidth()
# screenheight = window.winfo_screenheight()
# size_geo = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2)
# window.geometry(size_geo)



# 开始拟合按钮
x_data = []
y_data = []
x_text = Text(window, width=50, height=1)
x_text.grid(row=1)
x_text.insert(INSERT, 'C语言中文网')
# def getTextInput():
#     x_get_import=x_text.get("1.0","end")
#     for i in range(len(x_get_import)):
#         x_data.append(float(x_get_import[i]))
# btnRead=Button(window, height=2, width=10, text="开始拟合",
#                     command=getTextInput)
# btnRead.grid(row = 8,column=1)
# def output():
#     print(x_data)
# btnRead=Button(window, height=2, width=10, text="xianshi",
#                     command=output)
# btnRead.grid(row = 9,column=1)

#开启主循环，让窗口处于显示状态
window.mainloop()