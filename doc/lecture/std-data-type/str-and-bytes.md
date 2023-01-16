<a href="https://colab.research.google.com/github/nokomoro3/book-ml-transformers/blob/main/ml-transformers-chap01-introduction.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# str型とbytes型

## str型について

### 基本操作

str型は文字列を扱う型である。またimmutableでもある。

よく使う操作を以下に列挙する。


```python
sample_str = "aaa,bbb,ccc"

# splitで文字分割
tok = sample_str.split(",")
print(tok)

# splitの区切り文字は複数でもOK
sample_str = "aaa, bbb, ccc"
tok = sample_str.split(", ")
print(tok)

```

    ['aaa', 'bbb', 'ccc']
    ['aaa', 'bbb', 'ccc']
    


```python
# 大文字小文字の正規化
sample_str = "aPPle"
print(sample_str.lower())
print(sample_str.upper())
print(sample_str.capitalize())
```

    apple
    APPLE
    Apple
    


```python
# rstripで右側にあるゴミを消す。
sample_str = "aaa, bbb, ccc\r\n"
print(sample_str)
print(sample_str.rstrip("\r\n"))
```

    aaa, bbb, ccc
    
    aaa, bbb, ccc
    


```python
# joinで分割したものを任意の文字で結合する
sample_list = ["apple","orange","melon"]
print(", ".join(sample_list))
```

    apple, orange, melon
    


```python
# 繰り返し（まあリストでもできるので、str型の特性というわけではない）
print("="*100)
```

    ====================================================================================================
    


```python
# 日本語のスライスも文字単位（マルチバイトかどうかは関係なく文字数をカウントできる）
sample_str = "こんにちは。今日はいい天気ですね。"
print(sample_str[2:4])
```

    にち
    

その他、検索や置換などあります。以下も参照ください。

- [Python | 文字列操作(変数展開, スライス, 置換, 検索, 分割) - わくわくBank](https://www.wakuwakubank.com/posts/261-python-string/)

### 値の埋め込みはf-stringが基本

f-stringを極力使いましょう。高速ですし、何が出力されるのか明瞭です。


```python
value = 3.141592

print(f"{value}")
```

    3.141592
    

コロン以降に書式を記述できます。


```python
print(f"{value:.3f}")
```

    3.142
    

Python3.8以降では変数名を同時出力することが以下の記法で可能です。


```python
print(f"{value=:.3f}")
```

    value=3.142
    

### 文字コードとencode,decode

Pythonは基本的にprintなどで出力される文字列のデフォルトがutf-8となっています。

なお、変数定義した状態では文字コードはencodeされる前です。encode後はbytes型になります。


```python
sample_str = "こんにちは。今日はいい天気ですね。"

sample_str_encoded = sample_str.encode() # デフォルトはutf-8
print(sample_str_encoded)
print(type(sample_str_encoded))
```

    b'\xe3\x81\x93\xe3\x82\x93\xe3\x81\xab\xe3\x81\xa1\xe3\x81\xaf\xe3\x80\x82\xe4\xbb\x8a\xe6\x97\xa5\xe3\x81\xaf\xe3\x81\x84\xe3\x81\x84\xe5\xa4\xa9\xe6\xb0\x97\xe3\x81\xa7\xe3\x81\x99\xe3\x81\xad\xe3\x80\x82'
    <class 'bytes'>
    

以下のUTF-8のコード表を見ると、`b\xe3\x81\x93`の3byteが`"こ"`に該当する。

- [UTF-8コード表(1)](https://seiai.ed.jp/sys/text/java/utf8table.html)

また、コードポイントを調べるためには`ord()`を使用する。


```python
print(f"U+{ord('こ'):x}")
```

    U+3053
    

コードポイントとバイト列は異なるので注意が必要。

- [UnicodeとUTF-8の違いを雰囲気で理解する - Qiita](https://qiita.com/uchiko/items/cca77e3e6866ca35a0c9)

日本語だと、bytesになっていることがよくわかるが、英語だとprintしても何も変わってないように見えるので注意。よく見ると先頭に`b`が付いている。


```python
sample_str = "Hello, World."

sample_str_encoded = sample_str.encode()
print(sample_str_encoded)
print(type(sample_str_encoded))
```

    b'Hello, World.'
    <class 'bytes'>
    

encodeされているものを受け取った場合は、逆にdecodeすればPython上のstrデータとして扱うことが可能。


```python
sample_str = "こんにちは。今日はいい天気ですね。"

sample_str_encoded = sample_str.encode()

sample_str_encdec = sample_str_encoded.decode()
print(sample_str_encdec)
print(type(sample_str_encdec))
```

    こんにちは。今日はいい天気ですね。
    <class 'str'>
    

## bytes型について

### 変更可能性

bytes型もstr型と同様にimmutableである。しかし、bytesにはmutableなバージョンであるbytearrayがある。

### pack（数値をbytes型にする）

bytes型をそのまま使うシーンはそれほど多くないのですが、

音声のwavフォーマットなどはヘッダを除くと波形データがそのままbytesデータとして保管されているため

音声処理では使うシーンが多少ありました。

例えば、16bit signed little endianの場合は以下のように`<h`でbytes型にpackできます。


```python
import struct

src_int = 15000
dst_int = struct.pack('<h', src_int) # 16bit little-endian

print(dst_int)

# printでは勝手に文字に置き換わるので、bytesの要素で出力すると分かりやすい
print(f"0x" + "".join(f"{i:0x}" for i in dst_int))
```

    b'\x98:'
    0x983a
    

フォーマットに指定可能なものは以下を参照ください。

- [バイトオーダ、サイズ、アラインメント](https://docs.python.org/ja/3/library/struct.html#byte-order-size-and-alignment)
- [書式指定文字](https://docs.python.org/ja/3/library/struct.html#format-characters)

このフォーマットの指定方法はNumPyを使用する際にも、出てくるケースがあります。

配列をpackする方法は少し工夫が必要で、以下になります。


```python
src_int = [15000, 16000, 17000]
dst_int = struct.pack('<'+'h'*len(src_int), *src_int) # 16bit little-endian

print("".join(f"{i:0x}" for i in dst_int))
```

    983a803e6842
    

### unpack（bytes型を数値にする）

逆にunpackして数値データに戻すためには以下のようにします。


```python
struct.unpack('<'+'h'*(len(dst_int)>>1), dst_int)
```




    (15000, 16000, 17000)



### NumPyによる代用

pack, unpackを実際に利用するシーンは少ない。NumPyで代用でき、NumPyの方が直感的で扱いやすいため。


```python
import numpy as np

dst_int = np.array([15000, 16000, 17000], dtype='<h').tobytes()
print("".join(f"{i:0x}" for i in dst_int))
```

    983a803e6842
    

`tobytes()`にはorderが指定できるが、多次元配列をbytes型にする時のorderを決めるために使用する。

詳細は以下。

- [NumPyの多次元配列データ構造ndarrayの基礎 - DeepAge](https://deepage.net/features/numpy-ndarray.html)


```python
np.frombuffer(dst_int, dtype='<h')
```




    array([15000, 16000, 17000], dtype=int16)


