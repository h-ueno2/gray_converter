from pathlib import Path
import os


class FileInfo:
    OUTPUT_DIR_NAME = 'gray'

    def __init__(self, file_path: str) -> None:
        """このクラスは変換に必要となるファイル情報を保持するための物です。

        Args:
            file_path (str): 対象ファイルパス
        """
        self.file_path = file_path
        self._path = Path(file_path)
        self.parent_dir = self._path.parent

    @property
    def file_name(self) -> str:
        """パスを含まないファイル名を返却します。

        Returns:
            str: ファイル名
        """
        return self._path.name

    def output_file_path(self, is_overwrite: bool) -> str:
        """変換後ファイルの出力先パスを返却します。

        Args:
            is_overwrite (bool): 元ファイルを上書する場合は`True`を指定します。

        Returns:
            str: 変換後ファイルの出力先パス。
        """
        if is_overwrite:
            return self.file_path
        return os.path.join(self.parent_dir,
                            self.OUTPUT_DIR_NAME,
                            self.file_name)

    def output_dir_path(self, is_overwrite: bool) -> str:
        """変換後ファイルを出力するディレクトリのパスを返却します。

        Args:
            is_overwrite (bool): 元ファイルを上書する場合は`True`を指定します。

        Returns:
            str: 変換後ファイルを配置するディレクトリパス。
        """
        if is_overwrite:
            return self.parent_dir
        return os.path.join(self.parent_dir, self.OUTPUT_DIR_NAME)
