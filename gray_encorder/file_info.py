from pathlib import Path
import os


class FileInfo:
    OUTPUT_DIR_NAME = 'gray'

    def __init__(self, file_path: str) -> None:
        print(type(file_path))
        self.file_path = file_path
        self._path = Path(file_path)
        self.parent_dir = self._path.parent

    @property
    def file_name(self):
        return self._path.name

    def output_file_path(self, is_overwrite: bool) -> str:
        if is_overwrite:
            return self.file_path
        return os.path.join(self.parent_dir,
                            self.OUTPUT_DIR_NAME,
                            self.file_name)
