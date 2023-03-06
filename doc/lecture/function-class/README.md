<a href="https://colab.research.google.com/github/cm-nakamura-shogo/python-training/blob/master/doc/lecture/function-class/README.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# 関数とクラス

## 関数

### 関数を使う理由

関数とはなんか一連の処理を入出力を定義してまとめたもの。

すべてうまく言語化できないが、関数を使うメリットを挙げてみる。

- 同じような処理を複数箇所に埋め込むことを避けられる
- 上記のためメンテが楽になる
- 適切な関数名であれば抽象的なままコードを読むことができる
- 関数単位でテスト（単体試験）を行うことができる
- 同時に理解する範囲が狭くなり認知しやすくなる（関数内の変数に外部から基本的にはアクセスできないためスコープが狭まる）
- 単純に分担がしやすくなる

関数化する合図の整理。

- 似たような処理が増えてきたなと感じたら
- 今ベースに書いているコードがデカくなってるなと感じたら

### 関数の例


```python
def print_message(name: str):
    print(f"ワイは{name}である。")
    return

print_message("nokomoro3")
```

    ワイはnokomoro3である。
    

### 変数のスコープ

これを題材に関数外の変数にアクセスできるかみてみる。


```python
hoge = "hoge"
def print_message(name: str):
    print(f"ワイは{name}である。")
    print(f"{hoge}")
    return

print_message("nokomoro3")
```

    ワイはnokomoro3である。
    hoge
    

上記のように、インデントの無い部分はグローバル変数であり、関数内からでもアクセスが可能なことがわかる。

ローカル変数とグローバル変数はそれぞれ`locals()`と`globals()`で確認することが可能。


```python
hoge = "hoge"
def print_message(name: str):
    print(locals()) # add
    print(globals()) # add
    print(f"ワイは{name}である。")
    print(f"{hoge}")
    return

print_message("nokomoro3")
```

    {'name': 'nokomoro3'}
    {'__name__': '__main__', '__doc__': 'Automatically created module for IPython interactive environment', '__package__': None, '__loader__': None, '__spec__': None, '__builtin__': <module 'builtins' (built-in)>, '__builtins__': <module 'builtins' (built-in)>, '_ih': ['', 'def print_message(name: str):\n    print(f"ワイは{name}である。")\n    return\n\nprint_message("nokomoro3")', 'hoge = "hoge"\ndef print_message(name: str):\n    print(f"ワイは{name}である。")\n    print(f"{hoge}")\n    return\n\nprint_message("nokomoro3")', 'hoge = "hoge"\ndef print_message(name: str):\n    print(locals()) # add\n    print(globals()) # add\n    print(f"ワイは{name}である。")\n    print(f"{hoge}")\n    return\n\nprint_message("nokomoro3")'], '_oh': {}, '_dh': [WindowsPath('c:/Users/nakamura.shogo/Desktop/repos/cm-nakamura-shogo/python-training/doc/lecture/function-class'), WindowsPath('c:/Users/nakamura.shogo/Desktop/repos/cm-nakamura-shogo/python-training/doc/lecture/function-class')], 'In': ['', 'def print_message(name: str):\n    print(f"ワイは{name}である。")\n    return\n\nprint_message("nokomoro3")', 'hoge = "hoge"\ndef print_message(name: str):\n    print(f"ワイは{name}である。")\n    print(f"{hoge}")\n    return\n\nprint_message("nokomoro3")', 'hoge = "hoge"\ndef print_message(name: str):\n    print(locals()) # add\n    print(globals()) # add\n    print(f"ワイは{name}である。")\n    print(f"{hoge}")\n    return\n\nprint_message("nokomoro3")'], 'Out': {}, 'get_ipython': <bound method InteractiveShell.get_ipython of <ipykernel.zmqshell.ZMQInteractiveShell object at 0x000001ECE3000910>>, 'exit': <IPython.core.autocall.ZMQExitAutocall object at 0x000001ECE3035520>, 'quit': <IPython.core.autocall.ZMQExitAutocall object at 0x000001ECE3035520>, 'open': <function open at 0x000001ECE15714C0>, '_': '', '__': '', '___': '', '__vsc_ipynb_file__': 'c:\\Users\\nakamura.shogo\\Desktop\\repos\\cm-nakamura-shogo\\python-training\\doc\\lecture\\function-class\\README.ipynb', '_i': 'hoge = "hoge"\ndef print_message(name: str):\n    print(f"ワイは{name}である。")\n    print(f"{hoge}")\n    return\n\nprint_message("nokomoro3")', '_ii': 'def print_message(name: str):\n    print(f"ワイは{name}である。")\n    return\n\nprint_message("nokomoro3")', '_iii': '', '_i1': 'def print_message(name: str):\n    print(f"ワイは{name}である。")\n    return\n\nprint_message("nokomoro3")', 'print_message': <function print_message at 0x000001ECE3064F70>, '_i2': 'hoge = "hoge"\ndef print_message(name: str):\n    print(f"ワイは{name}である。")\n    print(f"{hoge}")\n    return\n\nprint_message("nokomoro3")', 'hoge': 'hoge', '_i3': 'hoge = "hoge"\ndef print_message(name: str):\n    print(locals()) # add\n    print(globals()) # add\n    print(f"ワイは{name}である。")\n    print(f"{hoge}")\n    return\n\nprint_message("nokomoro3")'}
    ワイはnokomoro3である。
    hoge
    

