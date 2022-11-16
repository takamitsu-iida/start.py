#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

__author__ = "takamitsu-iida"
__version__ = "0.0"

__date__ = "2017/02/24"  # 初版
__date__ = "2018/02/24"  # python3専用に書き換え
__date__ = "2019/12/28"  # ライブラリ用にlib/main_lib.pyを追加

#
# 標準ライブラリのインポート
#
import argparse
import configparser
import logging
import os
import sys


def here(path=''):
  """相対パスを絶対パスに変換して返却します"""
  return os.path.abspath(os.path.join(os.path.dirname(__file__), path))

# アプリケーションのホームディレクトリはこのファイルからみて一つ上
app_home = here("..")

# 自身の名前から拡張子を除いてプログラム名を得る
app_name = os.path.splitext(os.path.basename(__file__))[0]

# ディレクトリ
conf_dir = os.path.join(app_home, "conf")
data_dir = os.path.join(app_home, "data")


# libフォルダにおいたpythonスクリプトをインポートできるようにするための処理
# このファイルの位置から一つ
lib_dir = os.path.join(app_home, "lib")
if not lib_dir in sys.path:
  sys.path.append(lib_dir)

#
# 設定ファイルを読む
#
config_file = os.path.join(conf_dir, "config.ini")

if not os.path.exists(config_file):
  sys.exit("File not found:{}".format(config_file))

try:
  cp = configparser.ConfigParser()
  cp.read(config_file, encoding='utf8')

  # [default] セクション
  config = cp['default']
  USE_FILE_HANDLER = config.getboolean('USE_FILE_HANDLER', False)
  USERNAME = config.get('USERNAME', "admin")
  PASSWORD = config.get('PASSWORD', "password")

except configparser.Error as e:
  sys.exit(str(e))

#
# ログ設定
#

# ログファイルの名前
log_file = app_name + ".log"

# ログファイルを置くディレクトリ
log_dir = os.path.join(app_home, "log")
os.makedirs(log_dir, exist_ok=True)

# ロギングの設定
# レベルはこの順で下にいくほど詳細になる
#   logging.CRITICAL
#   logging.ERROR
#   logging.WARNING --- 初期値はこのレベル
#   logging.INFO
#   logging.DEBUG
#
# ログの出力方法
# logger.debug("debugレベルのログメッセージ")
# logger.info("infoレベルのログメッセージ")
# logger.warning("warningレベルのログメッセージ")

# default setting
logging.basicConfig()

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
if USE_FILE_HANDLER:
  file_handler = logging.FileHandler(os.path.join(log_dir, log_file), 'a+')
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
      # endを指定しない場合は"\n"がdefaultとなり出力の最後で改行される
      print("Hello World") # -> Hello World\n

      # end引数に空文字を指定することで改行を防止できる
      print("Hello World", end="") # -> Hello World

      # 引数には出力用データを複数指定可能
      # データの結合文字はsepで指定する。defaultは半角スペース
      print("Hello", "World") # -> aaa bbb\n

      # sepで結合文字を変更
      print("Hello", "World", sep=",") # -> Hello,World\n

      # sepとendは同時に設定可能
      print("Hello", "World", sep=",", end="") # -> Hello,World

      # fileで指定したファイルオブジェクトに出力できる
      print("Hello World", file=sys.stdout)
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
    parser.add_argument('-f', '--filename', dest='filename', metavar='file', default='FILENAME', help='Filename')
    parser.add_argument('-d', '--dump', action='store_true', default=False, help='Dump')
    args = parser.parse_args()

    # フィルタで受け取りたい場合はこうする（↓）
    # parser.add_argument('-i', '--inline', type=argparse.FileType('r'), default=sys.stdin, help='read from file')
    # args = parser.parse_args(args=sys.argv[1:])
    # with args.inline as f:
    #   data = f.read()

    if args.dump:
      dump()

    # do something nice

    return 0

  # 実行
  sys.exit(main())
