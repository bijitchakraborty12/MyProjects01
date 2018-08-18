import csv as objCSV
import pypyodbc

con = pypyodbc.connect('Driver={SQL Server};'

                                'Server=localhost;'

                                'Database=AdventureWorks2012_Data;'

                                'Trusted_Connection=yes;')


cur=con.cursor()
table=cur.execute('select top 100 * from [dbo].[Orders]')

heads=[x[0] for x in table.description]    

# for val in table.description:
#     print(val) #here, table.description contains the description of all the columns in the table, each description including the header, datatype information and the columns values...
filename='dbRecords.csv'
with open(filename,'w+',newline='') as fW:
    csvWriter=objCSV.writer(fW)
    csvWriter.writerow(heads)
    for val in table:
        csvWriter.writerow(val)

#print(heads)
print('done')

con.close()
