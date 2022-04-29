import MySQLdb

db=MySQLdb.connect("localhost","root","","activitydb1")

cursor=db.cursor()

print("connection success")
