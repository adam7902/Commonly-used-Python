# UTF-8
import numpy as np
import pandas as pd

arr = np.random.randint(1, 20, (5, 7))
print(arr)

arr_lis = [i.tolist() for i in arr]
df = pd.DataFrame(arr_lis)
print(df)
df.to_csv('csv_array.csv', index=0, header=None)
print('------------------------------------------')

my_array = np.loadtxt('csv_array.csv', delimiter=",", skiprows=1)
print(type(my_array))
print(my_array)












