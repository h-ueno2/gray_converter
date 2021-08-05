from gray_encorder.encorder import GrayEncorder
from gray_encorder.file_reader import FileReader
import click


@click.command()
@click.argument('target_path')
@click.option('--is_overwrite', default='0',
              help='1を指定した時、ファイルを上書きします。')
def cli(target_path: str, is_overwrite: str) -> None:
    """指定したパスの画像ファイルをグレースケールに変換します。

    Args:
        target_path (str): 対象パス
        is_overwrite (str): 元ファイルを上書きする場合、1を指定します。
        1以外の場合、同階層に`gray`ディレクトリを作成し、その下に変換後のファイルを配置します。
    """
    if not target_path:
        print("対象のディレクトリまたはファイルを指定して下さい。")
        return
    is_overwrite = to_is_overwrite(is_overwrite)
    reader = FileReader(target_path)
    if not reader.is_exists:
        print("指定したパスに画像ファイルがありません。")
        return
    list = reader.read(is_overwrite)
    encorder = GrayEncorder(list)
    encorder.exec()


def to_is_overwrite(arg: str) -> bool:
    """コマンドライン引数で指定された`is_overwrite`フラグをbool型に変換します。

    Args:
        arg (str): コマンドライン引数`is_overwrite`の値

    Returns:
        bool: 1の時`True`を返却。1以外の時は`False`を返却。
    """
    if not arg:
        return False
    if arg == '1':
        return True
    return False
