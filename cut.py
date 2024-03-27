#!/usr/bin/env python3
import os

# List of files to be read
file_list = [
    'ENCFF986UZO.txt',
    'ENCFF856GNF.txt',
    'ENCFF402BMP.txt',
    'ENCFF810SEM.txt',
    'ENCFF735ILY.txt',
    'ENCFF260PVK.txt',
    'ENCFF041GGN.txt',
    'ENCFF027BPY.txt',
    'ENCFF928NLF.txt',
    'ENCFF824LVP.txt',
    'ENCFF986UZO_Neg.txt',
    'ENCFF856GNF_Neg.txt',
    'ENCFF402BMP_Neg.txt',
    'ENCFF810SEM_Neg.txt',
    'ENCFF735ILY_Neg.txt',
    'ENCFF260PVK_Neg.txt',
    'ENCFF041GGN_Neg.txt',
    'ENCFF027BPY_Neg.txt',
    'ENCFF928NLF_Neg.txt',
    'ENCFF824LVP_Neg.txt'
]

# Function to read the content of a file
def read_file_content(filename):
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"No file found with the name {filename}")
        return None

# Function to count the letters in a line
def count_letters(line):
    return len(line)

def process_lines(lines):
    # Fixed value for letter count
    fixed_letter_count = 200

    # Process the lines according to the letter count
    processed_lines = []
    header_line = None
    for line in lines:
        if line.startswith('>'):
            # Include header lines in the output
            header_line = None
        else:
            # Count the letters in this line
            line_letter_count = count_letters(line)
            if line_letter_count >= fixed_letter_count:
                if header_line:
                    processed_lines.append(header_line)
                    header_line = None  # Reset the header line
                # Trim the line to 200 characters
                processed_lines.append(line[:fixed_letter_count])
            # Lines below the fixed count are omitted
    return processed_lines

# Loop through each file in the list
for filename in file_list:
    # Read the content of the file
    lines = read_file_content(filename)

    if lines:
        # Process the lines
        processed_content = process_lines(lines)

        output_filename = filename
        # Make sure the output directory exists
        output_file_path = os.path.join('/users/Hangyu/data', output_filename)

        # Write the processed lines to the new text file
        with open(output_file_path, 'w') as output_file:
            for processed_line in processed_content:
                output_file.write(f"{processed_line}\n")
        print(f"Processed file saved as {output_file_path}")
