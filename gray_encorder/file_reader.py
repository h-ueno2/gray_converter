from pathlib import Path
import os
from typing import List
from gray_encorder.file_info import FileInfo


class FileReader:
    PREFIXS = ('JPG', 'jpg', 'PNG', 'png', 'GIF', 'gif')

    def __init__(self, target) -> None:
        self.path = target

    @property
    def is_exists(self) -> bool:
        return os.path.exists(self.path)

    def is_image_file(self, filename: str) -> bool:
        if not filename:
            return False
        return filename.endswith(self.PREFIXS)

    def read(self) -> List[FileInfo]:
        if Path.is_dir(Path(self.path)):
            return [FileInfo(os.path.join(self.path, f))
                    for f in os.listdir(self.path)
                    if self.is_image_file(f)]

        if not self.is_image_file(Path(self.path).name):
            return []

        return [FileInfo(self.path)]
