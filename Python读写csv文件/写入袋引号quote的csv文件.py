# UTF-8
import csv
import pandas as pd

person = [['SN', 'Person', 'DOB'],
['1', 'John', '18/1/1997'],
['2', 'Marie', '19/2/1998'],
['3', 'Simon', '20/3/1999'],
['4', 'Erik', '21/4/2000'],
['5', 'Ana', '22/5/2001']]

# 通过使用csv模块的csv.register_dialect()类注册新的方言，我们可以用引号编写csv文件。
csv.register_dialect('myDialect', quoting=csv.QUOTE_ALL, skipinitialspace=True)

with open('person1.csv', 'w') as f:
    writer = csv.writer(f, dialect='myDialect')
    for row in person:
        writer.writerow(row)

f.close()

df = pd.read_csv('person1.csv')
print(df)
print('-----------------------------------')
print('\n')



