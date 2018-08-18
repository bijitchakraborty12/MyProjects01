# this is how we write to a file

import csv

fields=['Name','Branch','Year','CGPA']
rows=[['Nikhil','COE','2','9.0'],['Aditya','IT','2','9.3']]

filename='University_Records.csv'

with open(filename,'w+', newline='')as fn:
    csvWriter=csv.writer(fn)
    csvWriter.writerow(fields)
    csvWriter.writerows(rows)

