#移动文件
import os
import shutil
from config import settings

# 读取目录
read_dir = settings.read_dir
out_dir = settings.output_dir

# 目录下的文件
file_list = os.listdir(read_dir)

file_num = 0
folder_num = 1
for file in file_list:
    file_num += 1
    if not os.path.exists(f"{out_dir}_{folder_num}"):
        os.mkdir(f"{out_dir}_{folder_num}")
    shutil.move(os.path.join(read_dir, file), os.path.join(f"{out_dir}_{folder_num}", file))
    print(f"move file: {file} to {out_dir}_{folder_num}")
    if file_num % 1000 == 0:
        folder_num += 1