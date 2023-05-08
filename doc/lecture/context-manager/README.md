<a href="https://colab.research.google.com/github/cm-nakamura-shogo/python-training/blob/master/doc/lecture/context-manager/README.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

## コンテキストマネージャ

### コンテキストマネージャとは

with文を使う構文で、このコードブロックの前後でコンテキストマネージャを呼び出すことを可能としている。

たとえば、コードブロック内で例外を送出しても、ブロックの前後ではある処理がコールされる。

```python
with open("sample.txt", "wt") as f:
    lines = f.readlines()
    print(len(lines))
```

上記のサンプルでは、openをコンテキストマネージャとして扱っている。

本来、withを使わない場合は以下のように書く。

```python
f = open("sample.txt", "wt")
try:
    lines = f.readlines()
    print(len(lines))
finally:
    f.close()
```

これをwithでシンプルに記述できるようになっている。

### コンテキストマネージャを実装する（クラス）

コンテキストマネージャプロトコルを実装すると、コンテキストマネージャとして使用できる。

- プロトコルとしては、`__enter__`と`__exit__`を実装
- `__enter__`は、ラップされているコードの実行前に呼び出される処理を記述し、このメソッドはコンテキスト変数を返す
- `__exit__`は、ラップされているコードの実行後に呼び出され、例外すべてをキャプチャする


```python
class SampleContextManager:
    def __enter__(self):
        print("__enter__")
    def __exit__(self, exception_type, exception_value, traceback):
        print("__exit__")

        if exception_type is None:
            print("正常終了")
        else:
            print(f"例外あり. {exception_value}, {traceback}")

```


```python
with SampleContextManager():
    print("ラップされた処理")
```

    __enter__
    ラップされた処理
    __exit__
    正常終了
    


```python
with SampleContextManager():
    print("ラップされた処理")
    raise RuntimeError()
```

    __enter__
    ラップされた処理
    __exit__
    例外あり. , <traceback object at 0x00000277D16C6DC0>
    


    ---------------------------------------------------------------------------

    RuntimeError                              Traceback (most recent call last)

    Cell In[7], line 3
          1 with SampleContextManager():
          2     print("ラップされた処理")
    ----> 3     raise RuntimeError()
    

    RuntimeError: 


また、`__enter__`に戻り値を与えると、asを使って変数に設定できる。通常はselfをreturnするケースが多い。


```python
class SampleContextManager:
    def __enter__(self):
        print("__enter__")
        return self
    def __exit__(self, exception_type, exception_value, traceback):
        print("__exit__")

        if exception_type is None:
            print("正常終了")
        else:
            print(f"例外あり. {exception_value}, {traceback}")

with SampleContextManager() as context_manager:
    print(context_manager)
    print("ラップされた処理")
```

    __enter__
    <__main__.SampleContextManager object at 0x00000277D1582520>
    ラップされた処理
    __exit__
    正常終了
    

### コンテキストマネージャを実装する（関数として）

contextlibモジュールを使うことで、関数としてコンテキストマネージャを実装できる。

もっとも便利で使用されるのは、contextmanagerデコレータである。

このデコレータで実装すると、yieldが入った関数をを作成するのみで、`__enter__`と`__exit__`の動作を実装できる。


```python
from contextlib import contextmanager

@contextmanager
def sample_context_manager():
    print("__enter__")

    try:
        yield
    except Exception as e:
        print("__exit__")
        print(f"例外あり. {e}")
        raise # 例外は再送出が必要となる
    else:
        print("__exit__")
        print("正常終了")
```


```python
with sample_context_manager():
    print("ラップされた処理")
```

    __enter__
    ラップされた処理
    __exit__
    正常終了
    


