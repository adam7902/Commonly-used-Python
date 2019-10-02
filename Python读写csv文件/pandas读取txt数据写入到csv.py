# UTF-8
import pandas
df = pandas.read_csv('hrdata.txt', delimiter=',')
print(df)

print('\n')
df.to_csv('hrdata.csv', index=0)
print('csv saved ok ......')

