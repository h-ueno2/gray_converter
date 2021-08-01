from pathlib import Path
from typing import OrderedDict
import os
from file_info import FileInfo


class FileReader:
    PREFIXS = ('JPG', 'jpg', 'PNG', 'png', 'GIF', 'gif')

    def __init__(self, target) -> None:
        self.path = Path(target)

    @property
    def is_exists(self) -> bool:
        return os.path.exists(self.path)

    def is_image_file(self, filename: str) -> bool:
        return filename.endswith(self.PREFIXS)

    def read(self):
        if Path.is_dir(self.path):
            return [FileInfo(f)
                    for f in os.listdir(self.path)
                    if self.is_image_file(f)]

        if not self.is_image_file(self.path):
            return []

        return [FileInfo(self.path)]
