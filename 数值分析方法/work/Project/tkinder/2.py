from tkinter import *
import tkinter . messagebox
#创建主窗口
win = Tk()
win.config(bg='#87CEEB')
win.title("C语言中文网")
win.geometry('450x350+300+200')

# 绑定一个执行函数，当点击菜单项的时候会显示一个消息对话框
def menuCommand() :
    tkinter.messagebox.showinfo("主菜单栏","你正在使用主菜单栏")
# 创建一个主目录菜单，也被称为顶级菜单
main_menu = Menu (win)
#新增命令菜单项，使用 add_command() 实现
main_menu.add_command (label="文件",command=menuCommand)
main_menu.add_command (label="编辑",command=menuCommand)
main_menu.add_command (label="格式",command=menuCommand)
main_menu.add_command (label="查看",command=menuCommand)
main_menu.add_command (label="帮助",command=menuCommand)
#显示菜单
win.config (menu=main_menu)
win.mainloop()