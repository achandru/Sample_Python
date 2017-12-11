from datetime import datetime
from datetime import timedelta
import pandas as pd
import time

CurDate= datetime.now()

OutFile = open('/home/dalchemy/anjali'+'.csv', 'w')
df=pd.read_csv("/home/chandru/Anjali/MachineDiags-2.csv",)
df1 = pd.read_csv("/home/chandru/Anjali/io_stat_191117.csv", header=None)
abcd = df["occurred_at"]

changed=[]
OutFile.write("guid,power_avg,power_min,power_max,power_sum,num_measurements,occurred_at,channel_id,channel_number,node_id,node_hid,account_id, bridge_mac_addr,voltage_avg,current_avg,power_factor_avg,frequency_avg,status_avg,bridge_guid,node_guid,channel_guid,channel_profile_guid	device_type_guid,account_guid,user_guid,node_mac_addr,updated,created,id,device_type_name,date-time,device_type,rrqm/s,wrqm/s,r/s,w/s,rkB/s,wkB/s,avgrq-sz,avgqu-sz,await,r_await,w_await,svctm,%util"+'\n')

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

#print changed
for abc,abc1 in df.iterrows():
    print abc1["guid"]
#for changed1 in changed:
 #   for changed2 in df1[1]:
         #print changed1
         #print changed2
  #      if(str(changed1) == str(changed2)):
   #           print "abc"
            #OutFile.write(str(abc1["guid"]+'\n')#+","+str(df[1])+","+str(df[2])+","+str(df[3])+","+str(df[4])+","+str(df[5])+","+str(df[6])+","+str(df[7])+'\n')


#OutFile.write(str(Name[0].month)+'/'+str(Name[0].day)+'/'+str(Name[0].year) +","+str(Name[1])+","+str(Name[2])+","+str(Name[3])+","+str(Name[4])+","+str(Name[5])+","+str(Name[6])+","+str(Name[7])+","+str(Name[8])+","+str(Name[9])+'\n'+'\n')