ただし、以下のように実行するとエラーとなるので注意が必要。


```python
try:
    hoge = "hoge"
    def print_message(name: str):
        hoge = hoge + "aaa"
        print(f"ワイは{name}である。")
        print(hoge)
        return

    print_message("nokomoro3")
except Exception as e:
    print(e)
```

    local variable 'hoge' referenced before assignment
    

（グローバルにはipynbの場合なので様々な変数が格納されていることがわかる。）

globalsに定義済みの変数がlocalsにもある場合、関数内ではlocalsが優先されるため注意する。


```python
hoge = "hoge"
def print_message(name: str):
    hoge = "hoge_local" # add locals
    print(f"ワイは{name}である。")
    print(f"{hoge}")
    return

print_message("nokomoro3")
```

    ワイはnokomoro3である。
    hoge_local
    

なお上記はグローバル変数を上書きしているわけではなく、関数内で宣言したローカル変数は別オブジェクトになっている。

その証拠に関数を通った後でもグローバル側の値は変わらない（再代入されない）。念のためオブジェクトIDも見てみよう。


```python
hoge = "hoge"
print(f"{hoge}, {id(hoge)}") # add id check
def print_message(name: str):
    hoge = "hoge_local"
    print(f"ワイは{name}である。")
    print(f"{hoge}, {id(hoge)}") # add id check
    return

print_message("nokomoro3")
print(f"{hoge}, {id(hoge)}") # add id check
```

    hoge, 2116932675824
    ワイはnokomoro3である。
    hoge_local, 2116932702000
    hoge, 2116932675824
    

### グローバル変数の変更

グローバル変数そのものにアクセスし値を変えたい（再代入したい）場合は以下のような宣言を使用する。


```python
hoge = "hoge"
print(f"{hoge}, {id(hoge)}")
def print_message(name: str):
    global hoge # add global access
    hoge = "hoge_local"
    print(f"ワイは{name}である。")
    print(f"{hoge}, {id(hoge)}")
    return

print_message("nokomoro3")
print(f"{hoge}, {id(hoge)}")
```

    hoge, 2116932675824
    ワイはnokomoro3である。
    hoge_local, 2116932702000
    hoge_local, 2116932702000
    

オブジェクトIDを見ると分かるように、元と同じオブジェクトというわけではないので注意が必要（そもそも文字列がimmutableなので仕方ない）。

ローカルで宣言されているかどうかで、グローバルにアクセスするかどうかの挙動が変わるのも注意。

つまり、ローカルで宣言されており、その宣言前にグローバル側にアクセスしようとしてもできない。


```python
try:
    hoge = "hoge"
    print(f"{hoge}, {id(hoge)}")
    def print_message(name: str):
        print(f"{hoge}, {id(hoge)}") # ここがエラーに
        hoge = "hoge_local" # ここがあると
        print(f"ワイは{name}である。")
        print(f"{hoge}, {id(hoge)}")
        return

    print_message("nokomoro3")
    print(f"{hoge}, {id(hoge)}")
except Exception as e:
    print(e)
```

    hoge, 2116932675824
    local variable 'hoge' referenced before assignment
    

### mutableな変数の場合

