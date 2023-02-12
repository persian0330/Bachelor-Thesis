import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog 
import os
import shutil 
import time



class basedesk():
    def __init__(self,master):
        self.window = master
        self.window.config()
        self.window.title('词级别翻译质量评估')
        self.window.geometry('800x800')

        initface(self.window)        
                
class initface():
    a = 5
    def __init__(self,master):
        try:
            print('filename_1:' + filename_1)
            print('filename_2:' + filename_2)
            print('filename_3:' + filename_3)
            print('filename_4:' + filename_4)
        except NameError:
            print('OK')
        else:
            del filename_1
            del filename_2
            del filename_3
            del filename_4
        self.master = master
        #self.master.config()
        #基准界面initface
        self.initface = tk.Frame(self.master, width = 800, height = 800)
        
        filename_1 = ''
        lb1 = tk.Label(self.initface,text = '训练文章源train_feature', font=("Arial", 15))
        lb1.place(x = 180, y = 130)
        lb1_1 = tk.Label(self.initface, text = "您没有选择任何文件", font=(5))
        lb1_1.place(x = 180, y = 180)
        
        filename_2 = ''
        lb2 = tk.Label(self.initface,text = '训练文章标签源train_tags', font=("Arial", 15))
        lb2.place(x = 180, y = 230)
        lb2_1 = tk.Label(self.initface, text = "您没有选择任何文件", font=(5))
        lb2_1.place(x = 180, y = 280)
        
        filename_3 = ''
        lb3 = tk.Label(self.initface,text = '测试文章源dev_feature', font=("Arial", 15))
        lb3.place(x = 180, y = 330)
        lb3_1 = tk.Label(self.initface, text = "您没有选择任何文件", font=(5))
        lb3_1.place(x = 180, y = 380)
        
        filename_4 = ''
        lb4 = tk.Label(self.initface,text = '测试文章标签源dev_tags', font=("Arial", 15))
        lb4.place(x = 180, y = 430)
        lb4_1 = tk.Label(self.initface, text = "您没有选择任何文件", font=(5))
        lb4_1.place(x = 180, y = 480)
        
        
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
        
        def next_1():

            try:
                global filename_1
                global filename_2
                global filename_3
                global filename_4
                #print('filename_1:' + filename_1)
                #print('filename_2:' + filename_2)
                #print('filename_3:' + filename_3)
                #print('filename_4:' + filename_4)
            except NameError:
                tk.messagebox.showerror(title = '错误', message = '未完全选择目录')
            else:
                self.initface.destroy()
                face1(self.master) 

        
        btn1 = tk.Button(self.initface, text = '选择', 
                         command = file_selection_1)
        btn1.place(x = 540, y = 130)
        btn2 = tk.Button(self.initface, text = '选择', 
                         command = file_selection_2)
        btn2.place(x = 540, y = 230)
        btn3 = tk.Button(self.initface, text = '选择', 
                         command = file_selection_3)
        btn3.place(x = 540, y = 330)
        btn4 = tk.Button(self.initface, text = '选择', 
                         command = file_selection_4)
        btn4.place(x = 540, y = 430)     
        
        btn = tk.Button(self.initface, text='下一步',command=next_1)
        btn.place(x = 380 , y = 700)
        
        btn_exit = tk.Button(self.initface, text='退出',command=self.word_level_exit)
        btn_exit.place(x = 700 , y = 700)
                
        self.initface.pack()
        
                
    def word_level_exit(self,):
        self.master.destroy()
    
     
    
