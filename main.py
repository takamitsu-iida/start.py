#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
スクリプト全体のコメント

依存ライブラリ
　pylint
  yapf
  requests

依存ライブラリの一括インストール
  pip install -r requirements.txt [--proxy=http://user:pass@proxy-addr:8080]
"""

__author__ = "Name"
__version__ = "0.0"
__date__ = "2017/02/24"

#
# 標準ライブラリのインポート
#
import logging
import os
import sys

def here(path=''):
  """相対パスを絶対パスに変換して返却します"""
  return os.path.abspath(os.path.join(os.path.dirname(__file__), path))

# ./libフォルダにおいたpythonスクリプトをインポートできるようにするための処理
sys.path.append(here("./lib"))

# 独自の場所にsite-packagesを置いた場合は、その場所を指定します
sys.path.append(here("./lib/site-packages"))

#
# 外部ライブラリのインポート
#
try:
  import requests
  # HTTPSを使用した場合に、証明書関連の警告を無視する設定です
  requests.packages.urllib3.disable_warnings()
except ImportError:
  logging.error("requestsモジュールのインポートに失敗しました。")
  exit()

#
# ロギングの設定をします。
# レベルはこの順で下にいくほど詳細になります。
#   logging.CRITICAL
#   logging.ERROR
#   logging.WARNING --- 初期値はこのレベル
#   logging.INFO
#   logging.DEBUG
#
logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
handler.setLevel(logging.WARNING)
logger.setLevel(logging.WARNING)
logger.addHandler(handler)

# ログの出力方法
# logger.debug("debugレベルのログメッセージ")
# logger.info("infoレベルのログメッセージ")
# logger.warning("warningレベルのログメッセージ")

#
# ここからスクリプト
#

def main():
  """
  Hello Worldを出力する関数です。
  """

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


#
# 関数を実行
#

if __name__ == '__main__':
  main()
