import argparse

def crop_lines(input_file, output_file, deleted_file, start_line, end_line):
    with open(input_file, 'r', encoding='ISO-8859-1') as file:
        lines = file.readlines()

    deleted_lines = lines[start_line-1:end_line]
    remaining_lines = lines[:start_line-1] + lines[end_line:]

    with open(output_file, 'w', encoding='ISO-8859-1') as file:
        file.writelines(remaining_lines)

    with open(deleted_file, 'w', encoding='ISO-8859-1') as file:
        file.writelines(deleted_lines)

    print(f"Cropped lines {start_line} to {end_line} from {input_file}.")
    print(f"Remaining content saved to {output_file}.")
    print(f"Deleted content saved to {deleted_file}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Crop lines from a file.")
    parser.add_argument("input_file", help="Input file path")
    parser.add_argument("output_file", help="Output file path for remaining content")
    parser.add_argument("deleted_file", help="Output file path for deleted content")
    parser.add_argument("start_line", type=int, help="Start line for cropping")
    parser.add_argument("end_line", type=int, help="End line for cropping")

    args = parser.parse_args()

    crop_lines(args.input_file, args.output_file, args.deleted_file, args.start_line, args.end_line)
