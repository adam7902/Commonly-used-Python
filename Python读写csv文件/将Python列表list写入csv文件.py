# UTF-8
import csv
import pandas as pd

csvData = [['Person', 'Age'], ['Peter', '22'], ['Jasmine', '21'], ['Sam', '24']]
# 如果没有特别说明，列表的第一个元素列表默认作为列名称
with open('person.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvData)

csvFile.close()

df = pd.read_csv('person.csv')
print(df)

