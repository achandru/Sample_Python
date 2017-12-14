'''
Created on Dec 5, 2017

@author: chance
'''
import datetime
import pandas as pd

path="/home/dalchemy/Anjali_IO/Mail/system2_01.csv"
dfToBe=pd.read_csv(path)

start=dfToBe["occurred_at"][0]
base=pd.datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
date_list = [base + datetime.timedelta(minutes=x) for x in range(0, 1440)]
for i in range(0,len(date_list)):
    date_list[i]=str(date_list[i])
df=pd.DataFrame(date_list,columns=["Time"])
ans= df.merge(dfToBe, left_on='Time', right_on='occurred_at', how='left')
if len(ans)>1440:
	ans = ans.drop(ans[ans.num_measurements>60].index)
p=path.split("/")
pp=""
for i in p:
    if i!=p[len(p)-1]:
        pp=pp+i+"/"
    else:
        pp=pp+"Merged_"+i
        
ans.to_csv(pp, sep=',')