```python
with sample_context_manager():
    print("ラップされた処理")
    raise RuntimeError()
```

    __enter__
    ラップされた処理
    __exit__
    例外あり. 
    


    ---------------------------------------------------------------------------

    RuntimeError                              Traceback (most recent call last)

    Cell In[21], line 3
          1 with sample_context_manager():
          2     print("ラップされた処理")
    ----> 3     raise RuntimeError()
    

    RuntimeError: 


yieldに戻り値を持たせれば、asで受け取ることが可能。


```python
from contextlib import contextmanager

@contextmanager
def sample_context_manager():
    print("__enter__")
    ret_val = 100

    try:
        yield ret_val
    except Exception as e:
        print("__exit__")
        print(f"例外あり. {e}")
        raise # 例外は再送出が必要となる
    else:
        print("__exit__")
        print("正常終了")
```


```python
with sample_context_manager() as val:
    print("ラップされた処理")
    print(val)
```

    __enter__
    ラップされた処理
    100
    __exit__
    正常終了
    

### contextlibモジュールのその他のヘルパー

- closing(element)

close関数のあるオブジェクトをelementに与えると、自動でクローズ処理を行ってくれるコンテキストマネージャになる。


```python
import contextlib

class SampleClass():
    def __init__(self):
        self.__is_open = True
    def close(self):
        self.__is_open = False
    def is_open(self):
        return self.__is_open

with contextlib.closing(SampleClass()) as f:
    print(f.is_open())
print(f.is_open())

```

    True
    False
    

- suppress(*exception)

指定した例外をにぎりつぶすコンテキストマネージャを作ることができる。


```python
with contextlib.suppress(RuntimeError):
    raise RuntimeError
```

- redirect_stdout(new_target)とredirect_stderr(new_target)

ブロック内のstdoutとstderrを、new_targetにリダイレクトできる。new_targetはファイルやストリームを指定できる。


```python
import contextlib

with open("log.txt", "wt") as f:
    with contextlib.redirect_stdout(f):
        print("hogehoge")
```

`io.StringIO`などのストリームを使う例は以下の通り。


```python
import io

with io.StringIO() as f:
    with contextlib.redirect_stdout(f):
        print("hogehoge")
    print(f.getvalue())
```

    hogehoge
    
    

- ExitStack

複数のコンテキストを扱うために用意されている。stackに`enter_context`すれば、すべての終了処理が走る。


```python
from contextlib import contextmanager

@contextmanager
def sample_context_manager():
    print("__enter__")
    ret_val = 100

    try:
        yield ret_val
    except Exception as e:
        print("__exit__")
        print(f"例外あり. {e}")
        raise # 例外は再送出が必要となる
    else:
        print("__exit__")
        print("正常終了")

with contextlib.ExitStack() as stack:
    hoge = stack.enter_context(sample_context_manager())
    fuga = stack.enter_context(sample_context_manager())
    print("ブロック内の処理")
```

    __enter__
    __enter__
    ブロック内の処理
    __exit__
    正常終了
    __exit__
    正常終了
    

複数コンテキストを動かす方法は、withに複数書くのでも実はできる。


```python
with sample_context_manager() as hoge, sample_context_manager() as fuga:
    print("ブロック内の処理")
```

    __enter__
    __enter__
    ブロック内の処理
    __exit__
    正常終了
    __exit__
    正常終了
    

また、Python 3.10からは、以下のような括弧書きができるようになっている（3.9でも動くが、3.10で正式対応らしい。なので3.8では動かない）


```python
with (
    sample_context_manager() as hoge
    , sample_context_manager() as fuga
):
    print("ブロック内の処理")
```

    __enter__
    __enter__
    ブロック内の処理
    __exit__
    正常終了
    __exit__
    正常終了
    

### 演習問題

演習１：

### 参考

- 書籍 : エキスパートPythonプログラミング改訂3版 3.4.4 コンテキストマネージャ
- [Pythonのcontextlibでwithに渡せる処理を定義する - iMind Developers Blog](https://blog.imind.jp/entry/2019/07/06/144729)

以上。
