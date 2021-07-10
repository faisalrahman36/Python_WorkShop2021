## From SQL to DataFrame Pandas
import pandas as pd
import pyodbc
import pymssql

#sql_conn = pymssql.connect(server="DESKTOP-4TGCOMQ", DATABASE='Students',Trusted_Connection="yes")  # You can lookup the port number inside SQL server. 

#sql_conn = pymssql.connect(server="DESKTOP-4TGCOMQ")  # You can lookup the port number inside SQL server. 

sql_conn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=DESKTOP-4TGCOMQ;DATABASE=ISPA_test3;Trusted_Connection=yes') 
query = "SELECT [cid],[coursename],[teacher] FROM [ISPA_test3].[dbo].[courses]"
df = pd.read_sql(query, sql_conn)

#print('display only one row')

print(df.head(1))

print(df.tail(2))
print('display all')
print(df)



