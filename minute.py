import MySQLdb
from cassandra.cluster import Cluster

db = MySQLdb.connect("localhost","root","root","Enmetric" )
cursor = db.cursor()
cluster = Cluster(['localhost'])
session = cluster.connect('enmetric')

cursor.execute("select IF(guid IS NULL,'NULL',guid) AS guid,power_avg,power_min,power_max,power_sum,num_measurements,occurred_at,channel_id,channel_number,node_id,node_hid,account_id, bridge_mac_addr,voltage_avg,current_avg,power_factor_avg,frequency_avg,status_avg,bridge_guid,node_guid,channel_guid,channel_profile_guid,device_type_guid,account_guid,user_guid,node_mac_addr,updated,created  from minute_measurement where occurred_at >= '2016-01-01 00:00:00' and occurred_at < '2016-01-01 00:01:00'")

data = cursor.fetchall()
#count = 0
#print len(data)

#for i in range(5):
for i,row in enumerate (data):
        print i,len(row)
        #count = count+1
        #print  count

        #data = session.execute("Insert into minute_measurement(id,guid,power_avg,power_min,power_max,power_sum,num_measurements,occurred_at,channel_id,channel_number,node_id,node_hid,account_id,bridge_mac_addr,voltage_avg,current_avg,power_factor_avg,frequency_avg,status_avg,bridge_guid,node_guid,channel_guid,channel_profile_guid,device_type_guid,account_guid,user_guid,node_mac_addr,updated,created)" + "values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s ,%s);", [int(count), row[0], row[1], row[2], row[3],row[4],row[5],row[6],row[7],row[8],row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18],row[19],row[20], row[21], row[22], row[23], row[24], row[25], row[26], row[27]])
           #session.execute(data) 








