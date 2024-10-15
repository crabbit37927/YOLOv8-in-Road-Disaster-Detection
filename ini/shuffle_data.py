import os
import random
import shutil
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 文件路径
image_folder = '../src/processed_data/image'
label_folder = '../src/processed_data/txt'
train_folder = '../src/processed_data/train'
val_folder = '../src/processed_data/val'

# 创建目标文件夹（如果不存在）
for folder in [train_folder, val_folder]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# 获取所有图片文件名（不含扩展名）
image_files = [f.split('.')[0] for f in os.listdir(image_folder) if f.endswith('.jpg')]

# 随机打乱文件顺序
random.shuffle(image_files)

# 划分数据集 9:1
split_index = int(0.9 * len(image_files))
train_files = image_files[:split_index]
val_files = image_files[split_index:]


# 复制文件到目标文件夹
def copy_files(file_list, target_folder):
    for file in file_list:
        # 复制图片文件
        src_image_path = os.path.join(image_folder, file + '.jpg')
        target_image_path = os.path.join(target_folder, file + '.jpg')
        shutil.copy(src_image_path, target_image_path)

        # 复制对应的标签文件
        src_label_path = os.path.join(label_folder, file + '.txt')
        target_label_path = os.path.join(target_folder, file + '.txt')
        if os.path.exists(src_label_path):
            shutil.copy(src_label_path, target_label_path)


# 复制训练集文件
copy_files(train_files, train_folder)

# 复制验证集文件
copy_files(val_files, val_folder)

logging.info(f"数据集已划分并保存到：\n训练集：{train_folder}\n验证集：{val_folder}")
