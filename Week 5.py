import os

def modify(input_filename, output_filename):
    """
    Reads an input file, modifies each line, and writes the modified lines to a new file.
    Handles errors if the input file doesn't exist or can't be read.

    Args:
        input_filename (str): The name of the file to read from.
        output_filename (str): The name of the file to write to.
    """
    try:
        # Attempt to open the input file in read mode ('r')
        with open(input_filename, 'r') as infile:
            # Attempt to open the output file in write mode ('w')
            with open(output_filename, 'w') as outfile:
                # Read and process each line from the input file
                for line in infile:
                    # Modify the line (example: convert to uppercase and add " (Processed)")
                    modified_line = line.strip().upper() + " (Processed)\n"
                    # Write the modified line to the output file
                    outfile.write(modified_line)
                print(f"Successfully processed '{input_filename}' and wrote to '{output_filename}' 🎉")

    # Handle the specific case where the input file does not exist
    except FileNotFoundError:
        print(f"Error: The input file '{input_filename}' was not found. Please make sure the file exists and the name is correct. 🧪")
    # Handle more general input/output errors (e.g., file permissions issues)
    except IOError as e:
        print(f"Error: An error occurred while reading or writing the file: {e} 🧪")
    # Handle any other unexpected exceptions
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e} 🧪")

def main():
    """
    Main function to get user input and call the file processing function.
    """
    while True:
        input_file = input("Enter the name of the input file (or 'exit' to quit): ")
        if input_file.lower() == 'exit':
            print("EXITING")
            break

        output_file = input("Enter the name of the output file: ")
        modify(input_file, output_file)

if __name__ == "__main__":
    main()
