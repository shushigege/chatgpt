import argparse

def extract_text(input_file, output_file, prefix="------ KERNEL LOG (dmesg) ------", suffix="------ 0.048s was the duration of 'KERNEL LOG (dmesg)' ------"):
    with open(input_file, "r", encoding="ISO-8859-1") as file:
        lines = file.readlines()

    found = False
    text = ""
    output_lines = []

    for line in lines:
        if prefix in line:
            found = True
            text = ""
        if found:
            text += line
        if suffix in line:
            found = False
            output_lines.append(text)

    with open(output_file, "w", encoding="ISO-8859-1") as file:
        file.writelines(output_lines)

    print(f"提取的文本已保存到 {output_file} 文件中。")

def filter_keywords(input_file, keywords, output_file):
    with open(input_file, "r", encoding="ISO-8859-1") as file:
        lines = file.readlines()

    filtered_lines = [line for line in lines if any(keyword in line.lower() for keyword in keywords)]

    with open(output_file, "w", encoding="ISO-8859-1") as file:
        file.writelines(filtered_lines)

    print(f"包含关键词的行已保存到 {output_file} 文件中。")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract and filter text from a file.")
    parser.add_argument("input_file", help="Input file path")
    parser.add_argument("--output_file", default="output.txt", help="Output file path")

    args = parser.parse_args()

    extract_text(args.input_file, args.output_file)

    keywords = ["memory", "alloc", "free", "oom"]
    filter_keywords(args.output_file, keywords, "kernel_mem.txt")
