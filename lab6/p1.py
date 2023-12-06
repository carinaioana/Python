from os import path, listdir
from sys import argv as argv


def read_files_in_directory(directory, file_extension):
    try:
        if not path.exists(directory):
            raise FileNotFoundError(f"Directory '{directory}' not found.")

        for filename in listdir(directory):
            if filename.endswith(file_extension):
                file_path = path.join(directory, filename)

                try:
                    with open(file_path, 'r') as file:
                        print(f"Contents of {filename}:")
                        print(file.read())
                except Exception as e:
                    print(f"Error reading file {filename}: {e}")
                file.close()

    except Exception as e:
        print(f"Error: {e}")


def main():
    if len(argv) != 3:
        print("Usage: python p1.py <directory_path> <file_extension>")
    else:
        directory_path = argv[1]
        file_extension = argv[2]

        read_files_in_directory(directory_path, file_extension)


if __name__ == "__main__":
    main()
