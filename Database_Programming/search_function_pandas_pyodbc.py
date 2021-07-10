## From SQL to DataFrame Pandas
import pandas as pd
import pyodbc
import pymssql

#sql_conn = pymssql.connect(server="DESKTOP-4TGCOMQ", DATABASE='Students',Trusted_Connection="yes")  # You can lookup the port number inside SQL server. 
#sql_conn = pymssql.connect(server="DESKTOP-4TGCOMQ")  # You can lookup the port number inside SQL server. 

sql_conn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=DESKTOP-4TGCOMQ;DATABASE=ISPA_test3;Trusted_Connection=yes') 
    
def findteacher(coursename):
    query = "SELECT [cid],[coursename],[teacher] FROM [ISPA_test3].[dbo].[courses] where coursename='"+ coursename + "'"
    dff = pd.read_sql(query, sql_conn)
    return dff

print('display only one row')

df=findteacher('Matlab')

print(df)