当然だが、mutableなデータ型の場合、globalとしなくてもアクセスさせできれば書き換えが可能になる。

よくわからない場合は、mutable・immutableについて復習が必要。


```python
hoge_list = ["hoge1"]
print(f"{hoge_list}, {id(hoge_list)}")
def print_message(name: str):
    hoge_list.append("hoge2")
    print(f"ワイは{name}である。")
    print(f"{hoge_list}, {id(hoge_list)}")
    return

print_message("nokomoro3")
print(f"{hoge_list}, {id(hoge_list)}")
```

    ['hoge1'], 2116933016832
    ワイはnokomoro3である。
    ['hoge1', 'hoge2'], 2116933016832
    ['hoge1', 'hoge2'], 2116933016832
    

上のインデントの情報を持ってこれるのは、グローバル以外でも同様だが、グローバルのように再代入する方法は準備されていない様子。


```python
def sample():
    fuga = "fuga"
    print(f"{fuga}, {id(fuga)}")
    def print_message(name: str):
        fuga = "fugafuga"
        print(locals())
        print(f"ワイは{name}である。")
        print(f"{fuga}, {id(fuga)}")
        return

    print_message("nokomoro3")
    print(f"{fuga}, {id(fuga)}")

sample()
```

    fuga, 2116932768048
    {'name': 'nokomoro3', 'fuga': 'fugafuga'}
    ワイはnokomoro3である。
    fugafuga, 2116932708272
    fuga, 2116932768048
    

### 関数化の課題

このようにグローバル変数など関数外にある変数を使えば、状態（データ）を保持した処理が可能となる。

しかしそういったデータを保持したい処理の塊が複数ある場合、グローバル変数はどこからでも参照可能なので問題が発生する。

そのためデータと処理をまとめるためのクラスというものが使われる。

## クラス

クラス化とは何か。端的にいうと関連するデータ（変数）と処理（関数）をまとめるためのものである。

よく「クラスを使えば、現実世界のオブジェクトに当てはめてプログラミングをできる」などといかがわしい情報があるが、これは誤りである。

クラスは関連するものであれば抽象的でもよいし、現実の機構がかならずしもプログラミングの構造上適切であるとは限らない。

クラスを使う理由は、現実世界のモデリングではなく、極論関数を使う理由とそこまで変わらない。

クラスを使う理由をあげてみよう。

- 同じような処理を複数箇所に埋め込むことを避けられる
- 上記のためメンテが楽になる
- 適切なクラス名であれば抽象的なままコードを読むことができる
- クラス単位でテスト（単体試験）を行うことができる
- 同時に理解する範囲が狭くなり認知しやすくなる（関数内の変数に外部から基本的にはアクセスできないためスコープが狭まる）
- 単純に分担がしやすくなる

ほぼ関数のときと同じことを書いており、これがより効率的に実現できる手法と考えればよい。

### クラスの例


```python
class SampleCat():
    def __init__(self, name: str):
        self.name = name
    def なでる(self):
        print("ゴロゴロ...うれしいニャン")
    def 呼びかける(self, name: str):
        if self.name in name:
            print("にゃー")
        else:
            print("（は？名前よべし）")

tama = SampleCat("たま") # インスタンス化
tama.なでる()
tama.呼びかける("たま、こっちおいで")
tama.呼びかける("おーい、こっちおいで")
```

    ゴロゴロ...うれしいニャン
    にゃー
    （は？名前よべし）
    

`__init__`はマジックメソッドであり、この場合はコンストラクタである。コンストラクタはインスタンス化時に実行される初期化関数。

マジックメソッドの詳細は以下を参照。一応デストラクタとして`__del__`もあるみたい。

