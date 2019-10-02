# UTF-8
import csv


"""
name,department,birthday month
John Smith,Accounting,November
Erica Meyers,IT,March
"""
# Reading CSV Files Into a Dictionary With csv
with open('employee_birthday.txt', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)  # csv to dictionary
    line_count = 0
    for row in csv_reader:
        print(row)
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')


"""
OrderedDict([('name', 'John Smith'), ('department', 'Accounting'), ('birthday month', 'November')])
Column names are name, department, birthday month
	John Smith works in the Accounting department, and was born in November.
OrderedDict([('name', 'Erica Meyers'), ('department', 'IT'), ('birthday month', 'March')])
	Erica Meyers works in the IT department, and was born in March.
Processed 3 lines.
"""


