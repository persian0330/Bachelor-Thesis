import os
os.chdir("E:\\python")
f1=open("deal_test_result_0311.txt","r",encoding='UTF-8')
line1=f1.readline()
f2=open("dev_tags_0311.txt","r")
line2=f2.readline()
OK_OK=0#TP
OK_BAD=0#FP
BAD_OK=0#FN
BAD_BAD=0#TN
Precision=0.0
Recall=0.0
F1=0.0
i=1
while line1!='':
    while line1[0]=='#' or line1[0]=='\n':
        line1=f1.readline()
        print(i)
        i=i+1
    if line1.split()[6][0]=='O' and line2[0]=='O':
        OK_OK=OK_OK+1
    elif line1.split()[6][0]=='O' and line2[0]=='B':
        OK_BAD=OK_BAD+1
    elif line1.split()[6][0]=='B' and line2[0]=='O':
        BAD_OK=BAD_OK+1
    elif line1.split()[6][0]=='B' and line2[0]=='B':
        BAD_BAD=BAD_BAD+1
    line2=f2.readline()
    line1=f1.readline()
    print(i)
    i=i+1
print('TP(OK_OK)有%d个'%(OK_OK))
print('FP(OK_BAD)有%d个'%OK_BAD)
print('FN(BAD_OK)有%d个'%BAD_OK)
print('TN(BAD_BAD)有%d个'%BAD_BAD)
Precision=BAD_BAD/(BAD_BAD+BAD_OK)
Recall=BAD_BAD/(BAD_BAD+OK_BAD)
print('BAD精确率为%.6f'%(Precision))
print('BAD召回率为%.6f'%(Recall))
F1=2*Precision*Recall/(Precision+Recall)
print('F(BAD)值为%.6f'%(F1))
f1.close()
f2.close()
