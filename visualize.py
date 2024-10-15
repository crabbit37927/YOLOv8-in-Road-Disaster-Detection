import os
from pathlib import Path
from ultralytics import YOLO

# 设置路径
model_path = './src/yolo/runs/weights/best.pt'
val_images_path = './src/processed_data/val'
output_path = './src/yolo/predict'

# 创建预测结果保存的文件夹
Path(output_path).mkdir(parents=True, exist_ok=True)

# 加载模型
model = YOLO(model_path)

# 选择jpg文件
image_files = [f for f in os.listdir(val_images_path) if f.endswith('.jpg')]

# 执行预测并保存结果
for image_file in image_files:
    image_path = os.path.join(val_images_path, image_file)

    # 进行预测，将所有结果保存到同一个文件夹下
    results = model.predict(source=image_path, save=True, save_txt=True, save_conf=True, project=output_path,
                            exist_ok=True, name='')

print(f"预测完成，结果已保存至: {output_path}")
