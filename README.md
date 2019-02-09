# start.py

Pythonスクリプトをゼロから書くときにクローンするプロジェクトです。

## 使い方

1. クローンします

2. 作成されたフォルダの名前を変えます

3. .gitフォルダを削除します（使わないので）

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

## yapf

書式を自動整形したい場合にはyapfを使います。
特にスクリプトのインデントの数を2にするか、4にするか迷うときに、一括変換する場合に便利です。
Visual Studio Codeでは、右クリック→ドキュメントのフォーマット、で変換されます。

```bash
pip install yapf [--proxy=http://name:pass@proxyaddr:8080]
```

## Visual Studio Codeの設定

拡張機能の「Python」を導入することで、Pythonスクリプトの編集が楽になります。

<https://marketplace.visualstudio.com/items?itemName=donjayamanne.python>

ファイル→基本設定→設定、に以下の設定を加えることで、エディタの中でpylintとyapfが使えるようになります。。

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

# 履歴

20190209 改行コードを全てLFに統一
20190209 SafeConfigParser()をConfigParser()に変更
