import os


def get_data_directory_path() -> str:
    # Get the directory of the current script.
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Join the path to the data directory.
    file_path = os.path.join(current_dir, "../data")

    return file_path


def read_file(filename: str) -> str:
    data_directory_path = get_data_directory_path()
    with open(f"{data_directory_path}/{filename}", "r", encoding="utf-8") as f:
        content = f.read()

    return content.strip()
