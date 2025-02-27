import argparse
import os
import sys

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv('API'), base_url=os.getenv('BASE_URL'))
model = os.getenv('MODEL')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A tool for converting files and packages.")
    subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)

    # Command: convert
    convert_parser = subparsers.add_parser("convert", help="Convert an npm package")
    convert_parser.add_argument("npm_package", type=str, help="Path to the input npm package")

    # Command: json2json5
    json2json5_parser = subparsers.add_parser("json2json5", help="Convert JSON to JSON5")
    json2json5_parser.add_argument("input_json_file", type=str, help="Path to the input JSON file")
    json2json5_parser.add_argument("output_json5_file", type=str, help="Path to the output JSON5 file")

    # Command: ts2ets
    ts2ets_parser = subparsers.add_parser("ts2ets", help="Convert TypeScript to ArkTs")
    ts2ets_parser.add_argument("input_ts_file", type=str, help="Path to the input TypeScript file")
    ts2ets_parser.add_argument("output_ets_file", type=str, help="Path to the output ArkTs file")

    # Command: js2ets
    js2ets_parser = subparsers.add_parser("js2ets", help="Convert JavaScript to ArkTs")
    js2ets_parser.add_argument("input_js_file", type=str, help="Path to the input JavaScript file")
    js2ets_parser.add_argument("output_ets_file", type=str, help="Path to the output ArkTs file")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    if args.command == "convert":
        from src.parser import parse_package

        src = args.input_npm_package

        if not os.path.exists(src):
            print(f"Error: {src} does not exist", file=sys.stderr)
            sys.exit(1)
        if not os.path.isdir(src):
            print(f"Error: {src} is not a directory", file=sys.stderr)
            sys.exit(1)
        if src.endswith("-converted"):
            print(f"Error: {src} is already a converted directory", file=sys.stderr)
            sys.exit(1)
        if src.endswith("\\"):
            src = src[:-1]
        if src.endswith("/"):
            src = src[:-1]
        if src.endswith("\\\\"):
            src = src[:-2]

        parse_package(src, client, model)

    elif args.command == "json2json5":
        from src.json2json5.json2json5 import convert_json_to_json5

        convert_json_to_json5(args.input_json_file, args.output_json5_file)

    elif args.command == "ts2ets":
        from src.js2ets.ts2ets import convert_ts_to_ets

        convert_ts_to_ets(args.input_ts_file, args.output_ets_file, client, model)

    elif args.command == "js2ets":
        from src.js2ets.js2ets import convert_js_to_ets

        convert_js_to_ets(args.input_js_file, args.output_ets_file, client, model)