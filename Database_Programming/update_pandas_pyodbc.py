import pyodbc

connStr = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=DESKTOP-XYZ;DATABASE=ISPA_test3;Trusted_Connection=yes')
cursor = connStr.cursor()

cursor.execute("Update dbo.courses set coursename=? where cid=? and teacher=?", 'Mathematical Physics', '7' ,'saleem' ) 
connStr.commit()
cursor.close()
connStr.close()
