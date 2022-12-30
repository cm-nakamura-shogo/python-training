# memo

## 進め方(案)

- 座学（15分）
- 演習（30分）
  - 画面共有付しながら適宜フィードバック。
  - 複数人の画面共有ってできたっけ。ハドルなら確かできる。
- お答え合わせ（15分）

## お題目（素案）

### 基礎

- 済：環境構築（おのおので良さそう）
  - Pythonもう整ってる？エディタはVSCode推奨だが現状はどうだろうか。
  - notebookじゃない環境で始めた方が良いかなと

- 済：俺たちの入出力
  - argparser, 基本的なfile IO系, 応用でファイル操作するpathlibなど。
- 済：俺たちの標準データ型
  - Python標準のデータ型を理解しよう
  - set, list, dict, tupleなど
  - str, bytesなど。encodingなども。
  - list, dictのアンパック
  - deep copyなど、参照がそのままわたるかどうか。
- 俺たちのループと条件分岐
  - for文について、breakについて
  - if-elseの戦略。
  - yieldやreturnについて。
  - switchは存在しない件
  - dictのループ、ifに使うべきデータ型
  - ループで迷子にならないようにするために。
- 俺たちのnumpy
  - 配列処理になれよう。多次元配列は怖くない、切り口が違うだけ。
- 俺たちのpandas
  - よくあるテーブル処理
  - 参考
    - https://nakamura-shogo.gitbook.io/dev-wiki/python/pandas
- 俺たちのデバッグ
  - printは基本
    - len(), type(), shapeはめっちゃ使う。
  - icecreamは便利
  - notebookでもdebugはできる

### 応用

- 俺たちのscikit-learn
- 俺たちのpytest
- 俺たちの型ヒントとvalidation
- 俺たちのオブジェクト指向
- 俺たちのFast API
- 俺たちのコンテナ

## QA

- forのelseとは
  - https://python.civic-apps.com/else-loop/
  - elseはbreakで捕まえられなかった例外処理的な位置づけっぽい。
- forとwhileの使い分け
  - whileは無限ループというイメージ。何回やるか決まってない。
- transpose, reshape, view
  - イメージ
    - (100, 32, 32, 3) # batch, height, width, channel
    - np.transpose(0,3,1,2)
    - (100, 3, 32, 32) # batch, height, width, channel
    - transposeは軸自体が代わるので、メモリの並び順が代わる。
    - reshapeはメモリの並び順が代わり。
    - viewはtransposeをしつつ、メモリ配置を変えない。
  - ちょっと違ったかも
    - https://blog.kikagaku.co.jp/pytorch1
  - メモリ配置の参考
    - https://dev.classmethod.jp/articles/numpy-broadcast-visualize/

## 参考書籍

- fluent python
  - https://www.oreilly.co.jp/books/9784873118178/
- エキPy
  - https://www.freia.jp/taka/blog/expert-python-programming-3rd-intro/index.html
- Python実践レシピ（吉本さんが貼ってくれた本）
  - https://www.amazon.co.jp/dp/4297125765
- リーダブルコードの話するの忘れていたわ
  - https://zenn.dev/msy/articles/90dfccc6d8e5f4
  - https://qiita.com/fkrw/items/7646563a2b238fbcff9a