from datetime import datetime
from datetime import timedelta
CurDate= datetime.now()

OutFile = open('/home/chandru/Automation/Enmetric/enmauto'+'_'+str(CurDate.month)+'_'+str(CurDate.day)+'_'+str(CurDate.year)+'_'+str(CurDate.hour)+'_'+str(CurDate.minute)+'.txt', 'w')
file = open("/home/chandru/Automation/myuser.txt","r")
contect = file.readlines()
for datas in contect:
     OutFile.write(datas)
