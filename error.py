def write_to_file(filename):
    try:
        with open(filename, 'a') as file:
            data = input("Enter text to write to the file: ")
            data=input("Enter additional text to append file: ")
            file.write(data + '\n')
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print("\nFinal content of the file:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

filename = "output.txt"
write_to_file(filename)
read_file(filename)
