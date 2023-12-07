import argparse

def filter_keywords(input_file, output_file, keywords):
    with open(input_file, "r", encoding="ISO-8859-1") as file:
        lines = file.readlines()

    filtered_lines = [line for line in lines if any(keyword in line.lower() for keyword in keywords)]

    with open(output_file, "w", encoding="ISO-8859-1") as file:
        file.writelines(filtered_lines)

    print(f"包含关键词的行已保存到 {output_file} 文件中。")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Filter lines containing specific keywords.")
    parser.add_argument("input_file", help="Input file path")
    parser.add_argument("output_file", help="Output file path")

    # 定义关键词
    keywords = ["memory", "alloc", "free", "oom"]

    args = parser.parse_args()

    filter_keywords(args.input_file, args.output_file, keywords)
