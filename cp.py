import sys
import os


def print_help():
    """Prints help message."""
    print(">>>> ENTER DIRECTORY AND NUMBER OF FILES AS ARGUMENTS")
    print(">>>> ex {foldername} + {no of files} + {extension of file}")


def create_files(folder_name: str, num_files: int, file_extension: str):
    """Creates files in the specified directory."""
    print(">>>> CREATING FOLDER WITH FILES")
    if folder_name in os.listdir():
        print(">>>> FOLDER ALREADY EXISTS")
    elif num_files > 26:
        print(">>>> TOO MANY FILES")
    elif num_files <= 0:
        print(">>>> CANNOT CREATE FOLDER WITH NO FILES")
    else:
        os.mkdir(folder_name)
        os.chdir(os.path.join(os.getcwd(), folder_name))
        for i in range(num_files):
            file_name = chr(ord("A") + i) + "." + file_extension
            with open(file_name, "w") as file:
                pass


if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) == 1 and args[0] == "help":
        print_help()
    elif len(args) != 3 or not args[1].isdigit():
        print(">>>> ENTER ARGUMENTS IN VALID FORMAT")
    else:
        folder_name, num_files, file_extension = args
        create_files(folder_name, int(num_files), file_extension)
