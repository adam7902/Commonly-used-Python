# UTF-8
import csv
import pandas as pd

csvData = [['Fruit', 'Quantity'], ['Apple', '5'], ['Orange', '7'], ['Mango', '8']]

csv.register_dialect('myDialect', delimiter='|', lineterminator='\r\n\r\n')

with open('lineterminator.csv', 'w') as f:
    writer = csv.writer(f, dialect='myDialect')
    writer.writerows(csvData)

f.close()


df = pd.read_csv('lineterminator.csv', delimiter='|')
print(df)

