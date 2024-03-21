#!/usr/bin/env python3
import os

def read_file_content(filename):
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"No file found with the name {filename}")
        return None

def process_lines(lines, specified_value):
    processed_lines = []
    for line in lines:
        if line.startswith('>'):
            processed_lines.append(line)
        else:
            line_length = len(line.strip())
            if line_length > specified_value:
                processed_lines.append(line[:specified_value] + '\n')
            elif line_length < specified_value:
                continue
            else:
                processed_lines.append(line)
    return processed_lines

def main():
    file_specified_values = {
        'ENCFF986UZO_Neg.txt': 191,
        'ENCFF856GNF_Neg.txt': 205,
        'ENCFF402BMP_Neg.txt': 217,
        'ENCFF810SEM_Neg.txt': 225,
        'ENCFF735ILY_Neg.txt': 235,
        'ENCFF260PVK_Neg.txt': 197,
        'ENCFF041GGN_Neg.txt': 207,
        'ENCFF027BPY_Neg.txt': 221,
        'ENCFF928NLF_Neg.txt': 226,
        'ENCFF824LVP_Neg.txt': 251
    }

    for filename, specified_value in file_specified_values.items():
        lines = read_file_content(filename)
        if lines:
            processed_content = process_lines(lines, specified_value)
            output_filename = filename.split('.')[0] + '_neg.txt'
            output_file_path = os.path.join('/users/Hangyu/data', output_filename)

            with open(output_file_path, 'w') as output_file:
                for processed_line in processed_content:
                    output_file.write(processed_line)
            print(f"Processed file saved as {output_file_path}")

if __name__ == "__main__":
    main()
