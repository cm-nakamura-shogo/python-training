# 事前準備

本ページの内容は初回の開催前に各自で準備をお願いする想定です。（必要に応じてフォロー）

確認も含めて第１回としても良いように思います。

## 開発環境

- エディタはVSCodeを推奨。
- Python環境はpyenv + poetryでの構築を推奨。
- 以下を参考に構築する。
  - [pyenvとpoetryでディレクトリ毎にPython環境を切り替える手順＋ノウハウまとめ | DevelopersIO](https://dev.classmethod.jp/articles/pyenv-and-poetry/)
  - いれるバージョンは記事通りPython 3.8以降が良いかなと思います。

## VSCode

### VSCodeプラグイン

- 基本
  - [Japanese Language Pack](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-ja)
    - 日本語化。時々英語に戻るので以下で設定する。
      - Ctrl+Shift+P を押して "コマンド パレット" を表示。
      - display と入力して Configure Display Language コマンドを実行。
      - するとインストールされている言語の一覧がロケールごとに表示される。
      - UI 言語を切り替えるには、別の "ロケール" を選択。

- 編集補助
  - [Insert Numbers](https://marketplace.visualstudio.com/items?itemName=Asuka.insertnumbers)
    - マルチカーソルで文字列をフォーマット指定して連番を入力できる。
  - [change-case](https://marketplace.visualstudio.com/items?itemName=wmaurer.change-case)
    - 選択範囲を特定のchaseに変更する。
    - snake_caseやkebab-caseなど。
  - [Snippet Generator](https://marketplace.visualstudio.com/items?itemName=fiore57.snippet-generator)
    - コードスニペットを作成する補助ツール

- 視認性
  - [indent-rainbow](https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow)
    - インデントを色分けしてくれる。
  - [Rainbow CSV](https://marketplace.visualstudio.com/items?itemName=mechatroner.rainbow-csv)
    - CSVの視認性向上。
  - [Trailing Space](https://marketplace.visualstudio.com/items?itemName=shardulm94.trailing-spaces)
    - 空白を可視化する。
  - [Error Lens](https://marketplace.visualstudio.com/items?itemName=usernamehw.errorlens)
    - エラーの内容をエディタで見えるようにしてくれる（マウスオーバーする必要がない）

- Git
  - [Git Graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph)
    - 変更履歴がツリーで見れる。
  - [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)
    - ブランチ同士の差分確認やファイル別の変更履歴の確認に主に使っている。
    - フルの機能は実は使いこなせてない気もしている。

- Python
  - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
    - Python開発の基本。
  - [autoDocstring](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring)
    - Pythonのdocstringを自動生成できる。

- Markdown
  - [Markdown PDF](https://marketplace.visualstudio.com/items?itemName=yzane.markdown-pdf)
    - MarkdownをPDF変換する機能
  - [Markdown Preview Enhanced](https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced)
    - Markdownのプレビュー表示が見やすくなる。
  - [Draw.io Integration](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio)
    - drawioの図を書ける。
    - *.drawio.svgで保存すれば編集も可能で、そのままmarkdownにも埋め込める。
  - [PlantUML](https://marketplace.visualstudio.com/items?itemName=jebbs.plantuml)
    - UMLを記述できる。図として出力し、markdownに埋め込める。
    - 出力先はデフォルトはoutになるが、以下の設定で変更できる。
      ```json
      "plantuml.exportOutDir": "plantuml"
      ```
    - ある程度GitHubなどの描画側で対応しているところが出始めてるので、使わずに済む将来が来ると良いなと思っている。
  - [Paste Image](https://marketplace.visualstudio.com/items?itemName=mushan.vscode-paste-image)
    - クリップボードからmarkdownに画像を張り付けられる。
    - Snipping Toolとの連携で結構良い。
    - 以下に使い方と推奨設定があるのでご参考。
      - https://zenn.dev/ktechb/articles/968ff79f8f9c46a26ee5

- フォーマッター
  - [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)
    - 自動整形ツール。
    - あまりメリットをまだ感じられていないが、チーム開発では嬉しいらしい。
    - TS界隈の開発者は使ってるのをよく見るが、Pythonで使ってる人をあまり見たことがない。
      - これはおそらくPython拡張機能が含んでいるためと考えられる。
  - [isort](https://marketplace.visualstudio.com/items?itemName=ms-python.isort)
    - importをPEP8準拠にしてくれる拡張機能
  - [Black Formatter](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter)
    - 結構厳しめのPythonフォーマッタ
    - 設定方法
      - [VSCode拡張機能のBlack Formatterとisortを用いたPythonのコードフォーマット - nujust's blog](https://nujust.hatenablog.com/entry/2022/07/24/114715)

- リモート系
  - [Remote SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh)
    - VSCodeからサーバーにSSH接続できる。
    - サーバー上のフォルダもVSCodeでオープンすることが可能
  - [WSL](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl)
    - 上記のWSL版
    - 実はあまり詳しくない。
  - [Remote Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
    - コンテナ開発で使うやつ。実はあまり詳しくない。

### コードスニペットの使い方

- Visual Studio Codeに定型文（スニペット）を登録する方法
  - https://slash-mochi.net/?p=1978

- VSCodeのUser Snippetを活用しよう！
  - https://qiita.com/282Haniwa/items/82828c6a566e3e7e047d

### VSCodeショートカット

意外と網羅できてないショートカットを自分なりに整理する。

#### ウィンドウ移動

|キー|内容|
|:---|:---|
|Ctrl + \||左右分割|
|Ctrl + W|ウィンドウを閉じる|
|Ctrl + 数字|複数ウィンドウを移動(ない場合は作成)|
|Ctrl + Tab|タブ移動|
|Ctrl + P|ファイル名で検索してファイルをオープン|
|Ctrl + J|ターミナルウィンドウを開く|
|Ctrl + Shift + `|ターミナルウィンドウを増やす|

#### カーソル移動

|キー|内容|
|:---|:---|
|Ctrl + 左右|単語毎カーソル移動|
|Ctrl + Home|行頭移動|
|Ctrl + End |行末移動|

#### マルチカーソル

いくつかやり方がある。

- マウスを使用する方法
  - Alt + マウスクリック
  - マウス中芯ボタンクリックのドラッグ
  - Shift + Alt + マウスの右クリックドラッグ
- マウスなしで実行可能な方法
  - Alt + Ctrl + 上下
  - 単語選択 ⇒ Ctrl + D （検索しながらカーソルを増やせる）

#### 編集操作

|キー|内容|
|:---|:---|
|Alt + 上下|行移動|

## VSCodeのファイル比較

実はファイル２つを選択して右クリックで可能。

## Pythonの対話型シェルについて

昨今はipythonの他にも、bpythonやptpythonなどがあるらしい。

- [#python の動作確認に まだipython なんか使ってるの？これからは bpython でしょ！ ( コンソール比較 ) - Qiita](https://qiita.com/YumaInaura/items/1707b708c608e9f9a488)

bpythonはWindows + poetryでうまく動かせなかったので、みんなも試してみてほしい。

## 参考書

辞書的に使いますのでお財布と相談しながら準備。

- [O'Reilly Japan - リーダブルコード](https://www.oreilly.co.jp/books/9784873115658/)
- [O'Reilly Japan - Fluent Python](https://www.oreilly.co.jp/books/9784873118178/)
  - 英語の場合、第２版あり
    - [Fluent Python, 2nd Edition [Book]](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/)
- [O'Reilly Japan - Effective Python 第2版](https://www.oreilly.co.jp/books/9784873119175/)
- [エキスパートPythonプログラミング 改訂3版【委託】 - 達人出版会](https://tatsu-zine.com/books/expert-python-programming-3ed)
- [オブジェクト指向のこころ (SOFTWARE PATTERNS SERIES) | アラン・シャロウェイ, ジェームズ・R・トロット, 村上 雅章 |本 | 通販 | Amazon](https://www.amazon.co.jp/dp/4621066048)
