import os
import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog 
import frame_word_level


window = tk.Tk()
window.title('翻译评估')#窗口标题
window.geometry('800x600')#窗口长度

tk.Label(window, text = '请在这里输入要翻译的文章', 
         font=("Arial")).place(x = 80, y = 100)

t_origin = tk.Text(window, 
                   width = 20, height = 20)
t_origin.place(x = 80, y = 150)

t_aim = tk.Text(window, 
                width = 20, height = 20)
t_aim.place(x = 550, y = 150)

def original_input():
    try:
        with open('dev_result.txt', 'r', encoding='UTF-8') as o_file:
            origintext = o_file.read()
            t_origin.insert('end',origintext)
    except FileNotFoundError:
        tk.messagebox.showerror('Error', '未找到文件')

def aim_input():
    try:
        with open('test2.txt', 'r', encoding='UTF-8') as o_file:
            aimtext = o_file.read()
            t_aim.insert('end',aimtext)
    except FileNotFoundError:
        tk.messagebox.showerror('Error', '未找到文件')
           
def word_level_source_selection():
    '''
    res = 'window_word_level_fc' in locals().keys()
    print(res)
    if res == True:
        window_word_level_fc.destroy()
    '''
    window_word_level_source_selection = tk.Toplevel(window)   
    frame_word_level.basedesk(window_word_level_source_selection)
    
    '''
    filename_1 = ''
    lb1 = tk.Label(window_word_level_source_selection, 
                                               text = '训练文章源train_feature', font=("Arial", 15))
    lb1.place(x = 180, y = 130)
    lb1_1 = tk.Label(window_word_level_source_selection, font=("Arial", 15))
    lb1_1.place(x = 180, y = 180)
    
    filename_2 = ''
    lb2 = tk.Label(window_word_level_source_selection, 
                                               text = '训练文章标签源train_tags', font=("Arial", 15))
    lb2.place(x = 180, y = 230)
    lb2_1 = tk.Label(window_word_level_source_selection, font=("Arial", 15))
    lb2_1.place(x = 180, y = 280)
    
    filename_3 = ''
    lb3 = tk.Label(window_word_level_source_selection, 
                                               text = '测试文章源dev_feature', font=("Arial", 15))
    lb3.place(x = 180, y = 330)
    lb3_1 = tk.Label(window_word_level_source_selection, font=("Arial", 15))
    lb3_1.place(x = 180, y = 380)
    
    filename_4 = ''
    lb4 = tk.Label(window_word_level_source_selection, 
                                               text = '测试文章标签源dev_tags', font=("Arial", 15))
    lb4.place(x = 180, y = 430)
    lb4_1 = tk.Label(window_word_level_source_selection, font=("Arial", 15))
    lb4_1.place(x = 180, y = 480)
    
    def file_selection_1():
        global filename_1
        filename_1 = tkinter.filedialog.askopenfilename()
        if filename_1 != '': 
            lb1_1.config(text = "您选择的文件是："+filename_1); 
        else: 
            lb1_1.config(text = "您没有选择任何文件"); 

    def file_selection_2():
        global filename_2
        filename_2 = tkinter.filedialog.askopenfilename()
        if filename_2 != '': 
            lb2_1.config(text = "您选择的文件是："+filename_2); 
        else: 
            lb2_1.config(text = "您没有选择任何文件"); 

    def file_selection_3():
        global filename_3
        filename_3 = tkinter.filedialog.askopenfilename()
        if filename_3 != '': 
            lb3_1.config(text = "您选择的文件是："+filename_3); 
        else: 
            lb3_1.config(text = "您没有选择任何文件"); 

    def file_selection_4():
        global filename_4
        filename_4 = tkinter.filedialog.askopenfilename()
        if filename_4 != '': 
            lb4_1.config(text = "您选择的文件是："+filename_4); 
        else: 
            lb4_1.config(text = "您没有选择任何文件");   
            
    btn1 = tk.Button(window_word_level_source_selection, text = '选择', 
                     command = file_selection_1)
    btn1.place(x = 540, y = 130)
    btn2 = tk.Button(window_word_level_source_selection, text = '选择', 
                     command = file_selection_2)
    btn2.place(x = 540, y = 230)
    btn3 = tk.Button(window_word_level_source_selection, text = '选择', 
                     command = file_selection_3)
    btn3.place(x = 540, y = 330)
    btn4 = tk.Button(window_word_level_source_selection, text = '选择', 
                     command = file_selection_4)
    btn4.place(x = 540, y = 430)
    


    def word_level_feature_selection():
        window_word_level_source_selection.destroy()
        var_word = [0 for x in range(0, 28)]
        for i in range(28):
            var_word[i]=tk.IntVar()
        window_word_level_fc = tk.Toplevel(window)
        window_word_level_fc.geometry('800x800')
        window_word_level_fc.title('词级别翻译质量评估')
        
        tk.Label(window_word_level_fc, text = '请选择特征', font=("Arial", 20)).place(x = 320, y = 30)
        
        j=40
        c_word_0 = tk.Checkbutton(window_word_level_fc, text = '源语言句子长度', variable = var_word[0], onvalue = 0+1, 
                        offvalue = 0)
        c_word_0.place(x = 20, y = 40+j)
        
        c_word_1 = tk.Checkbutton(window_word_level_fc, text = '目标语言句子长度', variable = var_word[1], onvalue = 1+1, 
                        offvalue = 0)
        c_word_1.place(x = 20, y = 80+j)
        
        c_word_2 = tk.Checkbutton(window_word_level_fc, text = '源语言句子长度与目标语言句子比例', variable = var_word[2], onvalue = 2+1, 
                        offvalue = 0)
        c_word_2.place(x = 20, y = 120+j)
        
        c_word_3 = tk.Checkbutton(window_word_level_fc, text = '目标语言单词', variable = var_word[3], onvalue = 3+1, 
                        offvalue = 0)
        c_word_3.place(x = 20, y = 160+j)
        
        c_word_4 = tk.Checkbutton(window_word_level_fc, text = '目标语言的单词的左连接单词', variable = var_word[4], onvalue = 4+1, 
                        offvalue = 0)
        c_word_4.place(x = 20, y = 200+j)
        
        c_word_5 = tk.Checkbutton(window_word_level_fc, text = '目标语言的单词的右连接单词', variable = var_word[5], onvalue = 5+1, 
                        offvalue = 0)
        c_word_5.place(x = 20, y = 240+j)
        
        c_word_6 = tk.Checkbutton(window_word_level_fc, text = '对应目标语言的源语言单词', variable = var_word[6], onvalue = 6+1, 
                        offvalue = 0)
        c_word_6.place(x = 20, y = 280+j)
        
        c_word_7 = tk.Checkbutton(window_word_level_fc, text = '对应目标语言的源语言单词的左连接单词', variable = var_word[7], onvalue = 7+1, 
                        offvalue = 0)
        c_word_7.place(x = 20, y = 320+j)
        
        c_word_8 = tk.Checkbutton(window_word_level_fc, text = '对应目标语言的源语言单词的右连接单词', variable = var_word[8], onvalue = 8+1, 
                        offvalue = 0)
        c_word_8.place(x = 20, y = 360+j)
        
        c_word_9 = tk.Checkbutton(window_word_level_fc, text = '目标语言单词是否为停止词', variable = var_word[9], onvalue = 9+1, 
                        offvalue = 0)
        c_word_9.place(x = 20, y = 400+j)
        
        c_word_10 = tk.Checkbutton(window_word_level_fc, text = '目标语言单词是否为标点符号', variable = var_word[10], onvalue = 10+1, 
                        offvalue = 0)
        c_word_10.place(x = 20, y = 440+j)
        
        c_word_11 = tk.Checkbutton(window_word_level_fc, text = '目标语言单词是否为专有名词', variable = var_word[11], onvalue = 11+1, 
                        offvalue = 0)
        c_word_11.place(x = 20, y = 480+j)    
        
        c_word_12 = tk.Checkbutton(window_word_level_fc, text = '目标语言单词是否为数字', variable = var_word[12], onvalue = 12+1, 
                        offvalue = 0)
        c_word_12.place(x = 20, y = 520+j)
        
        c_word_13 = tk.Checkbutton(window_word_level_fc, text = '包含目标词及其左上下文的ngram的最高阶', variable = var_word[13], onvalue = 13+1, 
                        offvalue = 0)
        c_word_13.place(x = 20, y = 560+j)
        
        c_word_14 = tk.Checkbutton(window_word_level_fc, text = '包含目标词及其右上下文的ngram的最高阶', variable = var_word[14], onvalue = 14+1, 
                        offvalue = 0)
        c_word_14.place(x = 420, y = 40+j)
        
        c_word_15 = tk.Checkbutton(window_word_level_fc, text = '目标词及其前两个词的退避行为', variable = var_word[15], onvalue = 15+1, 
                        offvalue = 0)
        c_word_15.place(x = 420, y = 80+j)
        
        c_word_16 = tk.Checkbutton(window_word_level_fc, text = '目标词及其旁边两个词的退避行为', variable = var_word[16], onvalue = 16+1, 
                        offvalue = 0)
        c_word_16.place(x = 420, y = 120+j)
        
        c_word_17 = tk.Checkbutton(window_word_level_fc, text = '目标词及其后两个词的退避行为', variable = var_word[17], onvalue = 17+1, 
                        offvalue = 0)
        c_word_17.place(x = 420, y = 160+j)
        
        c_word_18 = tk.Checkbutton(window_word_level_fc, text = '包含源语言词及其左上下文的ngram的最高阶', variable = var_word[18], onvalue = 18+1, 
                        offvalue = 0)
        c_word_18.place(x = 420, y = 200+j)
        
        c_word_19 = tk.Checkbutton(window_word_level_fc, text = '包含源语言词及其右上下文的ngram的最高阶', variable = var_word[19], onvalue = 19+1, 
                        offvalue = 0)
        c_word_19.place(x = 420, y = 240+j)
        
        c_word_20 = tk.Checkbutton(window_word_level_fc, text = '目标语言单词的词性', variable = var_word[20], onvalue = 20+1, 
                        offvalue = 0)
        c_word_20.place(x = 420, y = 280+j)
        
        c_word_21 = tk.Checkbutton(window_word_level_fc, text = '源语言单词的词性', variable = var_word[21], onvalue = 21+1, 
                        offvalue = 0)
        c_word_21.place(x = 420, y = 320+j)    
        
        c_word_22 = tk.Checkbutton(window_word_level_fc, text = '目标词及其左上下文', variable = var_word[22], onvalue = 22+1, 
                        offvalue = 0)
        c_word_22.place(x = 420, y = 360+j)
        
        c_word_23 = tk.Checkbutton(window_word_level_fc, text = '目标词及其右上下文', variable = var_word[23], onvalue = 23+1, 
                        offvalue = 0)
        c_word_23.place(x = 420, y = 400+j)
        
        c_word_24 = tk.Checkbutton(window_word_level_fc, text = '目标词及对应源语言词', variable = var_word[24], onvalue = 24+1, 
                        offvalue = 0)
        c_word_24.place(x = 420, y = 440+j)
        
        c_word_25 = tk.Checkbutton(window_word_level_fc, text = '目标词词性及对应源语言词词性', variable = var_word[25], onvalue = 25+1, 
                        offvalue = 0)
        c_word_25.place(x = 420, y = 480+j)
        
        c_word_26 = tk.Checkbutton(window_word_level_fc, text = '目标词、及其左上下文词和源语言词', variable = var_word[26], onvalue = 26+1, 
                        offvalue = 0)
        c_word_26.place(x = 420, y = 520+j)
        
        c_word_27 = tk.Checkbutton(window_word_level_fc, text = '目标词、及其右上下文词和源语言词', variable = var_word[27], onvalue = 27+1, 
                        offvalue = 0)
        c_word_27.place(x = 420, y = 560+j)
        
        def word_train():
            for i in range(28):
                print(var_word[0].get())
            os.chdir("E:\\BS\py")
            f1 = open("train_features.txt","r", encoding='UTF-8')
            line  = f1.readline()
            f2 = open("train_result.txt","w", encoding='UTF-8')
            f3 = open("train_tags.txt","r")
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
         
        btn_word_feature_confirm = tk.Button(window_word_level_fc, text = '上一步', command = word_level_source_selection)
        btn_word_feature_confirm.place(x = 200, y = 700)    
            
        btn_word_feature_confirm = tk.Button(window_word_level_fc, text = '确认特征', command = word_train)
        btn_word_feature_confirm.place(x = 500, y = 700)
        
    btn5 = tk.Button(window_word_level_source_selection, text = '下一步', 
                     command = word_level_feature_selection)
    btn5.place(x = 400, y = 600)
    '''
btn_original_input = tk.Button(window, text = '导入源语言文章', 
                               command = original_input)
btn_original_input.place(x = 325, y = 150)

btn_aim_input = tk.Button(window, text = '导入目标语言文章', 
                          command = aim_input)
btn_aim_input.place(x = 325, y = 250)

btn_word = tk.Button(window, text = '词级别翻译质量评估', 
                     command = word_level_source_selection)
btn_word.place(x = 325, y = 350)

btn_sentence = tk.Button(window, text = '句级别翻译质量评估')
btn_sentence.place(x = 325, y = 450)








window.mainloop()