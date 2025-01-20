import json5


def convert_json_to_json5(input_file, output_file) -> str:
    with open(input_file, 'r', encoding='utf-8') as json_file, open(output_file, 'w', encoding='utf-8') as json5_file:
        json5.dump(json5.load(json_file), json5_file, indent=2)

    return output_file
