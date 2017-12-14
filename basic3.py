import json
import requests
import csv
import datetime,threading,time

response = requests.get('https://api.enmetric.com/rest/v2/channels/livedata',auth=('ram@dalchemy.com', 'dalchemy@enm'))
data = json.loads(response.text)
data1 = data['objects']	
dat = open('Data.csv', 'w')
csvwriter = csv.writer(dat)
count = 0

def enmetry():
  global count
  #threading.Timer(1.0, enmetry).start()  
  #while True:
  for emp in data1:
      if count == 0:
             header = emp.keys()
             csvwriter.writerow(header)
             count = count + 1
      csvwriter.writerow(emp.values())
      print emp.values()
      #time.sleep(0.1)
#for i in range(3):
 enmetry()
#time.sleep(0.1)
dat.close()

