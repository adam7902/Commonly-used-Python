# UTF-8
# https://jdhao.github.io/2018/05/13/read-write-csv-file-with-header/
import csv
import pandas as pd


lines = [['Bob', 'male', '27'],
         ['Smith', 'male', '26'],
         ['Alice', 'female', '26']]

header = ['name', 'gender', 'age']


# 写入文件
with open("testfile.csv", "w", newline='') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(header) # write the header
    # write the actual content line by line
    for l in lines:
        writer.writerow(l)
    # or we can write in a whole
    # writer.writerows(lines)
print(' csv file writed ok ...')


# csv读取文件
with open("testfile.csv", "r", newline='') as f:
    reader = csv.reader(f, delimiter=',')
    for l in reader:
        print(l)  # l will be a Python list
print('-------------------------------------------')

df = pd.read_csv('testfile.csv', delimiter=',')  # df is Pandas dataframe
print(df)
print('-------------------------------------------')


df2 = pd.read_csv("testfile.csv", delimiter=',', header=None)
print(df2)




