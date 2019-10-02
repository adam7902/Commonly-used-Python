# UTF-8
import csv
import pandas as pd

person = [['SN', 'Person', 'DOB'],
['1', 'John', '18/1/1997'],
['2', 'Marie','19/2/1998'],
['3', 'Simon','20/3/1999'],
['4', 'Erik', '21/4/2000'],
['5', 'Ana', '22/5/2001']]

csv.register_dialect('myDialect', delimiter='|', quoting=csv.QUOTE_NONE, skipinitialspace=True)
with open('dob.csv', 'w') as f:
    writer = csv.writer(f, dialect='myDialect')
    for row in person:
        writer.writerow(row)

f.close()

df = pd.read_csv('dob.csv')
print(df)
print('-----------------------------------')
print('\n')

df = pd.read_csv('dob.csv', delimiter='|')
print(df)

