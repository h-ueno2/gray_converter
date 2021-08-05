from gray_encorder.file_info import FileInfo
import cv2
import os
from typing import List, Any


class GrayEncorder:

    def __init__(self, imgs: List[FileInfo]) -> None:
        """画像をグレースケールに変換する処理クラスです。

        Args:
            imgs (list[str]): GrayScale対象の画像一覧
        """
        self.imgs = imgs

    def exec(self) -> None:
        """グレースケールの変換処理を行います。
        """
        for img in self.imgs:
            gray = self._encode(img.file_path)

            if not os.path.exists(img.output_dir_path):
                os.mkdir(img.output_dir_path)
            cv2.imwrite(img.output_file_path, gray)

    def _encode(self, file_path: str) -> Any:
        img = cv2.imread(file_path)
        return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
