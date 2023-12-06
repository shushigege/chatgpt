import os

def combine_numbered_logs(log_prefix, output_file):
    # 获取以log_prefix为前缀的所有文件
    log_files = sorted([f for f in os.listdir() if f.startswith(log_prefix)])

    # 如果没有匹配的文件，给出提示并返回
    if not log_files:
        print(f"No files with prefix {log_prefix} found.")
        return

    with open(output_file, 'w', encoding='utf-8', errors='ignore') as output:
        for log_file in log_files:
            log_file_path = os.path.join(log_file)  # 修正这一行
            with open(log_file_path, 'r', encoding='utf-8', errors='ignore') as input_file:
                output.write(input_file.read())

    print(f"Logs combined and saved to {output_file}")

if __name__ == "__main__":
    log_prefix1 = 'logcatkernel.txt.'#文件的前缀
    log_prefix2 = 'logcatlog.txt.'
    output_file1 = 'D:/code/combined_logs_logcatkernel.log'
    output_file2 = 'D:/code/combined_logs_logcat.log'
    #output_file = 'path/to/combined_logs.txt'

    combine_numbered_logs(log_prefix1, output_file1)
    combine_numbered_logs(log_prefix2, output_file2)
