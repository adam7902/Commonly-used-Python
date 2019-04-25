# UTF-8

import os
import pandas as pd

csv_path = './csv_files'
csvs = [os.path.join(csv_path, file) for file in os.listdir(csv_path)]
fout = open("csv_merge.csv", "a")
for csv_file in csvs:
    for line in open(csv_file):
         fout.write(line)
fout.close()


df = pd.read_csv('csv_merge.csv')
print(df)








