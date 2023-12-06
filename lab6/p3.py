import sys
import os


def calculate_dir_size(directory):
    total_size = 0
    try:
        print("Hi, this directory size is: ")
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Directory '{directory}' not found.")

        for filename in os.listdir(directory):
            try:
                file_path = os.path.join(directory, filename)
                total_size += os.path.getsize(file_path)

            except Exception as e:
                print("Error: ", e)
    except Exception as e:
        print("Error: ", e)

    print(total_size)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: py p3.py <directory_path>")
    else:
        directory_path = sys.argv[1]
        calculate_dir_size(directory_path)

