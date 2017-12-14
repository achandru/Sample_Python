from datetime import datetime
from datetime import timedelta
import pandas as pd
import time
CurDate= datetime.now()

df=pd.read_csv("/home/dalchemy/Enm_Auto/MachineDiags-2.csv")
df1 = pd.read_csv("/home/dalchemy/Anju/io_stat_191117.csv", header=None)
abcd = df["occurred_at"]

changed=[]

for i in abcd:
	conv=datetime.strptime(i,"%Y-%m-%d %H:%M:%S")

	if(conv.hour<9 and conv.minute<9):
		ab=str(conv.year)+str(conv.month)+str(conv.day)+str(str(conv.hour).zfill(2))+str(str(conv.minute).zfill(2))
	elif(conv.hour<9 and conv.minute>9):
		ab=str(conv.year)+str(conv.month)+str(conv.day)+str(str(conv.hour).zfill(2))+str(conv.minute)
	elif(conv.hour>9 and conv.minute<9):
		ab=str(conv.year)+str(conv.month)+str(conv.day)+str(conv.hour)+str(str(conv.minute).zfill(2))
	else:
		ab=str(conv.year)+str(conv.month)+str(conv.day)+str(conv.hour)+str(conv.minute)
        changed.append(ab)
df["changed"]=changed


print "========================================================================================================="

col_df=df.columns.values
col_df1=df1.columns.values
i_1=[]
j_1=[]
for i in range(0,len(df1[1])):
	for j in range(0,len(df["changed"])):
		if str(df1[1][i])==str(df["changed"][j]):
				i_1.append(i)
				j_1.append(j)

print len(i_1)
print len(j_1)
			
d=[]
e=[]		
for x in range(0,len(i_1)):
	d.append(df1.loc[i_1[x]])
	e.append(df.loc[j_1[x]])

d1=pd.DataFrame(d)
e1=pd.DataFrame(e)
d1.to_csv("d1", sep=',')
e1.to_csv("e1", sep=',')




#df4 = d1.append(e1, ignore_index=True, axis=axis)

#print df4

#result =  pd.merge(d1, e1(['guid','power_avg','power_min','power_max','power_sum','num_measurements','occurred_at','channel_id','channel_number','node_id','node_hid','account_id', 'bridge_mac_addr','voltage_avg','current_avg','power_factor_avg','frequency_avg','status_avg','bridge_guid','node_guid','channel_guid','channel_profile_guid','device_type_guid','account_guid','user_guid','node_mac_addr','updated','created','id','changed']), on = 'changed')
#print result 
#bigdata = pd.concat([e1, d1], axis=1)
#print bigdata

#df4.to_csv("abc", sep=',')
#print changed
'''
for abc,abc1 in df.iterrows():
    #print abc1["power_avg"]
    for changed1 in changed:
        for changed2 in df1[1]:
         #print changed1
         #print changed2
             if(str(changed1) == str(changed2)):
                OutFile.write(str(abc1["guid"])+'\n')#','+str(df1[1])+','+str(df1[2])+','+str(df1[3])+','+str(df1[4])+','+str(df1[5])+','+str(df1[6])+','+str(df1[7])+'\n')


#OutFile.write(str(Name[0].month)+'/'+str(Name[0].day)+'/'+str(Name[0].year) +","+str(Name[1])+","+str(Name[2])+","+str(Name[3])+","+str(Name[4])+","+str(Name[5])+","+str(Name[6])+","+str(Name[7])+","+str(Name[8])+","+str(Name[9])+'\n'+'\n')

'''

