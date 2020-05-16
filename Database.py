import pandas as pd
import pymysql
import pandas as pd

host = "bigdatadb-1.cluster-clixocjfzzkz.us-east-1.rds.amazonaws.com"
port = 3306
dbname = "bigdatadb"
user = "admin"
password = "WSUBigData2019"

conn = pymysql.connect(host, user=user, port=port, passwd=password, db=dbname)
cursor = conn.cursor()
sql = "SELECT label.coarse, hips_motion.accel_x, hips_motion.accel_y, hips_motion.accel_z," \
      "hips_motion.gyros_x, hips_motion.gyros_y, hips_motion.gyros_z," \
      "hips_motion.magne_x, hips_motion.magne_y, hips_motion.magne_z " \
      "FROM label, hips_motion WHERE label.timest = hips_motion.timest"
cursor.execute(sql) #instroction here
result = cursor.fetchall()
#for row in result:
#    print(row)
newdata = pd.DataFrame(result)
newdata.to_csv("hips_train.csv")
conn.close()
#pd.read_sq('')
#print(conn.query("Select * From hips_motion"))
