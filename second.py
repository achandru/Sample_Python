
from datetime import datetime
from datetime import timedelta
import pandas as pd
import time

path_machineDias="/home/dalchemy/Mani/system2_6th.csv"
path=path_ioStat="/home/dalchemy/Updated_Sys2_Sec/io_stat_sec061217.csv"
df=pd.read_csv(path_machineDias)
df1 = pd.read_csv(path_ioStat, header=None, error_bad_lines=False)

"""
#abcd = df["datetime"]
col_df=df.columns.values
abcd = df["datime"]
col_df1=df1.columns.values

changed=[]

for i in abcd:
    if np.isnan(i):
	changed.append(ab)
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

"""
print "========================================================================================================="

#print df["changed"]
#print df1[1]
col_df=df.columns.values
col_df1=df1.columns.values
i_1=[]
j_1=[]


df1=df1.drop_duplicates(subset= 1, keep="first")
df1=df1[df1[2] == "sda"]
ans=pd.merge(df, df1, left_on='datime', right_on=1,how='inner')
ans.to_csv("ans.csv", sep=',')
"""
for i in range(0,len(df1[1])):
    for j in range(0,len(df["datime"])):
	try:
        	if str(df1[1][i])==str(df["datime"][j]):
           		i_1.append(i)
	   		j_1.append(j)
	   		print i,j
	except:
		pass

print len(i_1)
print len(j_1)
			
d=[]
e=[]
	
for x in range(0,len(i_1)):
	d.append(df1.loc[i_1[x]])
	e.append(df.loc[j_1[x]])

d1=pd.DataFrame(d)
e1=pd.DataFrame(e)
print d1[2]
#d1=d1.drop_duplicates(subset= d1[1], keep="first")
    
d1.to_csv("d1.csv", sep=',')
e1.to_csv("e1.csv", sep=',')

#f=pd.concat([d3,e3], axis=1)
#f.to_csv("f1.csv", sep=',')

