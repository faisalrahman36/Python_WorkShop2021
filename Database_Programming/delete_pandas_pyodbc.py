import pyodbc


connStr = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=DESKTOP-XYZ;DATABASE=ISPA_test3;Trusted_Connection=yes')
cursor = connStr.cursor()

cursor.execute("Delete dbo.courses where coursename=? and teacher=?", 'Urdu' ,'Ali' ) 
connStr.commit()
cursor.close()

cursor = connStr.cursor()

cursor.execute("Delete dbo.courses where cid=?", '9' ) 
connStr.commit()
cursor.close()