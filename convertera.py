import MySQLdb
from cassandra.cluster import Cluster


db = MySQLdb.connect("localhost","root","root","Enmetric" )
cursor = db.cursor()
cluster = Cluster(['localhost'])
session = cluster.connect('enmetric')

cursor.execute("select id,uid,password,account_id,(CASE WHEN (admin_priv = '\x01') THEN 1 ELSE 0 END) AS admin_priv,(CASE WHEN (admin_rules_enabled = '\x01') THEN 1 ELSE 0 END) AS admin_rules_enabled,password_reset_token,password_reset_token_created_at,(CASE WHEN (super_admin_priv = '\x01') THEN 1 ELSE 0 END) AS super_admin_priv,created, updated,guid,(CASE WHEN (enabled = '\x01') THEN 1 ELSE 0 END) AS enabled,secret_key,hashed_password,salt from user")
data = cursor.fetchall()
for row in data:	     
     #print row
     data = session.execute("Insert into user(id,uid,password,account_id,admin_priv,admin_rules_enabled,password_reset_token,password_reset_token_created_at,super_admin_priv,created, updated,guid,enabled,secret_key,hashed_password,salt) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )", [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15]])
      




