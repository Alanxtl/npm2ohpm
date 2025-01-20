import sys
import json5


def convert_json_to_json5(input_file, output_file) -> str:
    with open(input_file, 'r', encoding='utf-8') as json_file:
        with open(output_file, 'w', encoding='utf-8') as json5_file:
            json5.dump(json5.load(json_file), json5_file, indent=2)

    return output_file

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python json2json5.py <input_json_file> <output_json5_file>", file=sys.stderr)
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    json5_content = convert_json_to_json5(input_file, output_file)
    
    if json5_content:
        print(json5_content)