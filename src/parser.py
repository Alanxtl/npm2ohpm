import os
from json2json5.json2json5 import convert_json_to_json5

def process_package_json(file_path):
    print(f'Processing {file_path}')
    convert_json_to_json5(file_path)

def parse_package(directory):
    for root, dirs, files in os.walk(directory):
        tar_root = root + "converted"
        for file in files:
            if file == 'package.json':
                full_path = os.path.join(root, file)
                tar_path = os.path.join(tar_root, file)
                process_package_json(full_path, tar_path)
            if file == 'package-lock.json':
                full_path = os.path.join(root, file)
                tar_path = os.path.join(tar_root, file)
                process_package_json(full_path, tar_path)

if __name__ == "__main__":
    # 从当前目录开始查找
    parse_package("C:\\Users\\Alan.lxt-redmi\\Desktop\\1")