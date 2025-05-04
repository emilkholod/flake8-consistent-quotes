import os


def get_absolute_path(filepath: str) -> str:
    return os.path.join(os.path.dirname(__file__), filepath)
