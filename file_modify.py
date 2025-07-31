def modify_file(input_filename, output_filename):
    """
    Reads content from input_filename, converts it to uppercase,
    and writes the result to output_filename.
    """
    try:
        with open(input_filename, 'r') as infile:
            content = infile.read()

        # Modify the content (convert to uppercase)
        modified_content = content.upper()

        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Modified content written to '{output_filename}'")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except IOError:
        print("Error: An error occurred while reading or writing files.")


if __name__ == "__main__":
    input_file = input("Enter the input filename: ")
    output_file = input("Enter the output filename: ")
    modify_file(input_file, output_file)
