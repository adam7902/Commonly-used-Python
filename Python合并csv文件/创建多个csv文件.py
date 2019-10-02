# UTF-8
import csv


# 如果没有特别说明，列表的第一个元素列表默认作为列名称
for i in range(1, 15, 3):
    csvData = [['Number', 'Square'], [i, i*i], [i+1, (i+1)**2]]
    with open('./csv_files/{}.csv'.format(i), 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(csvData)
    print('{}.csv'.format(i), 'writed over')

    csvFile.close()













