import os


def format_line(line):
    """保留六位小数并修改第一个数字为3"""
    parts = line.split()
    if parts:
        parts[0] = '3'  # 修改第一个数字为3
        # 对其余的数字保留六位小数
        for i in range(1, len(parts)):
            parts[i] = f"{float(parts[i]):.6f}"
    return ' '.join(parts)


def process_files(add_data_folder, processed_data_folder):
    total_append_count = 0  # 统计追加不重复数据的次数

    # 遍历add_data文件夹中的所有txt文件
    for filename in os.listdir(add_data_folder):
        if filename.endswith('.txt'):
            add_data_file_path = os.path.join(add_data_folder, filename)

            # 读取add_data文件中的内容
            with open(add_data_file_path, 'r') as file:
                lines = file.readlines()

            # 修改每一行数据
            modified_lines = [format_line(line) for line in lines]

            # 寻找processed_data中同名的txt文件
            processed_data_file_path = os.path.join(processed_data_folder, filename)
            if os.path.exists(processed_data_file_path):
                # 读取已存在的内容
                with open(processed_data_file_path, 'r') as processed_file:
                    existing_lines = set(line.strip() for line in processed_file.readlines())

                # 追加不重复的数据并更新计数
                new_lines = [line for line in modified_lines if line not in existing_lines]

                with open(processed_data_file_path, 'a') as processed_file:
                    for new_line in new_lines:
                        processed_file.write(new_line + '\n')
                        total_append_count += 1  # 每追加一条不重复数据，计数+1

            else:
                # 如果同名文件不存在，创建新文件并写入修改后的内容
                with open(processed_data_file_path, 'w') as processed_file:
                    for modified_line in modified_lines:
                        processed_file.write(modified_line + '\n')
                        total_append_count += 1  # 计数所有新写入的数据

    # 打印总共追加不重复数据的次数
    print(f"Total number of non-duplicate data appended: {total_append_count}")


# 设置文件夹路径
add_data_folder = '../src/add_data'
processed_data_folder = '../src/processed_data/txt'

# 执行文件处理
process_files(add_data_folder, processed_data_folder)
