import os

# 定义文件保存路径
yaml_file_path = '../src/yolo/dataset.yaml'
train_path = r'D:/py_project/RDD/src/processed_data/train'
val_path = r'D:/py_project/RDD/src/processed_data/val'

# 定义YOLOv8数据集路径和类别信息
yaml_content = f"""
train: {train_path}
val: {val_path}

# 类别信息
names:
  0: 'Longitudinal Crack'
  1: 'Lateral Crack'
  2: 'Alligator Crack'
  3: 'pothole'
  4: 'Repaired'
"""

# 检查保存目录是否存在，如果不存在则创建
yaml_dir = os.path.dirname(yaml_file_path)
if not os.path.exists(yaml_dir):
    os.makedirs(yaml_dir)

# 将内容写入yaml文件
with open(yaml_file_path, 'w') as file:
    file.write(yaml_content)

print(f"YAML文件已保存到: {yaml_file_path}")
