import json
import requests
import csv

response = requests.get('https://api.enmetric.com/rest/v2/channels/livedata',auth=('ram@dalchemy.com', 'dalchemy@enm'))
data = json.loads(response.text)
data1 = data['objects']
print json.dumps(data1)	
#Outfile = open("foo.csv",'w')
#Outfile.write("power,status,occurredAt,channelGuid,voltage,current,frequency,powerFactor,brightness,temperature,sampleInterval,secondIndex"+"\n")
for data2 in data1:
  data3 = json.dumps(data2)
  data4 = str(data3).replace("{","")
  data5 = str(data4).replace("}","")
  data6 = str(data5).replace(",","")
  #data6 = str(data6).split(":")
  #data7 = "".join(data6)
  #data7 = str(data6).replace(":","")
  
  #Outfile.write(str(data6)+'\n')
  #Outfile.write(str(data2['power'])+','+str(data2['status'])+','+str(data2['occurredAt'])+','+str(data2['channelGuid'])+','+str(data2['voltage'])+','+str(data2['current'])+','+str(data2['frequency'])+','+str(data2['powerFactor'])+','+str(data2['brightness'])+','+str(data2['temperature'])+','+str(data2['sampleInterval'])+','+str(data2['secondIndex'])+'\n');
#Outfile.close()
  
