import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog 
import os
import shutil 
import time

window = tk.Tk()
window.title('句级别翻译质量评估')#窗口标题
window.geometry('1200x1000')#窗口长度

l_1 = tk.Label(window, text = '句级别翻译质量评估',  
             font = ("Microsoft YaHei", 18))

l_1.place(x = 480, y = 20)

l_2 = tk.Label(window, text = '1、语料处理',  
             font = ("Microsoft YaHei", 14))

l_2.place(x = 50, y = 60)

filename_1 = ''
lb1 = tk.Label(window,text = '训练数据集源语言train.src', font=("Arial", 14))
lb1.place(x = 50, y = 100)
lb1_1 = tk.Label(window, text = "您没有选择任何文件", font=("Arial", 14))
lb1_1.place(x = 500, y = 100)

filename_2 = ''
lb2 = tk.Label(window,text = '训练数据集目标语言train.mt', font=("Arial", 14))
lb2.place(x = 50, y = 150)
lb2_1 = tk.Label(window, text = "您没有选择任何文件", font=("Arial", 14))
lb2_1.place(x = 500, y = 150)

filename_3 = ''
lb3 = tk.Label(window,text = '训练数据集标签分数train.hter', font=("Arial", 14))
lb3.place(x = 50, y = 200)
lb3_1 = tk.Label(window, text = "您没有选择任何文件", font=("Arial", 14))
lb3_1.place(x = 500, y = 200)

filename_4 = ''
lb4 = tk.Label(window,text = '测试数据集源语言test.src', font=("Arial", 14))
lb4.place(x = 50, y = 250)
lb4_1 = tk.Label(window, text = "您没有选择任何文件", font=("Arial", 14))
lb4_1.place(x = 500, y = 250)

filename_5 = ''
lb5 = tk.Label(window,text = '测试数据集目标语言test.mt', font=("Arial", 14))
lb5.place(x = 50, y = 300)
lb5_1 = tk.Label(window, text = "您没有选择任何文件", font=("Arial", 14))
lb5_1.place(x = 500, y = 300)

filename_6 = ''
lb6 = tk.Label(window,text = '待估计源语言文章dev.src', font=("Arial", 14))
lb6.place(x = 50, y = 300)
lb6_1 = tk.Label(window, text = "您没有选择任何文件", font=("Arial", 14))
lb6_1.place(x = 500, y = 300)

filename_7 = ''
lb7 = tk.Label(window,text = '待估计目标语言文章dev.mt', font=("Arial", 14))
lb7.place(x = 50, y = 300)
lb7_1 = tk.Label(window, text = "您没有选择任何文件", font=("Arial", 14))
lb7_1.place(x = 500, y = 300)


def file_selection_1():
    global filename_1
    filename_1 = tkinter.filedialog.askopenfilename()
    if filename_1 != '': 
        lb1_1.config(text = filename_1); 
    else: 
        lb1_1.config(text = "您没有选择任何文件"); 
        
def file_selection_2():
    global filename_2
    filename_2 = tkinter.filedialog.askopenfilename()
    if filename_2 != '': 
        lb2_1.config(text = filename_2); 
    else: 
        lb2_1.config(text = "您没有选择任何文件"); 

def file_selection_3():
    global filename_3
    filename_3 = tkinter.filedialog.askopenfilename()
    if filename_3 != '': 
        lb3_1.config(text = filename_3); 
    else: 
        lb3_1.config(text = "您没有选择任何文件"); 

def file_selection_4():
    global filename_4
    filename_4 = tkinter.filedialog.askopenfilename()
    if filename_4 != '': 
        lb4_1.config(text = filename_4); 
    else: 
        lb4_1.config(text = "您没有选择任何文件"); 

def file_selection_5():
    global filename_5
    filename_5 = tkinter.filedialog.askopenfilename()
    if filename_5 != '': 
        lb5_1.config(text = filename_5); 
    else: 
        lb5_1.config(text = "您没有选择任何文件"); 

btn1 = tk.Button(window, text = '选择', command = file_selection_1)
btn1.place(x = 400, y = 100)

btn2 = tk.Button(window, text = '选择', command = file_selection_2)
btn2.place(x = 400, y = 150)

btn3 = tk.Button(window, text = '选择', command = file_selection_3)
btn3.place(x = 400, y = 200)

btn4 = tk.Button(window, text = '选择', command = file_selection_4)
btn4.place(x = 400, y = 250)

btn5 = tk.Button(window, text = '选择', command = file_selection_5)
btn5.place(x = 400, y = 300)

tk.Label(window, text = '请在这里输入待估计的源语言文章', 
         font=("Arial", 10)).place(x = 50, y = 400)

tk.Label(window, text = '请在这里输入待估计的目标语言文章', 
         font=("Arial", 10)).place(x = 450, y = 400)

l_3 = tk.Label(window, text = '2、模型训练',  
             font = ("Microsoft YaHei", 14))

l_3.place(x = 50, y = 550)

l_3_1 = tk.Label(window, text = '未开始训练',  
             font = ("Arial", 14))

l_3_1.place(x = 50, y = 600)


window.mainloop()