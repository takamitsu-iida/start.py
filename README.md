# start.py

Pythonスクリプトをゼロから書くときにクローンするプロジェクトです。

## 使い方

1. クローンします

2. 作成されたフォルダの名前を変えます

3. .gitフォルダを削除します（使わないので）


## pylint

書式チェックツールはpylintを想定して、.pylintrcを同梱しています。
pylintをインストールしていない場合は、pipでインストールしてください。

```
pip install pylint [--proxy=http://name:pass@proxyaddr:8080]
```

.pylintrcは自動生成したものをベースに、ちょっとだけ書き換えています。

```
pylint --generate-rcfile > .pylintrc
```


## yapf

書式を自動整形したい場合にはyapfを使います。
特にスクリプトのインデントの数を2にするか、4にするか迷うときに、一括変換する場合に便利です。
Visual Studio Codeでは、右クリック→ドキュメントのフォーマット、で変換されます。

```
pip install yapf [--proxy=http://name:pass@proxyaddr:8080]
```


## Visual Studio Codeの設定

拡張機能の「Python」を導入することで、Pythonスクリプトの編集が楽になります。
https://marketplace.visualstudio.com/items?itemName=donjayamanne.python

ファイル→基本設定→設定、に以下の設定を加えることで、エディタの中でpylintとyapfが使えるようになります。。

```js
  // python
  "python.linting.pylintEnabled": true,
  "python.formatting.provider": "yapf",
  "python.formatting.yapfPath": "yapf",
  "python.formatting.yapfArgs": [
    "--style={based_on_style: chromium, indent_width: 4, continuation_indent_width: 4, column_limit: 120}"
  ],
```

この設定では、Pythonスクリプトのインデントの数を4で指定していますので、
VS Codeで『ドキュメントのフォーマット』を実行すると、インデントは4に整形されます。


# 初期スクリプト

Hello Worldを出力するだけでも、スクリプトとして完成させるとなると意外にいろいろ書かないといけないものです。
これを流用すると楽に書けます。

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
メインとなるスクリプトです。

使い方
py -3 main.py
"""

import logging
import os
import sys

# 通常はWARN
# 多めに情報を見たい場合はINFO
logging.basicConfig(level=logging.WARN)

def here(path=''):
  """相対パスを絶対パスに変換して返却します"""
  return os.path.abspath(os.path.join(os.path.dirname(__file__), path))

# ./libフォルダにおいたpythonスクリプトを読みこませるための処理
sys.path.append(here("./lib"))

# ./lib/site-packagesに外部ライブラリを置いたときに、それを読み込ませるための処理
sys.path.append(here("./lib/site-packages"))

###############################################################################

def main():
  """メイン関数"""

  # endを指定しない場合は"\n"がdefaultとなり出力の最後で改行される
  print("Hello") # -> aaa bbb\n

  # end引数に空文字を指定することで改行を防止できる
  print("aaa", end="") # -> aaa

  # 引数には出力用データを複数指定可能
  # データの結合文字はsepで指定する。defaultは半角スペース
  print("aaa", "bbb") # -> aaa bbb\n

  # sepで結合文字を変更
  print("aaa", "bbb", sep=",") # -> aaa,bbb\n

  # sepとendは同時に設定可能
  print("aaa", "bbb", sep=",", end="") # -> aaa,bbb

  # fileで指定したファイルオブジェクトに出力できる
  print("test", file=sys.stdout)


if __name__ == '__main__':
  main()

```
