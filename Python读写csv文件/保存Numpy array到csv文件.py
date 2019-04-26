# UTF-8
import numpy as np
import pandas as pd

arr = np.random.randint(1, 20, (5, 7))
print(arr)
print('-------------------------------------')


np.savetxt("saved_numpy_data.csv", arr, delimiter=",")
header = list('abcdefg')
print(header)
df = pd.read_csv("saved_numpy_data.csv", header=None)
# 如果文件中没有列名，则默认为0，否则设置为None。如果明确设定header=0 就会替换掉原来存在列名。
print(df)






