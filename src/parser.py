import os

from src.json2json5.json2json5 import convert_json_to_json5
from src.js2ets.ts2ets import convert_ts_to_ets

def process_package_json(input_file, output_file):
    print(f'Processing {input_file} to {output_file}')
    convert_json_to_json5(input_file, output_file)

def process_package_ts(input_file, output_file, client):
    print(f'Processing {input_file} to {output_file}')
    convert_ts_to_ets(input_file, output_file, client)

def parse_package(directory, client):
    for root, dirs, files in os.walk(directory):
        tar_root = directory + "-converted"
        relative_path = os.path.relpath(root, directory)

        for file in files:
            if file == 'package.json':
                full_path = os.path.join(root, file)
                tar_path = os.path.join(tar_root, relative_path, "oh-package.json5")
                os.makedirs(os.path.dirname(tar_path), exist_ok=True)
                process_package_json(full_path, tar_path)
            if file == 'package-lock.json':
                full_path = os.path.join(root, file)
                tar_path = os.path.join(tar_root, relative_path, "oh-package-lock.json5")
                os.makedirs(os.path.dirname(tar_path), exist_ok=True)
                process_package_json(full_path, tar_path)
            if file.endswith('.ts'):
                full_path = os.path.join(root, file)
                tar_path = os.path.join(tar_root, relative_path, file[:-3] + ".ets")
                os.makedirs(os.path.dirname(tar_path), exist_ok=True)
                process_package_ts(full_path, tar_path, client)
            else:
                full_path = os.path.join(root, file)
                tar_path = os.path.join(tar_root, relative_path, file)
                os.makedirs(os.path.dirname(tar_path), exist_ok=True)
                with open(full_path, 'rb') as fsrc, open(tar_path, 'wb') as fdst:
                    fdst.write(fsrc.read())

    print("Converted successfully, stored in " + os.path.join(tar_root))