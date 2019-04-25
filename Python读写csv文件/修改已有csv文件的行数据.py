# UTF-8
# Modifying existing rows of people.csv
# https://www.programiz.com/python-programming/working-csv-files
import pandas as pd

df = pd.read_csv('people.txt', delimiter=',')
print(df)
df.to_csv('people.csv', index=0)
print('------------------------------------------')
print('\n')

import csv

row = ['2', ' Marie', ' California']
with open('people.csv', 'r') as readFile:
    reader = csv.reader(readFile)
    lines = list(reader)
    lines[2] = row

with open('people.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(lines)

readFile.close()
writeFile.close()

df2 = pd.read_csv('people.csv')
print(df2)


