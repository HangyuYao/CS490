#!/usr/bin/env python3
def create_new_file(filename):
    # Check if the filename has an extension
    if '.' in filename:
        output_filename = filename.split('.')[0] + '_Neg.bed'
    else:
        output_filename = filename + '_Neg.bed'

    try:
        with open(filename, 'r') as file, open(output_filename, 'w') as output_file:
            for line in file:
                parts = line.strip().split('\t')
                
                # Check if the line has the expected format
                if len(parts) >= 3:
                    first_char = parts[0]
                    start_string = parts[2]
                    next_line = next(file, None)
                    start_number = int(start_string) + 1

                    if next_line is not None:
                        next_parts = next_line.strip().split('\t')
                        if len(next_parts) >= 2:
                            end_string = next_parts[1]
                            end_number = int(end_string) - 1

                            if end_number <= start_number:
                                continue
                            output_file.write(first_char + '\t' + str(start_number) + '\t' + str(end_number) + '\n')
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    filename = input("Enter the filename: ")
    create_new_file(filename)
    print("File created.")

if __name__ == "__main__":
    main()
