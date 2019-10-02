# UTF-8
# https://thepythonguru.com/python-how-to-read-and-write-csv-files/
import csv

header = ['id', 'name', 'address', 'zip']
rows = [
    [1, 'Hannah', '4891 Blackwell Street, Anchorage, Alaska', 99503],
    [2, 'Walton', '4223 Half and Half Drive, Lemoore, California', 97401],
    [3, 'Sam', '3952 Little Street, Akron, Ohio', 93704],
    [4, 'Chris', '3192 Flinderation Road, Arlington Heights, Illinois', 62677],
    [5, 'Doug', '3236 Walkers Ridge Way, Burr Ridge', 61257],
]

# 单行写入
with open('customers.csv', 'wt') as f:
    csv_writer = csv.writer(f)

    csv_writer.writerow(header)  # write header

    for row in rows:
        csv_writer.writerow(row)
print(' write ok ...')


# 多行写入
with open('customers2.csv', 'wt') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(header)  # write header
    csv_writer.writerows(rows)
print(' write ok ...')


with open('customers.csv', 'rt') as f:
    csv_reader = csv.DictReader(f)

    for row in csv_reader:
        print(row)


