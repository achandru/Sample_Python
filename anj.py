'''
Created on Dec 4, 2017

@author: chance
'''
from datetime import datetime
from datetime import timedelta
import pandas as pd
import time
CurDate= datetime.now()


df=pd.read_csv("/home/dalchemy/Enmetric_data/anjali_28to03.csv")
df1 = pd.read_csv("/home/dalchemy/Anjali_IO/Anjus/1stAnju.csv", header=None)
abcd = df["occurred_at"]

changed=[]
for i in abcd:
    conv=datetime.strptime(i,"%Y-%m-%d %H:%M:%S")
    if(conv.day)<=9:
	day=str(str(conv.day).zfill(2))
    else:
	day=str(conv.day)
    if(conv.hour<=9 and conv.minute<=9):
        ab=str(conv.year)+str(conv.month)+day+str(str(conv.hour).zfill(2))+str(str(conv.minute).zfill(2))
    elif(conv.hour<=9 and conv.minute>9):
        ab=str(conv.year)+str(conv.month)+day+str(str(conv.hour).zfill(2))+str(conv.minute)
    elif(conv.hour>9 and conv.minute<=9):
        ab=str(conv.year)+str(conv.month)+day+str(conv.hour)+str(str(conv.minute).zfill(2))
    else:
        ab=str(conv.year)+str(conv.month)+day+str(conv.hour)+str(conv.minute)
    changed.append(ab)
df["changed"]=changed

print "========================================================================================================="

empty=pd.DataFrame(index=['A'],columns=[range(0,16)])
col_df=df.columns.values
col_df1=df1.columns.values
i_1=[]
j_1=[]


for j in range(0,len(df["changed"])):
    flag=0
    for i in range(0,len(df1[1])):
        if str(df1[1][i])==str(df["changed"][j]):
                i_1.append(i)
                j_1.append(j)
                flag=1
                break
        else:
            if i==(len(df1[1])-1) and flag==0:
                i_1.append(-99)
                j_1.append(j)
                #print len(i_1),len(j_1)

#print len(i_1)
#print len(j_1)

d=[]
e=[]
for x in range(0,len(i_1)):
    if i_1[x] != -99:
        d.append(df1.loc[i_1[x]])
        e.append(df.loc[j_1[x]])
    else:
        d.append(empty.loc['A'])
        e.append(df.loc[j_1[x]])

print d
print e
        
d1=pd.DataFrame(d)
e1=pd.DataFrame(e)
print d1
print e1
#d1.to_csv("/home/dalchemy/Anjali_IO/Mail/d1.csv", sep=',')
#e1.to_csv("/home/dalchemy/Anjali_IO/Mail/e1.csv", sep=',')
