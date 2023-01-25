# 標準のデータ型

## 座学

2日程に分けるかもしれない。

- [1. 基本                ](./basic.md)
- [2. ミュータブルとコピー](./mutable-and-copy.md)
- [3. str型とbyte型       ](./str-and-bytes.md)
- [4. datetime型          ](./datetime.md)
- [5. collections         ](./collections.md)

## 演習

### 問１

例えばのような階層構造をもつリストが与えられる。

```python
sample_list = [ ['A', 'B', 'C'], ['D', 'E', 'F'], 'G', 'H', ['I', ['J', 'K'], ['L', 'M', 'N']]]
```

これをどのような階層構造になっても、以下のようにフラットにする関数を作成せよ。
その際、なるべく破壊的変更を使用せずに実装せよ。（再代入は許容する）

- ヒント：再帰処理

```python
print(flaten_list)
# OUT: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
```

### 問２

例えばのような階層構造をもつdictを考える。

```python
sample_dict = {
    "hoge": {'A': 1, 'B': 2, 'C': 3},
    "fuga": {'D': 4, 'E': 5, 'F': 6}, 
    'G': 7, 
    'H': 8, 
    "hage": {'I': 9 , "kuso": {'J': 10, 'K': 11}},
    "ahou": {'L': 12, 'M': 13, 'N': 14}
}
```

この末端の要素のvalueが数値(number)である場合、それを2倍とするような関数を作成せよ。
キーが数値(number)でない場合は、何もしないこととする。
また実装の際は、なるべく破壊的変更を使用せずに実装せよ。（再代入は許容する）

- ヒント：型の確認は、isinstanceで確認できる

```python
print(output_dict)
# OUT: {
#     "hoge": {'A': 2, 'B': 4, 'C': 6},
#     "fuga": {'D': 8, 'E': 10, 'F': 12}, 
#     'G': 14, 
#     'H': 16, 
#     "hage": {'I': 18 , "kuso": {'J': 20, 'K': 22}},
#     "ahou": {'L': 24, 'M': 26, 'N': 28}
# }
```

### 問３

センサーからバイトデータを取得してそれを実験用にprintでログを取得した。

しかし、バイトデータをそのままダンプしたため、以下のように結果がデコード前の生のバイトデータとなってしまった。

```
b'j\x8c\x13\xbeu\xdfm>}"\x08?\x00\x00'
b'\xa4\r1\xbe~\xef\x94?\xc6\r\xba\xbf\x01\x00'
b'\x92\xf9\xe3\xbdU\x19(?\xd0\xe2\x9f\xbe\x00\x00'
b'5\xb53?\x96Q\xe2=\xcc\x10\xfb>\x01\x00'
b'\x81\xa6\x02\xbe\xa5\x02=\xbfn\x97_?\x00\x00'
b'G\xa9\xbf\xbfu\xe0\x81\xbf\xa0gv\xbe\x01\x00'
b'\xa1%\xaa>!A|>\xb2\xd1\xc0>\x01\x00'
b'u\xe0\x88\xbe\x7f\xd1\xa7?\xab+~>\x00\x00'
b'k*^\xbec\xa0*=\x92FH?\x00\x00'
b'\x01U\xed=\x07\xc0\xd9\xbd\x11~\x8e\xbf\x00\x00'
```

このデータを解析して、人間がよめるログデータに変換せよ。

ただし、バイトデータは以下の仕様と分かっているものとする。

- 順にfloat(32bit)のデータが3つ、整数(16bit)が1つ格納されている。
- データはすべてLittle-Endianである。

- ヒント
  - [pythonの数値・bytes相互変換（＋おまけ：bytesを誤ってstr変換して保存してしまった場合） - Qiita](https://qiita.com/nokomoro3/items/36a53daf60381e068990)

### 問４

問３のようなログデータを生成するプログラムを作成せよ。

ただし、生成にはrandomモジュールを利用して良い。
