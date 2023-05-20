#!/usr/bin/env python
"""pythonスクリプト

依存ライブラリ
  pylint
  yapf

Note:
  依存ライブラリの一括インストール
  pip install -r requirements.txt [--proxy=http://user:pass@proxy-addr:8080]

Example:
  $ python bin/main.py --dump
  Hello World
  Hello WorldHello World
  Hello,World
  Hello,WorldHello World
"""

__author__ = 'takamitsu-iida'
__version__ = '0.0'

__date__ = '2017/02/24'  # 初版
__date__ = '2018/02/24'  # python3専用に書き換え
__date__ = '2019/12/28'  # ライブラリ用にlib/main_lib.pyを追加
__date__ = '2023/03/23'  # シングルクオートに変更

#
# 標準ライブラリのインポート
#
import argparse
import logging
import sys
from pathlib import Path


# このファイルへのPathオブジェクト
app_path = Path(__file__)

# このファイルの名前から拡張子を除いてプログラム名を得る
app_name = app_path.stem

# アプリケーションのホームディレクトリはこのファイルからみて一つ上
app_home = app_path.parent.joinpath('..').resolve()

# データ用ディレクトリ
data_dir = app_home.joinpath('data')

# libフォルダにおいたpythonスクリプトをインポートできるようにするための処理
# このファイルの位置から一つ
lib_dir = app_home.joinpath('lib')
if not lib_dir in sys.path:
    sys.path.append(lib_dir)

#
# ログ設定
#

# ログファイルの名前
log_file = app_path.with_suffix('.log').name

# ログファイルを置くディレクトリ
log_dir = app_home.joinpath('log')
log_dir.mkdir(exist_ok=True)

# ログファイルのパス
log_path = log_dir.joinpath(log_file)

# ロギングの設定
# レベルはこの順で下にいくほど詳細になる
#   logging.CRITICAL
#   logging.ERROR
#   logging.WARNING --- 初期値はこのレベル
#   logging.INFO
#   logging.DEBUG
#
# ログの出力方法
# logger.debug('debugレベルのログメッセージ')
# logger.info('infoレベルのログメッセージ')
# logger.warning('warningレベルのログメッセージ')

# 独自にロガーを取得するか、もしくはルートロガーを設定する
# logging.basicConfig()

# ロガーを取得
logger = logging.getLogger(__name__)

# ログレベル設定
logger.setLevel(logging.INFO)

# フォーマット
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# 標準出力へのハンドラ
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setFormatter(formatter)
stdout_handler.setLevel(logging.INFO)
logger.addHandler(stdout_handler)

# ログファイルのハンドラ
file_handler = logging.FileHandler(log_path, 'a+')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.INFO)
logger.addHandler(file_handler)

#
# ここからスクリプト
#
if __name__ == '__main__':

    def dump():
        """画面表示します。

        printで長い出力をするときにはBrokenPipeErrorに気をつけます。
        パイプでlessにつなげるとBrokenPipeErrorが発生するのでそれを捕捉して標準エラー出力を閉じます。
        """
        try:
            # endを指定しない場合は'\n'がdefaultとなり出力の最後で改行される
            print('Hello World')  # -> Hello World\n

            # end引数に空文字を指定することで改行を防止できる
            print('Hello World', end='')  # -> Hello World

            # 引数には出力用データを複数指定可能
            # データの結合文字はsepで指定する。defaultは半角スペース
            print('Hello', 'World')  # -> aaa bbb\n

            # sepで結合文字を変更
            print('Hello', 'World', sep=',')  # -> Hello,World\n

            # sepとendは同時に設定可能
            print('Hello', 'World', sep=',', end='')  # -> Hello,World

            # fileで指定したファイルオブジェクトに出力できる
            print('Hello World', file=sys.stdout)
        except KeyboardInterrupt:
            pass
        except (BrokenPipeError, IOError):
            # lessにパイプしたときのBrokenPipeError: [Errno 32] Broken pipeを避ける
            sys.stderr.close()


    def main():
        """メイン関数

        Returns:
        int -- 正常終了は0、異常時はそれ以外を返却
        """

        # 引数処理
        parser = argparse.ArgumentParser(description='main script.')
        parser.add_argument('-c', '--create', action='store_true', default=False, help='Create')
        parser.add_argument('-f', '--filename', dest='filename', default='FILENAME', help='Filename')
        parser.add_argument('-d', '--dump', action='store_true', default=False, help='Dump')
        args = parser.parse_args()

        # フィルタで受け取りたい場合はこうする（↓）
        # parser.add_argument('-i', '--inline', type=argparse.FileType('r'), default=sys.stdin, help='read from file')
        # args = parser.parse_args(args=sys.argv[1:])
        # with args.inline as f:
        #   data = f.read()

        if args.dump:
            dump()
            logger.info('logger info test')
            logger.error('logger error test')

        # do something nice

        return 0

    # 実行
    sys.exit(main())
