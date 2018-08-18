# this is how we write to a file

import csv

filename='University_Records.csv'

with open(filename,'r')as fn:
    csvReader=csv.DictReader(fn)

    for row in csvReader:
        print(row['Name'] + ' ' + row['Branch'] + ' ' + row['Year'] + ' ' + row['CGPA'])
