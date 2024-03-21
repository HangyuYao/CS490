#!/usr/bin/env python3

import math
import os

# Function to prompt the user for the file name and read the file
def read_file_content():
    filename = input("Enter the file name to be read: ")
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
    # Count the letters in each line excluding lines that start with '>'
    letter_counts = [count_letters(line) for line in lines if not line.startswith('>')]
    
    # Calculate the total and the average count of letters (rounded up)
    total_letter_count = sum(letter_counts)
    average_letter_count = math.ceil(total_letter_count / len(letter_counts))
    print(average_letter_count)
    # Process the lines according to the letter count
    processed_lines = []
    header_line = None
    for line in lines:
        if line.startswith('>'):
            # Include header lines in the output
            header_line = line
        else:
            # Count the letters in this line
            line_letter_count = count_letters(line)
            if line_letter_count >= average_letter_count:
                # Cut the line down to the average letter count
                if header_line:
                    processed_lines.append(header_line)
                    header_line = None  # Reset the header line
                processed_lines.append(line)
            # Lines below the average count are omitted
    return processed_lines

# Ask the user for the input file name
lines = read_file_content()

if lines:
    # Process the lines
    processed_content = process_lines(lines)
    
    # Get the name for the output file
    output_filename = input("Enter the file name for the output: ")
    output_file_path = os.path.join('/users/Hangyu/data', f"{output_filename}.txt")
    
    # Write the processed lines to the new text file
    with open(output_file_path, 'w') as output_file:
        for processed_line in processed_content:
            output_file.write(f"{processed_line}\n")
    print(f"Processed file saved as {output_file_path}")
