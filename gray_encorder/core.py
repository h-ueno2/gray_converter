from gray_encorder.encorder import GrayEncorder
from gray_encorder.file_reader import FileReader
import click


@click.command()
@click.argument('target_path')
@click.option('--is_overwrite', default='0',
              help='1を指定した時、ファイルを上書きします。')
def cli(target_path, is_overwrite):
    if not target_path:
        print("対象のディレクトリまたはファイルを指定して下さい。")
        return
    is_overwrite = to_is_overwrite(is_overwrite)
    reader = FileReader(target_path)
    if not reader.is_exists:
        print("指定したパスに画像ファイルがありません。")
        return
    list = reader.read()
    encorder = GrayEncorder(list, is_overwrite)
    encorder.exec()


def to_is_overwrite(arg):
    if not arg:
        return False
    if arg == '1':
        return True
    return False
