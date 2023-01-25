<a href="https://colab.research.google.com/github/nokomoro3/book-ml-transformers/blob/main/ml-transformers-chap01-introduction.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# collections

## collectionsとは

list, dict, tupleなどはcollectionsである。"ABC"などの文字列もcollectionsとなる。

その他、重要なcollectionsは以下。

- namedtuple：タプルのサブクラスを作成するファクトリ関数です。名前付きの属性としても要素にアクセスできる機能を持っています。
- deque：スタックとキューに必要な操作を備えた両端キューです。これはリストに似たコレクションですが、リストの先頭と末尾への高速な追加、削除を行うことができます。
- ChainMap：これは辞書のようなクラスで、複数の辞書をまとめて1 つの辞書に見せるビューを作成します。
- Counter：hashable なオブジェクトの個数をカウントするための辞書のサブクラスです。
- OrderedDict：要素が追加された順序を管理し変更できる、辞書のサブクラスです。
- defaultdict：要素が見つからなかったときに指定された関数を呼び出して初期値を自動作成する、辞書のサブクラスです。

### namedtuple
