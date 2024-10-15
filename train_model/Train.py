from ultralytics import YOLO
import os
import logging
import shutil
import torch

# 读取YAML文件路径
yaml_file = '../src/yolo/dataset.yaml'
yolo_dir = '../src/yolo'
model_save_dir = '../src/yolo/models'
pre_weight_path = '../src/yolo/yolov8n.pt'

# 检查模型是否存在，如果不存在则下载并保存到指定路径
if not os.path.exists(pre_weight_path):
    logging.info(f"模型文件不存在，正在下载预训练模型到默认路径...")
    model = YOLO('yolov8n.pt')
    default_weight_path = 'yolov8n.pt'
    shutil.move(default_weight_path, pre_weight_path)
    logging.info(f"模型下载完成，保存路径为 {pre_weight_path}...")
else:
    model = YOLO(pre_weight_path)

if __name__ == '__main__':
    torch.cuda.empty_cache()
    # 开始训练模型
    model.train(
        data=yaml_file,  # 数据集的yaml文件
        epochs=450,
        batch=16,
        imgsz=640,       # 图片尺寸
        workers=16,       # 工作线程数
        device='cuda',
        name='runs',  # 训练模型的名称
        project=yolo_dir,  # 项目保存路径
        save_period=5,   # 每隔多少个epoch保存一次权重
        save=True,        # 保存最后的模型权重
    )

    logging.info("模型训练完成")
