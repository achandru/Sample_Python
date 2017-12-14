import json
import requests
import csv
import datetime,threading,time

def link():
 try:
  response = requests.get('https://api.enmetric.com/rest/v2/channels/livedata',auth=('ram@dalchemy.com', 'dalchemy@enm'))
 except Exception as Err:
    print "Unable to open the url"
    print Err

 try:
  data = json.loads(response.text)
  data1 = data['objects']
  return data1
 except Exception as Err:
    print "Unable to load the data"
    print Err
try:
 dat = open('Data.csv', 'w')
 csvwriter = csv.writer(dat)
 count = 0
 try:
  while count >= 0:
    for emp in link():
      if count == 0:
	 header = emp.keys()
         csvwriter.writerow(header)
	 count = count + 1
      csvwriter.writerow(emp.values())
      print emp.values()
      print datetime.datetime.now()
    count = count + 1
 except Exception as Err:
    print "Unable to abc"
    print Err
except Exception as Err:
    print "Unable to load abc1"
    print Err
dat.close()

