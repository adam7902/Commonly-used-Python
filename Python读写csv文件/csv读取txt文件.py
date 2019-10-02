# UTF-8
import csv


# Reading txt Files With csv
"""
name,department,birthday month
John Smith,Accounting,November
Erica Meyers,IT,March
"""
with open('employee_birthday.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    # print(list(csv_reader))
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')


"""
输出:
Column names are name, department, birthday month
	John Smith works in the Accounting department, and was born in November.
	Erica Meyers works in the IT department, and was born in March.
Processed 3 lines.
"""



