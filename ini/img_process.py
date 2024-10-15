import os
import cv2
import shutil
import logging
import tqdm

# 设置日志输出格式
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 文件路径
image_folder = r'../src/original_data/train/images'
output_folder = r'../src/processed_data/image'

# 检查并创建输出文件夹
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
else:
    # 清理并重新创建文件夹（如果需要清空旧的处理结果）
    shutil.rmtree(output_folder)
    os.makedirs(output_folder)

# 读取images文件夹下的所有图片
for filename in tqdm.tqdm(os.listdir(image_folder), desc='Processing images', unit='image', ncols=100):
    if filename.endswith('.jpg') or filename.endswith('.png'):  # 根据图像格式选择
        img_path = os.path.join(image_folder, filename)
        img = cv2.imread(img_path)

        # 双向滤波算法
        processed_img = cv2.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)

        # 保存处理后的图片
        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, processed_img)

logging.info("所有图片已处理并保存到: %s", output_folder)

