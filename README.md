# python-training

Pythonトレーニング用のレポジトリです。

## lectures

### 基礎編

- [0. 事前準備                          ](./doc/lecture/prepare/README.md)
- [1. 標準データ型                      ](./doc/lecture/std-data-type/README.md)
- [2. プログラム入出力・ファイル操作    ](./doc/lecture/input-output/README.md)
- [3. 関数とクラス                      ](./doc/lecture/function-class/README.md)
- [4. ループと条件分岐                  ](./doc/lecture/for-if-else/README.md)
- [5. iteratorとgenerator               ](./doc/lecture/iterator-generator/README.md)
- [6. lambda式とmap, filter, reduce     ](./doc/lecture/lambda/README.md)
- [7. デコレータ                        ](./doc/lecture/decorator/README.md)
- [8. コンテキストマネージャ            ](./doc/lecture/context-manager/README.md)
- 型ヒントとvalidation
  - [Pythonで型を極める【Python 3.9対応】 - Qiita](https://qiita.com/papi_tokei/items/bf652696d6b98f23565a)
  - [Pythonで型指定するTypingの基本的な使い方まとめ | deecode blog](https://deecode.net/?p=530#%E9%96%A2%E6%95%B0%E3%82%AA%E3%83%96%E3%82%B8%E3%82%A7%E3%82%AF%E3%83%88%E3%83%BB%E3%82%B3%E3%83%BC%E3%83%AB%E3%83%90%E3%83%83%E3%82%AF_-_Callable%E5%9E%8B)
  - [Pythonのdataclassを知る](https://zenn.dev/karaage0703/articles/3508b20ece17d4)
  - [えんぶん@育休に戻りたいさんはTwitterを使っています: 「pydantic、だいぶdataclassっぽい書き方で行けるのねぇ。 JSONでschema出力できるのええなぁ。OpenAPI準拠だし。yamlも欲しいけど。」 / Twitter](https://twitter.com/enven_omiomi/status/1351923286498676738)
  - [https://twitter.com/digitalhimiko/status/1599929344629309442](https://twitter.com/digitalhimiko/status/1599929344629309442)
  - [pydanticを用いて@dataclassの型を堅牢にする - Qiita](https://qiita.com/valusun/items/971c227d7f74c14d874b?utm_content=buffer63f36&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer)
  - [https://twitter.com/search?q=dataclass pydantic&src=typed_query](https://twitter.com/search?q=dataclass%20pydantic&src=typed_query)
  - [Python3.7で導入されたdataclass入門 - MyEnigma](https://myenigma.hatenablog.com/entry/2020/03/07/171015#asdict%E9%96%A2%E6%95%B0%E3%81%A7dict%E3%81%AB%E5%A4%89%E6%8F%9B%E3%81%A7%E3%81%8D%E3%82%8BDict%E3%81%8B%E3%82%89%E7%B0%A1%E5%8D%98%E3%81%ABJSON%E3%81%AB%E3%82%82%E5%A4%89%E6%8F%9B%E3%81%A7%E3%81%8D%E3%82%8B)
  - [cpython/dataclasses.py at 29f98b46b77ee528477b9a7b335974b9682f7f14 · python/cpython](https://github.com/python/cpython/blob/29f98b46b77ee528477b9a7b335974b9682f7f14/Lib/dataclasses.py#L902)
- 非同期実行(threadとかasync)
- デバッグとロギング
- pytest
- その他
  - [Python パッケージングの標準を知ろう - Tech Blog - Recruit Engineer](https://engineer.recruit-lifestyle.co.jp/techblog/2019-12-25-python-packaging-specs/)
  - [python -m json.tool を実行したときの動きを確認してみた。 | DevelopersIO](https://dev.classmethod.jp/articles/python-m-json-tool-study/)
  - [PythonでS3上の自作モジュールをスクリプト中で動的にインポートしてみる | DevelopersIO](https://dev.classmethod.jp/articles/s3_python_module/)
  - [ThinkPython](https://cauldron.sakura.ne.jp/thinkpython/)
  - [[Python] 最小限setup.pyでのビルドを通じてsetuptoolsの気持ちを聞いてみた | DevelopersIO](https://dev.classmethod.jp/articles/python-setup-minimum/)
  - [Pythonの@propertyデコレータについてまとめる - Qiita](https://qiita.com/kudojp/items/6983f9ea5d0b2964f2ee)
  - キーワードのみの引数（エキPyより）
  - セイウチ演算子（エキPyより）
  - isなんとか（isinstance, issubclass）

### 応用編

- NumPy
- Pandas
  - いまさらもうPandasのやる気は起きないので、Polarsの記事でも見てもらおうかなぁ
- オブジェクト指向入門
- scikit-learn入門
- FastAPI入門
- Dockerコンテナ入門

### 実践編

- テーブルデータを処理する機械学習システムのバックエンドの構築
- NLPを処理する機械学習システムのバックエンドの構築
- CVを処理する機械学習システムのバックエンドの構築
- 上記のシステムをAWSにデプロイする検討
  - AppRunnerは良い選択肢かも（梶原さんが先生候補）
- 上記のシステムをGoogle Cloudにデプロイする検討
