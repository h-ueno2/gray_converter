from gray_encorder.file_info import FileInfo
import cv2
import os
from typing import List


class GrayEncorder:

    def __init__(self, imgs: List[FileInfo], is_overwrite: bool) -> None:
        """画像をグレースケールに変換する処理クラスです。

        Args:
            imgs (list[str]): GrayScale対象の画像一覧
        """
        self.imgs = imgs
        self.is_overwrite = is_overwrite

    def exec(self):
        for img in self.imgs:
            gray = self._encode(img.file_path)

            if not os.path.exists(img.output_dir_path(self.is_overwrite)):
                os.mkdir(img.output_dir_path(self.is_overwrite))
            cv2.imwrite(img.output_file_path(self.is_overwrite), gray)

    def _encode(self, file):
        img = cv2.imread(file)
        return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
