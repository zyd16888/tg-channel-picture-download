import os
import shutil
# 读取目录
read_dir = "images"

# 目录下的文件
file_list = os.listdir(read_dir)

# 遍历文件
for file in file_list:
    # 判断文件是否为正常照片
    if file.endswith(".jpg"):
        # 读取文件
        with open(os.path.join(read_dir, file), "rb") as f:
            # 读取文件内容
            content = f.read()
        # 判断文件内容是否为正常照片
        if content.startswith(b"\xff\xd8\xff\xe0\x00\x10JFIF"):
            # 如果是正常照片，不移动
            pass
        else:
            # 创建坏文件夹
            if not os.path.exists("bad"):
                os.mkdir("bad")
            # 如果不是正常照片，将其移动到坏目录
            shutil.move(os.path.join(read_dir, file), os.path.join("bad", file))
            print("move file: "+file)

