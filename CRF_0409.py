import os
import shutil
import time
#输出当前时间
print("程序开始时间为:"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

os.makedirs("E:\\BS\\test")   

train = os.system(r"python E:\BS\py\train.py")
if train == 0:
    print("train语料处理完成")
    print("当前时间为:"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    shutil.move("E:\\BS\\py\\train_result.txt","E:\\BS\\CRF\\CRF")
else:
    print("train语料处理未完成")
    
dev = os.system(r"python E:\BS\py\dev.py")
if dev == 0:
    print("dev语料处理完成")
    print("当前时间为:"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    shutil.move("E:\\BS\\py\\dev_result.txt","E:\\BS\\CRF\\CRF")
else:
    print("dev语料处理未完成")

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
F_OK = os.system(r"python E:\BS\py\OK.py")
if F_OK == 0:
    print("F(OK)统计完成")
else:
    print("F(OK)统计未完成")
    
F_BAD = os.system(r"python E:\BS\py\BAD.py")
if F_BAD == 0:
    print("F(BAD)统计完成")
else:
    print("F(BAD)统计未完成")
 
shutil.move("E:\\BS\\py\\deal_test_result.txt","E:\\BS\\test") 
shutil.move("E:\\BS\\py\\result.txt","E:\\BS\\test")
#输出当前时间
print("程序结束时间为:"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))