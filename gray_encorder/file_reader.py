from pathlib import Path
import os
from typing import List
from gray_encorder.file_info import FileInfo


class FileReader:
    PREFIXS = ('JPG', 'jpg', 'PNG', 'png', 'GIF', 'gif')

    def __init__(self, target) -> None:
        """ファイルを取得するためのクラスです。

        Args:
            target ([type]): 取得先パス
        """
        self.path = target

    @property
    def is_exists(self) -> bool:
        """パスが存在するか判定します。

        Returns:
            bool: パスが存在する場合`True`を返却します。
        """
        return os.path.exists(self.path)

    def is_image_file(self, filename: str) -> bool:
        """引数で指定したファイルが画像ファイルであるか判定します。
        画像ファイルかどうかは拡張子から確認します。

        Args:
            filename (str): 対象のファイル名

        Returns:
            bool: 画像ファイルだった場合`True`を返却。
        """
        if not filename:
            return False
        return filename.endswith(self.PREFIXS)

    def read(self, is_overwrite: bool) -> List[FileInfo]:
        """指定したパスがディレクトリだった場合、ディレクトリ以下の画像ファイルをリスト型式で返却します。
        指定したパスがファイルだった場合、ファイルパスをリストに含めて返却します。

        Args:
            is_overwrite (bool): 上書きフラグ

        Returns:
            List[FileInfo]: 対象の画像ファイル一覧
        """
        if Path.is_dir(Path(self.path)):
            return [FileInfo(os.path.join(self.path, f), is_overwrite)
                    for f in os.listdir(self.path)
                    if self.is_image_file(f)]

        if not self.is_image_file(Path(self.path).name):
            return []

        return [FileInfo(self.path,  is_overwrite)]
