import pyodbc



connStr = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=DESKTOP-XYZ;DATABASE=ISPA_test3;Trusted_Connection=yes')
cursor = connStr.cursor()

cursor.execute("INSERT INTO dbo.courses([coursename],[teacher]) values  (?,?)", 'Matlab' ,'saleem' ) 
connStr.commit()
cursor.close()

'''
No we try to add more than one items in the table using list.

'''

coursename=['islamiat','pak studies']
teacher=['jawwad','noshaba']

cursor = connStr.cursor()

for x in range(0,len(teacher)):
    
 cursor.execute("INSERT INTO dbo.courses([coursename],[teacher]) values  (?,?)", coursename[x] ,teacher[x] ) 
 connStr.commit()
cursor.close()
connStr.close()