import os

old_txt_path = '..\\txt_files'  # 存放多个单一txt文件的文件夹路径
store_path = '..\\new_txt_file'  # 指定合并后的txt文件存放路径
txt_files = [os.path.join(old_txt_path, file) for file in os.listdir(old_txt_path) if file.endswith('.txt')]
# txt_files 就是需要进行整合的多个txt文件列表
new_store_path = os.path.join(store_path, 'new_txt_file.txt')  
with open(new_store_path, 'w') as outfile:
	for fname in txt_files:
        with open(fname) as infile:
            outfile.write(infile.read())


