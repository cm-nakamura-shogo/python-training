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

## namedtuple

dictの代わりに使い、immutableなので変更不可能なdictとして使用できる。

- [namedtupleで美しいpythonを書く！（翻訳） - Qiita](https://qiita.com/Seny/items/add4d03876f505442136)


```python
from collections import namedtuple
Car = namedtuple('Car', ['color', 'mileage'])
car = Car("red", 3812.4)
car
```




    Car(color='red', mileage=3812.4)



アクセスに`.`が使用可能。つまりIDEの補完が効く


```python
print(f"{car.color=}, {car.mileage=}")
```

    car.color='red', car.mileage=3812.4
    

`getattr`でもアクセス可能。


```python
print(f"{getattr(car, 'color')=}, {getattr(car, 'mileage')=}")
```

    getattr(car, 'color')='red', getattr(car, 'mileage')=3812.4
    

dictのようなアクセスはできない点のは注意。


```python
car["color"], car["mileage"]
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[20], line 1
    ----> 1 car["color"], car["mileage"]
    

    TypeError: tuple indices must be integers or slices, not str


アンパックもできる。


```python
print(*car)
```

    red 3812.4
    

tupleと同様にimmutableなので要素を書き換えることはできない。


```python
try:
    car.color = "blue"
except Exception as e:
    print(e)
```

    can't set attribute
    

インデックスでもアクセス可能で、`tuple()`に変換することも可能。


```python
print(f"{car[0]=}, {car[1]=}")

print(f"{tuple(car)=}")
```

    car[0]='red', car[1]=3812.4
    tuple(car)=('red', 3812.4)
    

listよりtuple、dictよりnamedTupleを積極的に使用することで、immutableな変数でのプログラミングが実現できる。

## deque

スタックとキューに必要な操作を備えた両端キューです。これはリストに似たコレクションですが、リストの先頭と末尾への高速な追加、削除を行うことができます。

とあるので、先頭と末尾の編集が多いデータ型には使える。この性質のためパフォーマンス重視であり、リスト同様mutableである。


```python
from collections import deque

d = deque([0,1,2])
print(f"{d=}")

d.append(3)
print(f"{d=}")

d.appendleft(-1)
print(f"{d=}")

d.extend([4,5,6]) # 複数要素を追加
print(f"{d=}")

d.extendleft([-4,-3,-2]) # 複数要素を追加
print(f"{d=}")

v = d.pop() # 末尾から取り出す
print(f"{v=}, {d=}")

v = d.popleft() # 先頭から取り出す
print(f"{v=}, {d=}")

d.rotate(2) # ずらす
print(f"{d=}")

d.rotate(-2) # ずらす
print(f"{d=}")

d = deque([*d], maxlen=3) # 最後の3つで制限される
print(f"{d=}")
```

    d=deque([0, 1, 2])
    d=deque([0, 1, 2, 3])
    d=deque([-1, 0, 1, 2, 3])
    d=deque([-1, 0, 1, 2, 3, 4, 5, 6])
    d=deque([-2, -3, -4, -1, 0, 1, 2, 3, 4, 5, 6])
    v=6, d=deque([-2, -3, -4, -1, 0, 1, 2, 3, 4, 5])
    v=-2, d=deque([-3, -4, -1, 0, 1, 2, 3, 4, 5])
    d=deque([4, 5, -3, -4, -1, 0, 1, 2, 3])
    d=deque([-3, -4, -1, 0, 1, 2, 3, 4, 5])
    d=deque([3, 4, 5], maxlen=3)
    

以下をご参考

- [Python dequeのメソッド、使いどころ](https://qlitre-weblog.com/python-deque-how-to-use/)

## ChainMap

これは辞書のようなクラスで、複数の辞書をまとめて1 つの辞書に見せるビューを作成します。


```python
from collections import ChainMap

d1 = {'A': 1, 'B':2}
d2 = {'C': 3, 'D':4}
cm = ChainMap(d1, d2)

d2["E"] = 5
print(f"{cm['E']=}")
```

    cm['E']=5
    

重複するキーがある場合、手前の辞書にある要素が優先される


```python
d2["A"]=0
print(f"{cm['A']=}")
```

    cm['A']=1
    

dictと同様に、`items()`, `keys()`, `values()`が使用可能。まあそこまで使いどころは思いつかない。

## Counter

hashable なオブジェクトの個数をカウントするための辞書のサブクラスです。

要素数をカウントするのに使用可能。


```python
from collections import Counter
a = ['a', 'b', 'c', 'd', 'a', 'a', 'b']
c = Counter(a)
print(c)
```

    Counter({'a': 3, 'b': 2, 'c': 1, 'd': 1})
    

Counterは辞書型として扱える。


```python
print(f"{c['a']=}")
```

    c['a']=3
    

`most_common()`で多い順にならんだtupleのリストを得られる。


```python
c.most_common()
```




    [('a', 3), ('b', 2), ('c', 1), ('d', 1)]



参考

- [【Python】リストの要素の数え上げ、collections.Counterの使い方 - Qiita](https://qiita.com/ell/items/259388b511e24625c0d7)

## OrderedDict

要素が追加された順序を管理し変更できる、辞書のサブクラスです。

Python 3.6以降はdictが順番を保持しているので使用頻度は高くない。以下のような場合に使用するかも。

- ある指定した位置に要素を追加したい場合
- `move_to_end`などは独自メソッド

参考

- [Pythonの順序付き辞書OrderedDictの使い方 | note.nkmk.me](https://note.nkmk.me/python-collections-ordereddict/)

## defaultdict

要素が見つからなかったときに指定された関数を呼び出して初期値を自動作成する、辞書のサブクラスです。


```python
from collections import defaultdict

keys = ["A", "B", "C", "D"]

d = defaultdict(int)

for key in keys:
    d[key] += 1

print(d)
```

    defaultdict(<class 'int'>, {'A': 1, 'B': 1, 'C': 1, 'D': 1})
    

`int`だとintの0がデフォルトになる。このほか、float()、list()、dict()が使える。


```python
from collections import defaultdict

keys = ["A", "B", "C", "D"]

d = defaultdict(dict)

for key in keys:
    d[key]["aaa"] = 100

print(d)
```

    defaultdict(<class 'dict'>, {'A': {'aaa': 100}, 'B': {'aaa': 100}, 'C': {'aaa': 100}, 'D': {'aaa': 100}})
    

初期化についてはlambda式や関数を使用できる。


```python
from collections import defaultdict

keys = ["A", "B", "C", "D"]

d = defaultdict(lambda: {"bbb": 200})

for key in keys:
    d[key]["aaa"] = 100

print(d)
```

    defaultdict(<function <lambda> at 0x000001F9CF0B5F70>, {'A': {'bbb': 200, 'aaa': 100}, 'B': {'bbb': 200, 'aaa': 100}, 'C': {'bbb': 200, 'aaa': 100}, 'D': {'bbb': 200, 'aaa': 100}})
    

ただしlambda を利用している defaultdict の場合、そのままではpickleなどでシリアライズできないため注意。

以下ご参考

- [Python defaultdict の使い方 - Qiita](https://qiita.com/xza/items/72a1b07fcf64d1f4bdb7)



