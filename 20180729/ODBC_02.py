import csv as objCSV
import pypyodbc
import pandas as pd 

con = pypyodbc.connect('Driver={SQL Server};'

                                'Server=localhost;'

                                'Database=AdventureWorks2012_Data;'

                                'Trusted_Connection=yes;')


df = pd.read_sql("SELECT * from [dbo].[Project_Data]", con)

filename='myRecords.csv'
df.to_csv(filename, sep=',', encoding='utf-8')

print(df)

con.close()

