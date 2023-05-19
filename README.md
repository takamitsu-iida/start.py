# start.py

Pythonスクリプトをゼロから書くときにクローンするプロジェクトです。

<br><br>

## 使い方

1. クローンします

`git clone https://github.com/takamitsu-iida/start.py.git`

2. 作成されたフォルダの名前を変えます

3. .gitフォルダを削除します

```
rm -rf .git
```

4. venvで仮想環境のフォルダを作ります

```
python3 -m venv .venv
```

5. direnv用の.envrcを作ります

```
cat - << EOS > .envrc
source .venv/bin/activate
unset PS1
EOS

direnv allow
```

6. 仮想環境のpipを最新化します

```
python -m pip install --upgrade pip
```

<br><br>

## pathlibへの変更 (2023年5月15日変更)

`os.path` を用いてこのように書いていたディレクトリへの参照はすべて`pathlib`に置き換えました。

> 参考：os.pathとPathの対応
>
> https://docs.python.org/ja/3/library/pathlib.html#correspondence-to-tools-in-the-os-module


```
# アプリケーションのホームディレクトリはこのファイルからみて一つ上
app_home = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# 自身の名前から拡張子を除いてプログラム名を得る
app_name = os.path.splitext(os.path.basename(__file__))[0]

# データ用ディレクトリ
data_dir = os.path.join(app_home, 'data')

# libフォルダにおいたpythonスクリプトをインポートできるようにするための処理
# このファイルの位置から一つ
lib_dir = os.path.join(app_home, 'lib')
```

<br><br>

## pylint

書式チェックツールはpylintを想定して、.pylintrcを同梱しています。
pylintをインストールしていない場合は、pipでインストールしてください。

```bash
pip install pylint [--proxy=http://name:pass@proxyaddr:8080]
```

.pylintrcは自動生成したものをベースに、ちょっとだけ書き換えています。

```bash
pylint --generate-rcfile > .pylintrc
```

<br><br>

## yapf

書式を自動整形したい場合にはyapfを使います。
特にスクリプトのインデントの数を2にするか、4にするか迷うときに、一括変換する場合に便利です。
Visual Studio Codeでは、右クリック→ドキュメントのフォーマット、で変換されます。

```bash
pip install yapf [--proxy=http://name:pass@proxyaddr:8080]
```

<br><br>

## Visual Studio Codeの設定

拡張機能の「Python」を導入することで、Pythonスクリプトの編集が楽になります。

<https://marketplace.visualstudio.com/items?itemName=donjayamanne.python>

ファイル→基本設定→設定、に以下の設定を加えることで、エディタの中でpylintとyapfが使えるようになります。

```js
  // python
  "python.linting.pylintEnabled": true,
  "python.formatting.provider": "yapf",
  "python.formatting.yapfPath": "yapf",
  "python.formatting.yapfArgs": [
    "--style={based_on_style: chromium, indent_width: 2, continuation_indent_width: 2, column_limit: 120}"
  ],
```

この設定では、Pythonスクリプトのインデントの数を2で指定していますので、
VS Codeで『ドキュメントのフォーマット』を実行すると、インデントは2に整形されます。

インデント数を変えたい時は上記設定を変更してフォーマットし直してください。

`lib`ディレクトリにライブラリを置いていますので、そこへの参照をvscodeに追加設定しないと不便です。

vscodeの設定画面で extra path を検索すると

```text
Python > Analysis: Extra Paths
```

という設定項目が出てきますので、「項目を追加」ボタンを押して

```text
lib/
```

を追加します。

環境変数 PYTHONPATH を使う方法もあります。この場合は `.envrc` で設定するとよいでしょう。

```
cat - << EOS >> .envrc

# PYTHONPATH
export PYTHONPATH=$PWD/lib:$PYTHONPATH

EOS
```

<br><br><br>

### 履歴

- 20230515 os.pathからpathlibに変更
- 20230504 .envrcを削除、インデント数を4に変更、ConfigParser()の利用を廃止
- 20221116 .envrcを追加
- 20190209 改行コードを全てLFに統一
- 20190209 SafeConfigParser()をConfigParser()に変更
- 20191228 ライブラリの雛形lib/main_lib.pyを追加
