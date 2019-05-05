import pymysql

c = pymysql.connect(database='mysql', user='root')
cursor = c.cursor()
r = cursor.execute('select * from mysql.user where user = %s', ('和root',))
print('@@@@', r)
print(cursor.fetchall())
cursor.close()
c.close()

