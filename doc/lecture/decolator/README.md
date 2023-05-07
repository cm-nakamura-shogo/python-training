<a href="https://colab.research.google.com/github/cm-nakamura-shogo/python-training/blob/master/doc/lecture/decolator/README.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

## デコレータ

### デコレータとは

`@`とか書いて関数定義やクラス定義の直前についているやつのことをデコレータと言います。

既に登場した`@classmethod`や`@staticmethod`もデコレータの１種です。


```python
# ex.1 関数に付ける例

class MyClass:
    def __init__(self):
        pass
    @classmethod # これがデコレータ
    def sample_class_method(cls):
        pass
```

以下のようにクラス定義前にもつけることが可能です。


```python
# ex.2 クラスに付ける例

from dataclasses import dataclass

@dataclass  # これがデコレータ
class MyDataClass:
    attribute1: int
    attribute2: float
```

デコレータは自作することも可能で、関数に共通的な魔改造を施すときに使います。

例は色々ありますが、ログ出力を共通で実装したい場合などが例としてあります。

- [Pythonの関数の引数と戻り値のログ出力をデコレータで部品化する（Google Cloud Functions） | DevelopersIO](https://dev.classmethod.jp/articles/python-decorator-log-gcf/)

### デコレータの意味

デコレータ構文は単なるシンタックスシュガーであり、裏で行われる処理は単純に以下のようになっています。

```python
@some_decorator
def decorated_function():
    pass
```

上記は以下と等価です。

```python
def decorated_function():
    pass
decorated_function = some_decorator(decorated_function)
```

このようにデコレータは１つの引数を受け取れる、名前付きのcallableオブジェクトです。

`__call__()`メソッドが定義されていれば、callableオブジェクトとなるため、関数以外で実装することも可能です。

### デコレータの実装例

よく使われる実装例は以下です。


```python
def mydecorator(function):
    def wrapped(*args, **kwargs):

        print("ここに前処理")

        result = function(*args, **kwargs)

        print("ここに後処理")

        return result

    return wrapped
```

引数で与えられる関数`function`を別の関数`wrapped`でラップされたものを返す関数が`mydecorator`となっていることが分かります。

関数にデコレータを付けてみましょう。


```python
@mydecorator
def myfunc(a, b):
    print(a+b)

myfunc(1,2)
```

    ここに前処理
    3
    ここに後処理
    

デコレータはクラスとして実装することもできます。その場合、`__call__`というメソッドを実装しておきます。

デコレータが複雑なパラメータを扱う必要があったり、状態に依存した動作をさせたい場合は、クラスで実装する方が適切となります。


```python
class MyDecoratorClass():
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):

        print("ここに前処理")

        result = self.function(*args, **kwargs)

        print("ここに後処理")

        return result
```

関数に付けてみましょう。


```python
@MyDecoratorClass
def myfunc(a, b):
    print(a+b)

myfunc(1,2)
```

    ここに前処理
    3
    ここに後処理
    

### パラメータを受け取るデコレータ

より実用的にはパラメータを受け取るデコレータも需要がある。

その場合はさらにラッパーを一つ外側に増やせばよい。


```python
def decorator_wrapper(val=0):
    def mydecorator(function):
        def wrapped(*args, **kwargs):

            print("ここに前処理")
            print(val)

            result = function(*args, **kwargs)

            print("ここに後処理")

            return result
        return wrapped

    return mydecorator
```

引数で与えられる関数`function`を別の関数`wrapped`でラップされたものを返す関数が`mydecorator`となっている点は変わりがない。

その外側に`decorator_wrapper`というラッパーを作ることで、`decorator_wrapper(5)`がデコレータを返す。

この`decorator_wrapper`の引数に与えたものは、それぞれの中の関数のローカルに定義されていない限り、その上位インデントのものが参照できるため、結果的にデコレータにパラメータを与えられる。

（よくわから無い場合は、「day03 : 関数とクラス」を復習しよう）

実際のところ`decorator_wrapper`がデコレータかと言えば微妙で、`decorator_wrapper(5)`がデコレータを返すと見た方が理解しやすいと思われる。


```python
@decorator_wrapper(5)
def myfunc(a, b):
    print(a+b)

myfunc(1,2)
```

    ここに前処理
    5
    3
    ここに後処理
    

### docstringが失われる件

実際ここまでのサンプルのままでは、元の関数名やdocstringなどの関数のメタデータが失われ、実用上問題がある。

（VSCode上でも見えなくなると思ったけど、普通にdocstring消えなかった…）


```python
@decorator_wrapper(5)
def myfunc(a, b):
    """myfuncの説明"""
    print(a+b)
```


```python
print(myfunc.__name__)
```

    wrapped
    


```python
print(myfunc.__doc__)
```

    None
    

その場合は、`wrapped`にfunctoolsで提供されるwrapsデコレータを使えばよい。


```python
from functools import wraps

def decorator_wrapper(val=0):
    def mydecorator(function):
        @wraps(function)
        def wrapped(*args, **kwargs):

            print("ここに前処理")
            print(val)

            result = function(*args, **kwargs)

            print("ここに後処理")

            return result
        return wrapped

    return mydecorator

@decorator_wrapper(5)
def myfunc(a, b):
    """myfuncの説明"""
    print(a+b)

print(myfunc.__name__)
print(myfunc.__doc__)
```

    myfunc
    myfuncの説明
    

これで、関数のメタデータも保持されることが分かる。

### 少し用途が違うデコレータ

デコレータを付けた関数を普通に呼び出すことを想定しない使い方もある。


```python
funcs = []

def mydecorator(function):
    funcs.append(function)

@mydecorator
def hoge():
    print("hoge")

@mydecorator
def fuga():
    print("fuga")

print(funcs)
```

    [<function hoge at 0x00000206D2B1CD30>, <function fuga at 0x00000206D2B1CA60>]
    

むろんこの場合は`hoge`や`fuga`を直接呼び出すことはできない。これはmydecoratorがcallableを返してないためである。（`return function`をすれば直接呼び出せる）

呼び出し時は以下のように、`funcs[0]()`とすればよい。


```python
# fuga() # エラー
funcs[0]()
```

    hoge
    

こういった動作は、FlaskやFastAPIなどのWebフレームワークは使用していると考えられる。

参考

- [Python デコレータ再入門　 ~デコレータは種類別に覚えよう~ - Qiita](https://qiita.com/macinjoke/items/1be6cf0f1f238b5ba01b)

この場合にも、パラメータを与える場合には一つ外側にラッパーを設ければOK。

### 演習１

指定回数処理を繰り返すデコレータを作成してください。
<br>
<br>
<br>
<br>
<br>
以下解答。


```python
from functools import wraps

def repeat(n=5):
    def mydecorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                fn(*args, **kwargs)
        return wrapper
    return mydecorator
```


```python
@repeat(3)
def myfunc():
    """myfuncの説明"""
    print("hogehoge")

myfunc()
```

    hogehoge
    hogehoge
    hogehoge
    

### 実用例

ここまで理解できていれば、以下のブログの例は理解できるはず。

- [Pythonの関数の引数と戻り値のログ出力をデコレータで部品化する（Google Cloud Functions） | DevelopersIO](https://dev.classmethod.jp/articles/python-decorator-log-gcf/)

かなり複雑に作り込むとこういう例も。

- [A better way to logging in Python | F5 - Squashing Bugs](https://ankitbko.github.io/blog/2021/04/logging-in-python/)

その他には以下の例がエキPyでは挙げられている。

- 引数チェック
- キャッシュ
  - 関数が状態を持たない場合にのみ
- プロキシ
  - タグ付け、アクセス保護
- コンテキストプロバイダ
  - 特別な実行環境の設定をしたり、外したり
  - 例としてはロック機構など
  - 後述するwith文（コンテキストマネージャ）を使う方が現在は一般的

以上。
