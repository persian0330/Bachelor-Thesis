import os
import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog 
import frame_word_level


window = tk.Tk()
window.title('翻译评估')#窗口标题
window.geometry('800x800')#窗口长度


tk.Label(window, text = '沈航机器翻译译文质量自动估计系统', 
         font=("Microsoft YaHei", 20)).place(x = 140, y = 20)


tk.Label(window, text = '请在这里输入已标注的要估计的译文', 
         font=("Arial", 10)).place(x = 80, y = 120)

t_origin = tk.Text(window, 
                   width = 50, height = 30)
t_origin.place(x = 80, y = 150)

def file_create():
    
    text = t_origin.get('0.0','end')
    
    save_file_name = tkinter.filedialog.asksaveasfilename(filetypes=[('TEXT','txt'),("python",".py")])#返回文件名
    print(save_file_name)
    
    f = open(save_file_name, "w", encoding = 'UTF-8')
    f.write(text)
    f.close()
    
           
def word_level_source_selection():

    window_word_level_source_selection = tk.Toplevel(window)   
    frame_word_level.basedesk(window_word_level_source_selection)
    

btn_original_input = tk.Button(window, text = '手动输入待估计译文', 
                               command = file_create)
btn_original_input.place(x = 550, y = 150)

btn_aim_input = tk.Button(window, text = '导入待估计译文')

btn_aim_input.place(x = 550, y = 250)

btn_word = tk.Button(window, text = '词级别译文质量估计', 
                     command = word_level_source_selection)
btn_word.place(x = 550, y = 350)

btn_sentence = tk.Button(window, text = '句级别译文质量估计')
btn_sentence.place(x = 550, y = 450)








window.mainloop()