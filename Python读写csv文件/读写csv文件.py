# UTF-8
# import necessary modules
# https://www.guru99.com/python-csv.html
import csv

# 写入数据
with open('writeData.csv', mode='w') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    # way to write to csv file
    writer.writerow(['Programming language', 'Designed by', 'Appeared', 'Extension'])
    writer.writerow(['Python', 'Guido van Rossum', '1991', '.py'])
    writer.writerow(['Java', 'James Gosling', '1995', '.java'])
    writer.writerow(['C++', 'Bjarne Stroustrup', '1985', '.cpp'])

print(' write over ...')


# 读取数据
reader = csv.DictReader(open("writeData.csv"))
for raw in reader:
    print(raw)
print('--------------------------------------')
print('\n')


# Read a CSV as a Dictionary
reader = csv.DictReader(open("writeData.csv"))
for raw in reader:
    print(raw)
print('--------------------------------------')
print('\n')


import pandas as pd
df = pd.read_csv("writeData.csv")
print(df)

