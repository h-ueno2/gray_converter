import click


@click.command()
@click.option('--target_dir', help='対象のディレクトリ。ディレクトリかファイルのどちらかを必ず指定してください。')
@click.option('--target_file', help='変換対象ファイル。ディレクトリかファイルのどちらかを必ず指定してください。')
@click.option('--is_overwrite', default='0', help='1を指定した時、ファイルを上書きします。')
def cli(target_dir, target_file):
    if not (target_dir and target_file):
        print("--target_dirもしくは--target_fileを指定して下さい。")
        return
    print("bb")
