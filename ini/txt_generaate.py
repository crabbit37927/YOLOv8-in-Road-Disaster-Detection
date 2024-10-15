import os
import xml.etree.ElementTree as ET
import logging
from tqdm import tqdm

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 类别与ID的映射（需要根据实际情况调整）
class_mapping = {
    "D00": 0,
    "D01": 0,
    "D10": 1,
    "D11": 1,
    "D20": 2,
    "D40": 3,
    "D43": 3,
    "D44": 3,
    "Repair": 4,
}

# 文件路径
xml_folder = '../src/original_data/train/annotations/xmls'
output_folder = '../src/processed_data/txt'

# 检查并创建输出文件夹
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 读取xml文件夹中的所有xml文件
for xml_file in tqdm(os.listdir(xml_folder), desc='Converting XML to TXT', unit='files', ncols=100):
    if xml_file.endswith('.xml'):
        xml_path = os.path.join(xml_folder, xml_file)
        tree = ET.parse(xml_path)
        root = tree.getroot()

        # 获取图片尺寸
        size = root.find('size')
        width = int(size.find('width').text)
        height = int(size.find('height').text)

        # YOLO格式的txt文件名
        txt_file_name = xml_file.replace('.xml', '.txt')
        txt_path = os.path.join(output_folder, txt_file_name)

        with open(txt_path, 'w') as f:
            # 遍历所有的object节点
            for obj in root.findall('object'):
                class_name = obj.find('name').text
                if class_name not in class_mapping:
                    continue  # 跳过未定义的类别

                class_id = class_mapping[class_name]
                bndbox = obj.find('bndbox')
                xmin = int(bndbox.find('xmin').text)
                ymin = int(bndbox.find('ymin').text)
                xmax = int(bndbox.find('xmax').text)
                ymax = int(bndbox.find('ymax').text)

                # 计算中心点坐标和宽高，并归一化
                x_center = (xmin + xmax) / 2.0 / width
                y_center = (ymin + ymax) / 2.0 / height
                bbox_width = (xmax - xmin) / width
                bbox_height = (ymax - ymin) / height

                # 写入YOLO格式：class_id, x_center, y_center, bbox_width, bbox_height
                f.write(f"{class_id} {x_center:.6f} {y_center:.6f} {bbox_width:.6f} {bbox_height:.6f}\n")

logging.info(f"XML文件已成功转换为YOLOv8格式并保存到: {output_folder}")

