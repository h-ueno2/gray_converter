from gray_encorder.file_info import FileInfo
import cv2
import numpy as np


class GrayEncorder:

    def __init__(self, imgs: list[FileInfo], is_overwrite: bool) -> None:
        """画像をグレースケールに変換する処理クラスです。

        Args:
            imgs (list[str]): GrayScale対象の画像一覧
        """
        self.imgs = imgs
        self.is_overwrite = is_overwrite

    def exec(self):
        for img in self.imgs:
            gray = self._encode(img.file_path)
            cv2.imwrite(img.output_file_path(self.is_overwrite), gray)

    def _encode(self, img):
        return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
