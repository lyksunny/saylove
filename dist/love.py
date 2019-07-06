from tkinter import *
from tkinter import messagebox

#点击关闭弹出消息
def closeWindow():
    messagebox.showinfo(title = "警告", message = "不许关闭，好好回答")

def closeall():
    window.destroy()

def closelove():
    messagebox.showinfo(title = "不再考虑一下吗", message = "再考虑一下吧")

def Love():
    #是一个顶级窗口
    love = Toplevel(window)
    love.geometry("300x100+630+260")
    love.title("好巧，我也是")
    label = Label(love, text = "好巧，我也是", font = ("微软雅黑", 25))
    label.pack()     #包
    btn = Button(love, text = "确定", width = 10, height = 2, command = closeall)
    btn.pack()
    love.protocol("WM_DELETE_WINDOW", closelove)

def nolove():
    no_love = Toplevel(window)
    no_love.geometry("300x100+630+260")
    no_love.title("再考虑考虑呗")
    label = Label(no_love, text="再考虑考虑呗", font=("微软雅黑", 25))
    label.pack()
    btn = Button(no_love, text = "好的", width = 10, height = 2, command = no_love.destroy)
    btn.pack()
    no_love.protocol("WM_DELETE_WINDOW", closenolove)

def closenolove():
    nolove()

window = Tk()                    #创建窗口
window.title("你喜欢我吗？")      #设置窗口标题
window.geometry("380x420")       #窗口大小
window.geometry("+450+180")      #窗口位置
window.protocol("WM_DELETE_WINDOW",closeWindow)

#标签控件
label1 = Label(window, text="hey,小姐姐", font = ("微软雅黑", 15), fg ='red')
label1.grid()                    #定位
label2 = Label(window, text="喜欢我吗", font = ("微软雅黑", 30))
label2.grid(row = 1, column = 1, sticky = E)    #sticky定位方法：N E W S 东西南北

#显示图片
photo = PhotoImage(file = '../Im/cc.png')
imagelabel = Label(window, image = photo)
imagelabel.grid(row = 2, columnspan = 2) #columnspan组件跨越的列数

#按钮
btn1 = Button(window, text = "喜欢", width = 15, height = 2,command = Love)
btn1.grid(row = 3, column = 1, sticky = W)

btn2 = Button(window, text = "不喜欢", command = nolove)
btn2.grid(row = 3, column = 1, sticky = E)

window.mainloop()                #显示窗口
