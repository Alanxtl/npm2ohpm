import os
import sys

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv('DEEPSEEK_API'), base_url="https://api.deepseek.com")

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print("Usage: python main.py convert <input_npm_package>", file=sys.stderr)
        print("Usage: python main.py json2json5 <input_json_file> <output_json5_file>", file=sys.stderr)
        print("Usage: python main.py ts2ets <input_ts_file> <output_ets_file>", file=sys.stderr)
        sys.exit(1)

    if sys.argv[1] == "convert":
        from src.parser import parse_package

        parse_package(sys.argv[2], client)

    if sys.argv[1] == "json2json5":
        from src.json2json5.json2json5 import convert_json_to_json5

        convert_json_to_json5(sys.argv[2], sys.argv[3])

    if sys.argv[1] == "ts2ets":
        from src.js2ets.ts2ets import convert_ts_to_ets

        convert_ts_to_ets(sys.argv[2], sys.argv[3], client)

