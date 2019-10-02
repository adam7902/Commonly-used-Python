# UTF-8
import csv
import pandas as pd


df = pd.read_csv('people1.csv')
print(df)
print('------------------------------------------')
print('\n')

row = ['4', ' Danny', ' New York']
with open('people1.csv', 'a') as csvFile:  # 'a'袋表追加写入文件， 'w'则是覆盖写入
    writer = csv.writer(csvFile)
    writer.writerow(row)

csvFile.close()

df2 = pd.read_csv('people1.csv')
print(df2)


