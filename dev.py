import os
os.chdir("E:\\python")
f1 = open("dev_features.txt","r",encoding='UTF-8')
line  = f1.readline()
f2 = open("test.txt","w",encoding='UTF-8')
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
    print(output)
    f2.write(output+'\n')
    line = f1.readline()
f1.close()
f2.close()
