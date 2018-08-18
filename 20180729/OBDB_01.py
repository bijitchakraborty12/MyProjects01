import pypyodbc

con = pypyodbc.connect('Driver={SQL Server};'

                                'Server=localhost;'

                                'Database=AdventureWorks2012_Data;'

                                'Trusted_Connection=yes;')


cur=con.cursor()
cur.execute('select top 100 * from [dbo].[Orders]')

for row in cur:
    print('row = %r' % (row,)) #we need to write it as (row,) because, each row returned from the db table is a touple and NOT a single string. this is used to unpack the touple...


con.close()
