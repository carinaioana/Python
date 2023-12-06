import os
import sys


def rename_sequentially(directory):
    try:
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Directory '{directory}' not found.")
        counter = 1
        for filename in os.listdir(directory):
            try:
                ext = os.path.splitext(filename)[1]

                old_filepath = os.path.join(directory, filename)

                new_filename = "file" + "_" + str(counter) + ext
                new_filepath = os.path.join(directory, new_filename)

                os.rename(old_filepath, new_filepath)
                counter += 1
            except FileExistsError as e:
                print("A file with the same name exists already!")
            except OSError as e:
                print("Could not rename file:", filename, "Exception: ", e)
            except Exception as e:
                print("Error ", e)
    except Exception as e:
        print("Error: ", e)


def main():
    if len(sys.argv) != 2:
        print("Usage: python p2.py <directory_path>")
    else:
        directory_path = sys.argv[1]

        rename_sequentially(directory_path)


if __name__ == "__main__":
    main()
