# UTF-8
#
import csv

with open('hrdata.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        print(row)

