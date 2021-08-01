import pathlib
import os


class FileInfo:
    OUTPUT_DIR_NAME = 'gray'

    def __init__(self, file_path) -> None:
        self.file_path = pathlib.Path(file_path)
        self.parent_dir = self.file_path.parent

    @property
    def file_name(self):
        return self.file_path.name

    @property
    def output_file_path(self, is_overwrite):
        if is_overwrite:
            return self.file_path
        return os.path.join(self.parent_dir,
                            self.OUTPUT_DIR_NAME,
                            self.file_name)
