# UTF-8
# https://www.techbeamers.com/merge-multiple-csv-files/
import os
import pandas as pd

csv_header = 'Number, Square'
csv_out = 'consolidated.csv'

# csv_dir = os.getcwd()
csv_dir = './csv_files'
dir_tree = os.walk(csv_dir)
# print(dir_tree)
for dirpath, dirnames, filenames in dir_tree:
   pass

csv_list = []
for file in filenames:
   if file.endswith('.csv'):
      csv_list.append(file)

csv_merge = open(csv_out, 'w')
csv_merge.write(csv_header)
csv_merge.write('\n')

for file in csv_list:
   csv_in = open(os.path.join(csv_dir, file))
   for line in csv_in:
      if line.startswith(csv_header):
         continue
      csv_merge.write(line)
   csv_in.close()
csv_merge.close()
print('Verify consolidated CSV file : ' + csv_out)


df = pd.read_csv('consolidated.csv')
print(df)








