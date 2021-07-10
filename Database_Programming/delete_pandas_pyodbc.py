import pyodbc
#import pymssql

#connStr = pymssql.connect(server="DESKTOP-4TGCOMQ", DATABASE='Students',Trusted_Connection="yes")  # You can lookup the port number inside SQL server. 

#sql_conn = pymssql.connect(server="DESKTOP-4TGCOMQ")  # You can lookup the port number inside SQL server. 



connStr = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=DESKTOP-4TGCOMQ;DATABASE=ISPA_test3;Trusted_Connection=yes')
cursor = connStr.cursor()

cursor.execute("Delete dbo.courses where coursename=? and teacher=?", 'Urdu' ,'Ali' ) 
connStr.commit()
cursor.close()

cursor = connStr.cursor()

cursor.execute("Delete dbo.courses where cid=?", '9' ) 
connStr.commit()
cursor.close()