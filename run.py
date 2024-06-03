import sys
import os


def get_file_path(argv):
    """Extracts the file path from command line arguments."""
    return argv[0]


def build_cpp(file_path):
    """Builds and executes C++ file."""
    if file_path.endswith(".cpp"):
        directory, filename = os.path.split(file_path)
        print(">>>> BUILDING ", filename)
        os.system(f"g++ {file_path} -o {directory}/{filename[:-4]}.exe")
        executable_path = os.path.join(directory, filename[:-4] + ".exe")
        print(">>>> EXECUTING ", executable_path)
        os.system(executable_path)


def run_python(file_path):
    """Runs Python file."""
    if file_path.endswith(".py"):
        directory, filename = os.path.split(file_path)
        print(">>>> RUNNING ", filename)
        os.system(f"python {file_path}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)

    sys.argv
    file_path = get_file_path(sys.argv[1:])
    build_cpp(file_path)
    run_python(file_path)
