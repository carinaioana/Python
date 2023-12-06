import os
import sys


def count_files_by_extension(directory):
    try:
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Directory '{directory}' not found.")

        if not os.path.isdir(directory):
            raise NotADirectoryError(f"'{directory}' is not a directory.")

        files = os.listdir(directory)
        if not files:
            raise ValueError(f"Directory '{directory}' is empty.")

        extension_counts = {}

        for file in files:
            name, extension = os.path.splitext(file)
            if extension in extension_counts:
                extension_counts[extension] += 1
            else:
                extension_counts[extension] = 1

        print("File counts by extension:")
        for extension, count in extension_counts.items():
            print(f"{extension}: {count} files")

    except (FileNotFoundError, NotADirectoryError, ValueError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: py p4.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    count_files_by_extension(directory_path)