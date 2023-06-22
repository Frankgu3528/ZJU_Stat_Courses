from tkinter.simpledialog import *
from tkinter.filedialog import *
import tkinter
 
windows = tkinter.Tk()
# windows.maxsize(800,800)
windows.minsize(300, 300)
# windows.resizable(False,False)
# 窗口初始大小
# windows.geometry("1300x1300")
windows.title("place")
 
 
def openfile():
    import os
    tkinter.filedialog.askopenfilename(title="打开文件", initialdir=r"C:\Users\Administrator\Desktop\infinite",
                                       filetypes=(("jpg格式", "*.jpg"), ("全部", "*.*")))
 
 
def string1():
    askstring("请输入字符串", "输入字符串", initialvalue="是")
    # askfloat("请输入浮点","22.22")
    # a= askinteger("请输入整数","整数：1")
    # print(a)
    # 打开文件对话框
    #
 
 
button1 = tkinter.Button(text="按钮", command=string1)
button2 = tkinter.Button(text="打开文件", command=openfile)
button2.place(x=40, y=60)
 
menubar = tkinter.Menu(windows)
# 创建一个下拉菜单，并且加入文件菜单
filemenu = tkinter.Menu(menubar)
# 创建下来菜单的选项
filemenu.add_command(label="打开", command=openfile)
filemenu.add_command(label="保存")
# 创建下拉菜单的分割线
filemenu.add_separator()
filemenu.add_command(label="退出", )
# 将文件菜单作为下拉菜单添加到总菜单中，并且将命名为File
menubar.add_cascade(label="文件", menu=filemenu)
# 显示总菜单
windows.config(menu=menubar)
 
button1.place(x=10, y=30)
 
windows.mainloop()