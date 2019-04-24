# https://stackoverflow.com/questions/33686747/save-a-list-to-a-txt-file
values = ['1', '2', '3']  # 新建一个测试列表

# 存储写入
with open("file.txt", "w") as output:
    output.write(str(values))
    print('列表存储完成......')

# 读取已经存储的文件
with open("file.txt") as f:
    s = [line for line in f.readlines()]
    print(s)
    print(eval(s[0]))
    print(type(eval(s[0])))

del "file.txt"
exit()


