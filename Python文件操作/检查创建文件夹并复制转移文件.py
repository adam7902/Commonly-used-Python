from shutil import copyfile
import time
import os

# 检查路径是否存在，不存在则创建新文件夹
def make_dir(dirs):
    if not os.path.exists(dirs):
        os.makedirs(dirs)
        
# 定义复制转移文件的函数
def move(src, dst):
    copyfile(src, dst)
    
root_path = '..\\image_list_path'  # 图片文件路径
target_path = '..\\new_image_list_path'

images = os.listdir(root_path)
for _, image in enumerate(images):
    if _%100 == 0:
        print(_, time.ctime())
    src_path = os.path.join(root_path, image)
    dst_path = os.path.join(target_path, image)
    try:
        image_ok = os.path.join(src_path, image)  # 判断图片文件是否存在异常
        # if os.path.exists(src_path):
        move(src_path, dst_path)
        # else:
        #     continue
    except OSError:  # 如果图片有问题直接跳过进行下一轮循环
        continue