- [http://www.ops.dti.ne.jp/ironpython.beginner/method.html](http://www.ops.dti.ne.jp/ironpython.beginner/method.html)

またクラス内の第一引数は`self`を付ける必要があり、クラス内で呼び出す場合は`self.関数名`で呼び出す。

`self.変数名`はクラス内でアクセス可能な変数であり、インスタンス内にデータが保持される。

### クラス関数

さきほど定義した`def なでる(self)`という関数は、クラスのデータに依存しない。そのためインスタンスではなくクラス関数にしても良い。

クラス関数は、`@classmethod`デコレータで囲み、`self`の代わりに`cls`を第一引数に持つ。


```python
class SampleCat():
    @classmethod
    def なでる(cls):
        print("ゴロゴロ...うれしいニャン")
    def __init__(self, name: str):
        self.name = name
    def 呼びかける(self, name: str):
        if self.name in name:
            print("にゃー")
        else:
            print("（は？名前よべし）")

tama = SampleCat("たま") # インスタンス化

print(tama.name)

tama.なでる()
tama.呼びかける("たま、こっちおいで")
tama.呼びかける("おーい、こっちおいで")
```

    たま
    ゴロゴロ...うれしいニャン
    にゃー
    （は？名前よべし）
    

クラス関数はインスタンス化せずに呼び出すことも可能（この例では少し奇妙だが）


```python
SampleCat.なでる()
```

    ゴロゴロ...うれしいニャン
    

classmethodを使うシーンは以下を参照

- [Pythonのクラスメソッド（@classmethod）とは？使いどころとメソッドとの違いを解説 - Python学習チャンネル by PyQ](https://blog.pyq.jp/entry/Python_kaiketsu_190205)

### staticmethodとclassmethodの違い

あまり気にしなくて良い。基本的には`@classmethod`を使えばOK。`@staticmethod`はclsを暗黙的に第一引数にとらない。

- [Python の staticmethod と classmethod のちがい - Life with Python](https://www.lifewithpython.com/2014/02/python-difference-between-staticmethod-and-classmethod.html)

clsにあるものを使わない場合は、`@staticmethod`でも良いよということ。

### クラス変数

クラス変数は、メンバ関数とおなじインデント記述すればそのような動きになる。（インスタンス化前にアクセスできる）


```python
class SampleCat():
    sample_class_var = "hoge"
    @classmethod
    def なでる(cls):
        print("ゴロゴロ...うれしいニャン")
    def __init__(self, name: str):
        self.name = name
        self.hoge = name
    def 呼びかける(self, name: str):
        if self.name in name:
            print("にゃー")
        else:
            print("（は？名前よべし）")

print(SampleCat.sample_class_var)
```

    hoge
    

このクラス変数はクラスのどこでも再代入できるので要注意。


```python
class SampleCat():
    sample_class_var = "hoge"
    @classmethod
    def なでる(cls):
        print("ゴロゴロ...うれしいニャン")
    def __init__(self, name: str):
        self.name = name
        self.hoge = name
    def 呼びかける(self, name: str):
        if self.name in name:
            print("にゃー")
        else:
            print("（は？名前よべし）")

print(SampleCat.sample_class_var)
```

    hoge
    

### finalな変数（定数）の定義

定数とは一度代入すると、再代入できない定数のこと。PEP8ではすべて大文字のアンダーバー区切りとなっている。

Python 3.7まではfinalな変数（定数）は定義できなかったが、Python 3.8のtypingモジュールでは定義できるようになった。

- [Pythonで型を極める【Python 3.9対応】 - Qiita](https://qiita.com/papi_tokei/items/bf652696d6b98f23565a)

## PEP8に基づく命名規則

ここでいまいちど、PEP8に基づく命名規則を抑えておこう。

- [Python命名規則（PEP8より) - Qiita](https://qiita.com/shiracamus/items/bc3bdfc206b39e0a75b2)

ここらへんも

- [Pythonのアンダースコア( _ )を使いこなそう！. Pythonを上手そうに見させる手品の一つ「アンダースコア」の4種類の使い方を説… | by Neil Wu | LSC PSD | Medium](https://medium.com/lsc-psd/pythonic%E8%89%B2%E3%80%85-python%E3%81%AE%E3%82%A2%E3%83%B3%E3%83%80%E3%83%BC%E3%82%B9%E3%82%B3%E3%82%A2-%E3%82%92%E4%BD%BF%E3%81%84%E3%81%93%E3%81%AA%E3%81%9D%E3%81%86-3c132842eeef)

## 演習

問１：以下を実行した時の出力を答えよ


```python
def f():
    def g(a):
        global s
        s += a
    s = 1
    g(2)
    print(s)

s = 0
f()
print(s)
```

問２：以下を実行した時の出力を答えよ


```python
def f():
    def g(a):
        s = 100
        print(s)
    g(2)
    print(s)

s = 0
f()
print(s)
```
