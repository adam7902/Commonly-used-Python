# UTF-8
import pandas
df = pandas.read_csv('hrdata.csv', index_col='Name', parse_dates=['Hire Date'])
print(df)
print('\n')
print(type(df['Hire Date'][0]))

print('-----------------------------------------------------------')
# 指定索引列，修改时间列有字符串转换为时间格式， 重新定义列名称
df2 = pandas.read_csv('hrdata.csv', index_col='Employee', parse_dates=['Hired'], header=0,
                      names=['Employee', 'Hired', 'Salary', 'Sick Days'])
print(df2)
df2.to_csv('hrdata_2.csv')

