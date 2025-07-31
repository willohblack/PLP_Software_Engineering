def read_user_file():
    """
    Prompts the user for a filename and attempts to read and print its contents.
    Handles errors if the file doesn't exist or can't be read.
    """
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("\nFile content:\n")
            print(content)
    except FileNotFoundError:
        print(f"Oops! The file '{filename}' does not exist.")
    except IOError:
        print(f"Sorry, the file '{filename}' cannot be read.")


if __name__ == "__main__":
    read_user_file()
