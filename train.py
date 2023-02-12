import os
os.chdir("E:\\python")
f1 = open("train_features.txt","r",encoding='UTF-8')
line  = f1.readline()
f2 = open("train_result.txt","w",encoding='UTF-8')
f3=open("train_tags.txt","r")
tagline = f3.readline()
while line:
    z=0
    output=''
    for char in line:       
        if char=='\t':
            if z!=3 and z!=6 and z!=20 and z!=21:
                z=z+1
                if z==22:
                    break
            else:
                z=z+1
                output=output+'\t'
        elif z==3 or z==6 or z==20 or z==21:
            output=output+char
    if output!='':
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
#0源语言句子长度
#1目标语言句子长度
#2源语言句子长度与目标语言句子比例
#3目标语言单词
#4目标语言的单词的左连接单词
#5目标语言的单词的右连接单词
#6对应目标语言的源语言单词
#7对应目标语言的源语言单词的左连接单词
#8对应目标语言的源语言单词的右连接单词
#9目标语言单词是否为停止词
#10目标语言单词是否为标点符号
#11目标语言单词是否为专有名词
#12目标语言单词是否为数字
#20目标语言单词的词性
#21源语言单词的词性