class face1():

    def __init__(self,master):
        '''
        print('filename_1:' + filename_1)
        print('filename_2:' + filename_2)
        print('filename_3:' + filename_3)
        print('filename_4:' + filename_4)
        '''
        self.master = master
        self.n = 0
        #self.master.config()
        self.face1 = tk.Frame(self.master, width = 800, height = 800)
        var_word = [0 for x in range(0, 28)]
        for i in range(28):
            var_word[i]=tk.IntVar()
        
        tk.Label(self.face1, text = '请选择特征', font=("Arial", 20)).place(x = 320, y = 30)
        
        j=40
        c_word_0 = tk.Checkbutton(self.face1, text = '源语言句子长度', variable = var_word[0], onvalue = 0+1, 
                        offvalue = 0)
        c_word_0.place(x = 20, y = 40+j)
        
        c_word_1 = tk.Checkbutton(self.face1, text = '目标语言句子长度', variable = var_word[1], onvalue = 1+1, 
                        offvalue = 0)
        c_word_1.place(x = 20, y = 80+j)
        
        c_word_2 = tk.Checkbutton(self.face1, text = '源语言句子长度与目标语言句子比例', variable = var_word[2], onvalue = 2+1, 
                        offvalue = 0)
        c_word_2.place(x = 20, y = 120+j)
        
        c_word_3 = tk.Checkbutton(self.face1, text = '目标语言单词', variable = var_word[3], onvalue = 3+1, 
                        offvalue = 0)
        c_word_3.place(x = 20, y = 160+j)
        
        c_word_4 = tk.Checkbutton(self.face1, text = '目标语言的单词的左连接单词', variable = var_word[4], onvalue = 4+1, 
                        offvalue = 0)
        c_word_4.place(x = 20, y = 200+j)
        
        c_word_5 = tk.Checkbutton(self.face1, text = '目标语言的单词的右连接单词', variable = var_word[5], onvalue = 5+1, 
                        offvalue = 0)
        c_word_5.place(x = 20, y = 240+j)
        
        c_word_6 = tk.Checkbutton(self.face1, text = '对应目标语言的源语言单词', variable = var_word[6], onvalue = 6+1, 
                        offvalue = 0)
        c_word_6.place(x = 20, y = 280+j)
        
        c_word_7 = tk.Checkbutton(self.face1, text = '对应目标语言的源语言单词的左连接单词', variable = var_word[7], onvalue = 7+1, 
                        offvalue = 0)
        c_word_7.place(x = 20, y = 320+j)
        
        c_word_8 = tk.Checkbutton(self.face1, text = '对应目标语言的源语言单词的右连接单词', variable = var_word[8], onvalue = 8+1, 
                        offvalue = 0)
        c_word_8.place(x = 20, y = 360+j)
        
        c_word_9 = tk.Checkbutton(self.face1, text = '目标语言单词是否为停止词', variable = var_word[9], onvalue = 9+1, 
                        offvalue = 0)
        c_word_9.place(x = 20, y = 400+j)
        
        c_word_10 = tk.Checkbutton(self.face1, text = '目标语言单词是否为标点符号', variable = var_word[10], onvalue = 10+1, 
                        offvalue = 0)
        c_word_10.place(x = 20, y = 440+j)
        
        c_word_11 = tk.Checkbutton(self.face1, text = '目标语言单词是否为专有名词', variable = var_word[11], onvalue = 11+1, 
                        offvalue = 0)
        c_word_11.place(x = 20, y = 480+j)    
        
        c_word_12 = tk.Checkbutton(self.face1, text = '目标语言单词是否为数字', variable = var_word[12], onvalue = 12+1, 
                        offvalue = 0)
        c_word_12.place(x = 20, y = 520+j)
        
        c_word_13 = tk.Checkbutton(self.face1, text = '包含目标词及其左上下文的ngram的最高阶', variable = var_word[13], onvalue = 13+1, 
                        offvalue = 0)
        c_word_13.place(x = 20, y = 560+j)
        
        c_word_14 = tk.Checkbutton(self.face1, text = '包含目标词及其右上下文的ngram的最高阶', variable = var_word[14], onvalue = 14+1, 
                        offvalue = 0)
        c_word_14.place(x = 420, y = 40+j)
        
        c_word_15 = tk.Checkbutton(self.face1, text = '目标词及其前两个词的退避行为', variable = var_word[15], onvalue = 15+1, 
                        offvalue = 0)
        c_word_15.place(x = 420, y = 80+j)
        
        c_word_16 = tk.Checkbutton(self.face1, text = '目标词及其旁边两个词的退避行为', variable = var_word[16], onvalue = 16+1, 
                        offvalue = 0)
        c_word_16.place(x = 420, y = 120+j)
        
        c_word_17 = tk.Checkbutton(self.face1, text = '目标词及其后两个词的退避行为', variable = var_word[17], onvalue = 17+1, 
                        offvalue = 0)
        c_word_17.place(x = 420, y = 160+j)
        
        c_word_18 = tk.Checkbutton(self.face1, text = '包含源语言词及其左上下文的ngram的最高阶', variable = var_word[18], onvalue = 18+1, 
                        offvalue = 0)
        c_word_18.place(x = 420, y = 200+j)
        
        c_word_19 = tk.Checkbutton(self.face1, text = '包含源语言词及其右上下文的ngram的最高阶', variable = var_word[19], onvalue = 19+1, 
                        offvalue = 0)
        c_word_19.place(x = 420, y = 240+j)
        
        c_word_20 = tk.Checkbutton(self.face1, text = '目标语言单词的词性', variable = var_word[20], onvalue = 20+1, 
                        offvalue = 0)
        c_word_20.place(x = 420, y = 280+j)
        
        c_word_21 = tk.Checkbutton(self.face1, text = '源语言单词的词性', variable = var_word[21], onvalue = 21+1, 
                        offvalue = 0)
        c_word_21.place(x = 420, y = 320+j)    
        
        c_word_22 = tk.Checkbutton(self.face1, text = '目标词及其左上下文', variable = var_word[22], onvalue = 22+1, 
                        offvalue = 0)
        c_word_22.place(x = 420, y = 360+j)
        
        c_word_23 = tk.Checkbutton(self.face1, text = '目标词及其右上下文', variable = var_word[23], onvalue = 23+1, 
                        offvalue = 0)
        c_word_23.place(x = 420, y = 400+j)
        
        c_word_24 = tk.Checkbutton(self.face1, text = '目标词及对应源语言词', variable = var_word[24], onvalue = 24+1, 
                        offvalue = 0)
        c_word_24.place(x = 420, y = 440+j)
        
        c_word_25 = tk.Checkbutton(self.face1, text = '目标词词性及对应源语言词词性', variable = var_word[25], onvalue = 25+1, 
                        offvalue = 0)
        c_word_25.place(x = 420, y = 480+j)
        
        c_word_26 = tk.Checkbutton(self.face1, text = '目标词、及其左上下文词和源语言词', variable = var_word[26], onvalue = 26+1, 
                        offvalue = 0)
        c_word_26.place(x = 420, y = 520+j)
        
        c_word_27 = tk.Checkbutton(self.face1, text = '目标词、及其右上下文词和源语言词', variable = var_word[27], onvalue = 27+1, 
                        offvalue = 0)
        c_word_27.place(x = 420, y = 560+j)
        
        def final_confirm():
            is_final_confirm = tk.messagebox.askokcancel(title = '确认', message = '是否确认特征选择完毕？点击“确定”，则开始处理语料->训练->测试过程(预计要花费一段时间，取决于特征值多少)')
            if is_final_confirm:
                self.n = 0 
                for i in range(28):
                    if var_word[i].get()>0:
                        self.n = self.n + 1
                print(self.n)
                os.makedirs("E:\\BS\\test")
                word_train()
        def word_train():

                 
            #开始处理train_feature
            print("当前时间为:"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) 
            os.chdir("E:\\BS\py")
            f1 = open(filename_1,"r", encoding='UTF-8')
            line  = f1.readline()
            f2 = open("train_result.txt","w", encoding='UTF-8')
            f3 = open(filename_2,"r")
            tagline = f3.readline()
            while line:
                z=0
                output=''
                for char in line:       
                    if char=='\t' or char=='\n':
                        if z!=var_word[0].get()-1 and z!=var_word[1].get()-1 and z!=var_word[2].get()-1 and z!=var_word[3].get()-1 and z!=var_word[4].get()-1 and z!=var_word[5].get()-1 and z!=var_word[6].get()-1 and z!=var_word[7].get()-1 and z!=var_word[8].get()-1 and z!=var_word[9].get()-1 and z!=var_word[10].get()-1 and z!=var_word[11].get()-1 and z!=var_word[12].get()-1 and z!=var_word[13].get()-1 and z!=var_word[14].get()-1 and z!=var_word[15].get()-1 and z!=var_word[16].get()-1 and z!=var_word[17].get()-1 and z!=var_word[18].get()-1 and z!=var_word[19].get()-1 and z!=var_word[20].get()-1 and z!=var_word[21].get()-1 and z!=var_word[22].get()-1 and z!=var_word[23].get()-1 and z!=var_word[24].get()-1 and z!=var_word[25].get()-1 and z!=var_word[26].get()-1 and z!=var_word[27].get()-1:
                            z=z+1
                            if z==28:
                                break
                        else:
                            z=z+1
                            output=output+'\t'
                    elif z==var_word[0].get()-1 or z==var_word[1].get()-1 or z==var_word[2].get()-1 or z==var_word[3].get()-1 or z==var_word[4].get()-1 or z==var_word[5].get()-1 or z==var_word[6].get()-1 or z==var_word[7].get()-1 or z==var_word[8].get()-1 or z==var_word[9].get()-1 or z==var_word[10].get()-1 or z==var_word[11].get()-1 or z==var_word[12].get()-1 or z==var_word[13].get()-1 or z==var_word[14].get()-1 or z==var_word[15].get()-1 or z==var_word[16].get()-1 or z==var_word[17].get()-1 or z==var_word[18].get()-1 or z==var_word[19].get()-1 or z==var_word[20].get()-1 or z==var_word[21].get()-1 or z==var_word[22].get()-1 or z==var_word[23].get()-1  or z==var_word[24].get()-1 or z==var_word[25].get()-1 or z==var_word[26].get()-1 or z==var_word[27].get()-1:
                        output=output+char
                if output!='' and output!='\t':
                    print(output+tagline.split()[0])
                    f2.write(output+tagline.split()[0]+'\n')
                    tagline = f3.readline()
                else:
                    print(output)
                    f2.write(output+'\n')
                line = f1.readline()
            f1.close()
            f2.close()
            f3.close()
            
            
            #开始处理dev_feature
            os.chdir("E:\\BS\py")
            f1 = open(filename_3,"r",encoding='UTF-8')
            line  = f1.readline()
            f2 = open("dev_result.txt","w",encoding='UTF-8')
            while line:
                z=0
                output=''
                for char in line:       
                    if char=='\t' or char=='\n':
                        if z!=var_word[0].get()-1 and z!=var_word[1].get()-1 and z!=var_word[2].get()-1 and z!=var_word[3].get()-1 and z!=var_word[4].get()-1 and z!=var_word[5].get()-1 and z!=var_word[6].get()-1 and z!=var_word[7].get()-1 and z!=var_word[8].get()-1 and z!=var_word[9].get()-1 and z!=var_word[10].get()-1 and z!=var_word[11].get()-1 and z!=var_word[12].get()-1 and z!=var_word[13].get()-1 and z!=var_word[14].get()-1 and z!=var_word[15].get()-1 and z!=var_word[16].get()-1 and z!=var_word[17].get()-1 and z!=var_word[18].get()-1 and z!=var_word[19].get()-1 and z!=var_word[20].get()-1 and z!=var_word[21].get()-1 and z!=var_word[22].get()-1 and z!=var_word[23].get()-1 and z!=var_word[24].get()-1 and z!=var_word[25].get()-1 and z!=var_word[26].get()-1 and z!=var_word[27].get()-1:
                            z=z+1
                            if z==28:
                                break
                        else:
                            z=z+1
                            output=output+'\t'
                    elif z==var_word[0].get()-1 or z==var_word[1].get()-1 or z==var_word[2].get()-1 or z==var_word[3].get()-1 or z==var_word[4].get()-1 or z==var_word[5].get()-1 or z==var_word[6].get()-1 or z==var_word[7].get()-1 or z==var_word[8].get()-1 or z==var_word[9].get()-1 or z==var_word[10].get()-1 or z==var_word[11].get()-1 or z==var_word[12].get()-1 or z==var_word[13].get()-1 or z==var_word[14].get()-1 or z==var_word[15].get()-1 or z==var_word[16].get()-1 or z==var_word[17].get()-1 or z==var_word[18].get()-1 or z==var_word[19].get()-1 or z==var_word[20].get()-1 or z==var_word[21].get()-1 or z==var_word[22].get()-1 or z==var_word[23].get()-1  or z==var_word[24].get()-1 or z==var_word[25].get()-1 or z==var_word[26].get()-1 or z==var_word[27].get()-1:
                        output=output+char
                print(output)
                f2.write(output+'\n')
                line = f1.readline()
            f1.close()
            f2.close()
            
            shutil.move("E:\\BS\\py\\train_result.txt","E:\\BS\\CRF\\CRF")
            shutil.move("E:\\BS\\py\\dev_result.txt","E:\\BS\\CRF\\CRF")
                                    
            tk.messagebox.showinfo(title = '完成', message = '语料处理完成！即将开始训练！')
            self.next_1()
            
        btn_n = tk.Button(self.face1, text='确认',command=final_confirm)
        btn_n.place(x = 480 , y = 700)
        btn_p = tk.Button(self.face1, text='上一步',command=self.previous_1)
        btn_p.place(x = 280 , y = 700)
        btn_exit = tk.Button(self.face1, text='退出',command=self.word_level_exit)
        btn_exit.place(x = 700 , y = 700)
        
            
        self.face1.pack()    
        
    def next_1(self):
        self.face1.destroy()
        face2(self.master, self.n)
        
    def previous_1(self):

        
        self.face1.destroy()
        initface(self.master)
        
    def word_level_exit(self,):
        self.master.destroy()
        
