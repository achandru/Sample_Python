import MySQLdb
from cassandra.cluster import Cluster


db = MySQLdb.connect("localhost","root","root","Enmetric" )
cursor = db.cursor()
cluster = Cluster(['localhost'])
session = cluster.connect('enmetric')

cursor.execute("select * from node")
data = cursor.fetchall()
for row in data:
      data = session.execute("Insert into node  (id,account_id,name,description,type,mac_addr,hid,created,updated,guid,firmware_version,hardware_version,bridge_id,sample_interval,user_id,state) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" , [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15]])

