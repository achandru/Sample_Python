from datetime import datetime
from datetime import timedelta
import time
CurDate= datetime.now()

OutFile = open('/home/dalchemy/Automation/Enmetric/enmauto'+'_'+str(CurDate.month)+'_'+str(CurDate.day)+'_'+str(CurDate.year)+'_'+str(CurDate.hour)+'_'+str(CurDate.minute)+'.txt', 'w')
X = 0
print CurDate

dt = datetime.combine(date.today(), CurDate) + timedelta(minutes=5)
print dt

for j in range(2):
    file = open("/home/dalchemy/Automation/myuser.csv","r")
    abc = file.read()
    X= X+1
   
file = open("/home/dalchemy/Automation/myuser.csv","r")
contect = file.readlines()

for i in range(2):
   for datas in contect:
     OutFile.write(datas)
     i= i+1
OutFile.close()
