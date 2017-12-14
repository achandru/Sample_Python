import MySQLdb
from cassandra.cluster import Cluster


db = MySQLdb.connect("localhost","root","root","Enmetric" )
cursor = db.cursor()
cluster = Cluster(['localhost'])
session = cluster.connect('enmetric')

cursor.execute("select * from account")
data = cursor.fetchall()
for row in data:
	data = session.execute("Insert into account (id,name,created,updated,guid,enabled,default_device_type_id,api_key,synced) values (%s, %s, %s, %s, %s, %s, %s, %s, %s )", [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]])
      
