# this is how we write to a file

import csv

filename='University_Records.csv'

with open(filename,'r')as fn:
    csvReader=csv.reader(fn)
    fields=next(csvReader)
    
    rows=[]
    for row in csvReader:
        rows.append(row)   

print(fields)
print(rows)
