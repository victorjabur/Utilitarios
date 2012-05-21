import pymssql
conn = pymssql.connect(host='host', user='user', password='pass', database='bd')
cur = conn.cursor()
cur.execute("SELECT @@VERSION")
row = cur.fetchone()
print row[0]
conn.close()