class face2():
    

    def __init__(self,master,num):
        self.master = master
        self.n = num
        print(self.n)
        #self.master.config(bg='red')
        self.face2 = tk.Frame(self.master, width = 800, height = 800)
        
        
        t_aim = tk.Text(self.face2, width = 50, height = 30)
        t_aim.place(x = 80, y = 150)
        
        t_F = tk.Text(self.face2, width = 20, height = 20)
        t_F.place(x = 580, y = 170)
                
        
        
        print("开始调用crf训练")
        os.system('start /WAIT E:\\BS\\CRF\\CRF\\crf_learn.exe.lnk')
        print("调用结束")
        print("当前时间为:"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) 
        print("开始调用crf测试")
        os.system('start /WAIT E:\\BS\\CRF\\CRF\\crf_test.exe.lnk')
        print("调用结束") 
        print("当前时间为:"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print("开始移动文件") 
        
        shutil.move("E:\\BS\\CRF\\CRF\\train_result.txt","E:\\BS\\test")
        shutil.move("E:\\BS\\CRF\\CRF\\dev_result.txt","E:\\BS\\test")
        shutil.move("E:\\BS\\CRF\\CRF\\model_deal_result","E:\\BS\\test")
        shutil.move("E:\\BS\\CRF\\CRF\\model_deal_result.txt","E:\\BS\\test")

        shutil.move("E:\\BS\\CRF\\CRF\\deal_test_result.txt","E:\\BS\\py")
        print("移动文件结束")
        
        
        def Evaluation(self):

            
            #F_OK值
            os.chdir("E:\BS\py")
            f1=open("deal_test_result.txt","r",encoding='UTF-8')
            line1=f1.readline()
            f2=open(filename_4,"r")
            line2=f2.readline()
            f3 = open("result.txt","a")
            OK_OK = 0#TP
            OK_BAD = 0#FP
            BAD_OK = 0#FN
            BAD_BAD = 0#TN
            Precision = 0.0
            Recall = 0.0
            F1 = 0.0
            i = 1
            while line1!='':
                while line1[0]=='#' or line1[0]=='\n':
                    line1=f1.readline()
                    if line1 == '':
                        break;
                    #print(i)
                    i=i+1
                if line1 !='':
                    if line1.split()[self.n][0]=='O' and line2[0]=='O':
                        OK_OK=OK_OK+1
                    elif line1.split()[self.n][0]=='O' and line2[0]=='B':
                        OK_BAD=OK_BAD+1
                    elif line1.split()[self.n][0]=='B' and line2[0]=='O':
                        BAD_OK=BAD_OK+1
                    elif line1.split()[self.n][0]=='B' and line2[0]=='B':
                        BAD_BAD=BAD_BAD+1
                    line2=f2.readline()
                    line1=f1.readline()
                    #print(i)
                    i=i+1
                    
                    
            print('TP(OK_OK)有%d个'%OK_OK)
            t_F.insert('end','TP(OK_OK)有%d个\n'%OK_OK)
            print('FP(OK_BAD)有%d个'%OK_BAD)
            t_F.insert('end','TP(OK_BAD)有%d个\n'%OK_BAD)
            print('FN(BAD_OK)有%d个'%BAD_OK)
            t_F.insert('end','TP(BAD_OK)有%d个\n'%BAD_OK)
            print('TN(BAD_BAD)有%d个'%BAD_BAD)
            t_F.insert('end','TP(BAD_BAD)有%d个\n'%BAD_BAD)
            Precision=OK_OK/(OK_OK+OK_BAD)
            Recall=OK_OK/(OK_OK+BAD_OK)
            print('OK精确率为%.6f'%(Precision))
            t_F.insert('end','OK精确率为%.6f\n'%(Precision))
            print('OK召回率为%.6f'%(Recall))
            t_F.insert('end','OK召回率为%.6f\n'%(Recall))
            F1=2*Precision*Recall/(Precision+Recall)
            print('F(OK)值为%.6f'%(F1))
            t_F.insert('end','F(OK)值为%.6f\n'%(F1))
            
            f3.write('TP(OK_OK)有%d个   '%(OK_OK))
            f3.write('FP(OK_BAD)有%d个   '%OK_BAD)
            f3.write('FN(BAD_OK)有%d个   '%BAD_OK)
            f3.write('TN(BAD_BAD)有%d个   '%BAD_BAD)            
            f3.write('OK精确率为%.6f   '%(Precision))
            f3.write('OK召回率为%.6f   '%(Recall))            
            f3.write('F(OK)值为%.6f\n'%(F1))	        

            f1.close()
            f2.close()
            f3.close()
            
            print("F(OK)统计完成")
    
            #F_BAD值    
            os.chdir("E:\BS\py")
            f1=open("deal_test_result.txt","r",encoding='UTF-8')
            line1=f1.readline()
            f2=open(filename_4,"r")
            line2=f2.readline()
            f3 = open("result.txt","a")
            OK_OK = 0#TP
            OK_BAD = 0#FP
            BAD_OK = 0#FN
            BAD_BAD = 0#TN
            Precision = 0.0
            Recall = 0.0
            F1 = 0.0
            i = 1
            while line1!='':
                while line1[0]=='#' or line1[0]=='\n':
                    line1=f1.readline()
                    if line1 == '':
                        break;
                    #print(i)
                    i=i+1
                if line1 !='':
                    if line1.split()[self.n][0]=='O' and line2[0]=='O':
                        OK_OK=OK_OK+1
                    elif line1.split()[self.n][0]=='O' and line2[0]=='B':
                        OK_BAD=OK_BAD+1
                    elif line1.split()[self.n][0]=='B' and line2[0]=='O':
                        BAD_OK=BAD_OK+1
                    elif line1.split()[self.n][0]=='B' and line2[0]=='B':
                        BAD_BAD=BAD_BAD+1
                    line2=f2.readline()
                    line1=f1.readline()
                    #print(i)
                    i=i+1
            print('TP(OK_OK)有%d个'%(OK_OK))
            t_F.insert('end','TP(OK_OK)有%d个\n'%OK_OK)
            print('FP(OK_BAD)有%d个'%(OK_BAD))
            t_F.insert('end','TP(OK_BAD)有%d个\n'%OK_BAD)
            print('FN(BAD_OK)有%d个'%(BAD_OK))
            t_F.insert('end','TP(BAD_OK)有%d个\n'%BAD_OK)
            print('TN(BAD_BAD)有%d个'%(BAD_BAD))
            t_F.insert('end','TP(BAD_BAD)有%d个\n'%BAD_BAD)
            
            f3.write('TP(OK_OK)有%d个   '%(OK_OK))
            f3.write('FP(OK_BAD)有%d个   '%(OK_BAD))
            f3.write('FN(BAD_OK)有%d个   '%(BAD_OK))
            f3.write('TN(BAD_BAD)有%d个   '%(BAD_BAD))
            
            if BAD_BAD+BAD_OK!=0:
                Precision=BAD_BAD/(BAD_BAD+BAD_OK)
                print('BAD精确率为%.6f'%(Precision))
                t_F.insert('end','BAD精确率为%.6f\n'%(Precision))
                f3.write('BAD精确率为%.6f   '%(Precision))
            else:
                Precision=2
                print('BAD精确率为0')
                t_F.insert('end','BAD精确率为0\n')
                f3.write('BAD精确率为0   ')
            
            if BAD_BAD+OK_BAD!=0:
                Recall=BAD_BAD/(BAD_BAD+OK_BAD)
                print('BAD召回率为%.6f'%(Recall))
                t_F.insert('end','BAD召回率为%.6f\n'%(Recall))
                f3.write('BAD召回率为%.6f   '%(Recall))
            else:
                Recall=2
                print('BAD召回率为0')
                t_F.insert('end','BAD召回率为0\n')
                f3.write('BAD召回率为0   ')
            	
            if Precision+Recall!=0 and Precision<2 and Recall<2:
                F1=2*Precision*Recall/(Precision+Recall)
                print('F(BAD)值为%.6f'%(F1))
                t_F.insert('end','F(BAD)值为%.6f\n'%(F1))
                f3.write('F(BAD)值为%.6f\n'%(F1))
            else:
                print('F(BAD)值为0')
                t_F.insert('end','F(BAD)值为0\n')
                f3.write('F(BAD)值为0')	
            
                 
            f1.close()
            f2.close()
            f3.close()
            
        
            print("F(BAD)统计完成")
            
            #评估分数
            '''
            def convert(str):
                new_str = ''
                z = 0
                for i in str:
                    if i == '/':
                        z = 1
                    elif z == 1:
                        new_str = new_str + i
                return float(new_str)
            
            print(self.var_mark.get())
            '''
            #开始处理train_feature
            os.chdir("E:\BS\py")
            print("当前时间为:"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) 
            f1 = open(filename_3, "r", encoding='UTF-8')
            line  = f1.readline()
            f2 = open("mark_result.txt", "w", encoding='UTF-8')
            f3 = open("deal_test_result.txt", "r", encoding='UTF-8')
            f4 = open(filename_4, "r", encoding = 'UTF-8')
            tagline = f3.readline()
            real_tagline = f4.readline()
            while line:
                z=0
                output=''
                for char in line:       
                    if char=='\t' or char=='\n':
                        if z!=3:
                            z=z+1
                            if z==4:
                                break
                        else:
                            z=z+1
                            output=output+'\t'
                    elif z==3:
                        output=output+char
                if output!='' and output!='\t':
                    while tagline[0] =='#' or tagline[0] =='\n':
                        tagline = f3.readline()
                    output = output + tagline.split()[self.n] + ' ' + real_tagline     
                    #print(output)
                    f2.write(output + '\n')
                    tagline = f3.readline()
                    real_tagline = f4.readline()
                else:
                    f2.write(output+'\n')
                line = f1.readline()
            f1.close()
            f2.close()
            f3.close()
        
            f1 = open("mark_result.txt","r", encoding='UTF-8')
            line1 = f1.readline()
            while line1:
                while line1 == '\n':
                    line1 = f1.readline()
                if line1 == '':
                    break
                z = 0
                a = t_aim.index('insert')
                t_aim.insert('end',line1.split()[0])
                b = t_aim.index('insert')
                if(line1.split()[1][0] == 'B'):
                    z = 1
                if(line1.split()[2][0] == 'B'):
                    z = z + 0.5 
                if z == 1:
                    t_aim.tag_add('BAD_1', a, b)
                    t_aim.tag_config('BAD_1', foreground = 'red')
                elif z == 0.5:
                    t_aim.tag_add('BAD_0.5', a, b)
                    t_aim.tag_config('BAD_0.5', foreground = 'blue')  
                elif z == 1.5:
                    t_aim.tag_add('BAD_1.5', a, b)
                    t_aim.tag_config('BAD_1.5', foreground = 'green') 
                print(line1.split()[0])
                if(line1.split()[0] == '.' or line1.split()[0] == '?' or line1.split()[0] == ':'):
                    t_aim.insert('end','\n')
                else:
                    t_aim.insert('end',' ')
                line1 = f1.readline()
            f1.close()
           
            print('完成')
            print("当前时间为:"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) 

            
            
            shutil.move("E:\\BS\\py\\deal_test_result.txt","E:\\BS\\test") 
            shutil.move("E:\\BS\\py\\result.txt","E:\\BS\\test")
            shutil.move("E:\\BS\\py\\mark_result.txt","E:\\BS\\test") 
            
            print("程序结束时间为:"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) 
            
        def last_one():
            is_last_one = tk.messagebox.askokcancel(title = '确认', message = '确定进行评估吗？')
            if is_last_one:
                Evaluation(self)
        
        
        btn_exit = tk.Button(self.face2,text='比较',command = last_one)
        btn_exit.place(x = 420 , y = 95)
        
        btn_exit = tk.Button(self.face2,text='退出',command = self.word_level_exit)
        btn_exit.place(x = 700 , y = 700)
        
        
    
        self.face2.pack()
        
    
    
    def next_1(self):
        self.face2.destroy()
        initface(self.master)
        
    def previous_1(self):
        self.face2.destroy()
        face1(self.master)
        
    def word_level_exit(self,):
        is_exit_confirm = tk.messagebox.askokcancel(title = '确认退出', message = '是否确认退出？')
        if is_exit_confirm:
            self.master.destroy()
    
if __name__ == '__main__':    
    window = tk.Tk()
    print('__main__')
    basedesk(window)
    window.mainloop()



