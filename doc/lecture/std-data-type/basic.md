<a href="introduction.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# 基本のデータ型

## データ型一覧

一覧については以下を一読

- [図解！Python データ型を徹底解説！(確認・変換・指定方法と種類一覧) - AI-interのPython3入門](https://ai-inter1.com/python-data_type/)

記載の通りだが、以下のような認識。

- スカラーとしてはint, float, bool
- 複数の値を持つデータ構造としてはlist, tuple, float, set
  - あれ上のリンクにはsetなかったな…
- strはちょっと特殊

## データ型の確認方法

以下のように`type`で確認する


```python
sample_val = 3.14
type(sample_val)
```




    float



## listについて

### listの基本操作

基本は以下を参照

- [list(リスト)型の更新と削除 | Python学習講座](https://www.python.ambitious-engineer.com/archives/137)

要素の追加方法は`append`以外にも`extend`もある。破壊的変更なので注意。


```python
sample_list = ["A", "B"]

# 要素を追加
sample_list.append("C")
print(sample_list)

# 複数を追加する場合はこちら
sample_list.extend(["D","E"])
print(sample_list)
```

    ['A', 'B', 'C']
    ['A', 'B', 'C', 'D', 'E']
    

破壊的変更をしないためには、後述のアンパックを駆使して新しいオブジェクトを作る方が良い。


```python
sample_list = ["A", "B"]

# 要素を追加
sample_list = [*sample_list, "C"]
print(sample_list)

# 複数を追加する場合はこちら
sample_list = [*sample_list, *["D", "E"]]
print(sample_list)
```

    ['A', 'B', 'C']
    ['A', 'B', 'C', 'D', 'E']
    

### listのスライス

スライスについては以下の通り。


```python
sample_list = [0,1,2,3,4,5,6,7,8,9]

print(sample_list[2:5])

print(sample_list[:5])

print(sample_list[1:-1])

print(sample_list[::2])

print(sample_list[::3])
```

    [2, 3, 4]
    [0, 1, 2, 3, 4]
    [1, 2, 3, 4, 5, 6, 7, 8]
    [0, 2, 4, 6, 8]
    [0, 3, 6, 9]
    

### listのソート

ソートには`sort`と`sorted`があり、それぞれ破壊的変更とそうではないものなので注意する。


```python
sample_list = [1,5,2,3,6,1,5,8]
sample_list.sort()
print(sample_list)

sample_list = [1,5,2,3,6,1,5,8]
sample_list_sorted = sorted(sample_list)

print(sample_list)
print(sample_list_sorted)
```

    [1, 1, 2, 3, 5, 5, 6, 8]
    [1, 5, 2, 3, 6, 1, 5, 8]
    [1, 1, 2, 3, 5, 5, 6, 8]
    

### listのアンパック

listの要素をアンパック（カッコを外すイメージ）するためには、アスタリスクを使う。


```python
sample_list1 = ["A", "B"]
sample_list2 = ["C", "D", "E"]
sample_list = [sample_list1, sample_list2]
print(sample_list)

sample_list = [*sample_list1, *sample_list2]
print(sample_list)
```

    [['A', 'B'], ['C', 'D', 'E']]
    ['A', 'B', 'C', 'D', 'E']
    

アンパックは関数の引数（キーワード無し）としても展開できる。

あまる部分にもアンパックを記述することで、tupleとして取得できる。


```python
print(sample_list)

def main(v1, v2, *args):
    print(v1, v2)
    print(args)
    print(type(args))

main(*sample_list)
```

    ['A', 'B', 'C', 'D', 'E']
    A B
    ('C', 'D', 'E')
    <class 'tuple'>
    

### listの要素の型一貫性

listは要素の値が異なっても一つにまとめることが一応できてしまう。


```python
sample_list = ["A", "B", 100, 10.112]
print(sample_list)
```

    ['A', 'B', 100, 10.112]
    

ただし使い方としてはお勧めできないので、基本的にはやらない。

こういったものを入れるのは後述するtupleの方が適切。

やる必要がある場合はたぶん設計が何かおかしいので見直すこと。

(スコープが5行程度の狭い変数であれば、まあありかもしれないが。)

## dictについて

### dictの基本操作

以下のようにすれば要素を追加できる。ただし破壊的変更となるので注意。


```python
sample_dict = {"A": 100, "B": 200, "C": 300}
sample_dict["D"] = 400

print(sample_dict)
```

    {'A': 100, 'B': 200, 'C': 300, 'D': 400}
    

破壊的変更を避けるためには、後述するアンパックをうまく活用すれば可能。


```python
sample_dict = {"A": 100, "B": 200, "C": 300}
sample_dict = {**sample_dict, "D": 400}

print(sample_dict)
```

    {'A': 100, 'B': 200, 'C': 300, 'D': 400}
    

その他、基本操作は以下の通り。

updateなどを使う方法やアンパックを使う方法でマージできる。

- [Pythonで辞書に要素を追加、辞書同士を連結（結合） | note.nkmk.me](https://note.nkmk.me/python-dict-add-update/)

こちらは削除方法。

- [Pythonで辞書の要素を削除するclear, pop, popitem, del | note.nkmk.me](https://note.nkmk.me/python-dict-clear-pop-popitem-del/)

アンパックでマージする場合、後にある方が優先っぽい。


```python
sample_dict1 = {"A": 100, "B": 200, "C": 300}
sample_dict2 = {"A": 1000, "B": 2000, "C": 3000}

sample_dict = {**sample_dict1, **sample_dict2}
print(sample_dict)
```

    {'A': 1000, 'B': 2000, 'C': 3000}
    

### dictのアンパック

dict型はアスタリスクを２個でアンパックできる。（ちなみに１個にするとkeyのアンパックとなる）


```python
sample_dict = {"A": 100, "B": 200, "C": 300}

sample_dict = {**sample_dict, "D": 400}
print(sample_dict)
```

    {'A': 100, 'B': 200, 'C': 300, 'D': 400}
    

アンパックは、関数のキーワード引数にすることが可能。

あまる部分を受け取るためには、引数にもアンパックを記述しておけばよい。あまる部分はdictとして取得可能。


```python
def main(B, D, **kwargs):
    print(B, D)
    print(kwargs)

main(**sample_dict)
```

    200 400
    {'A': 100, 'C': 300}
    

### dictの要素一覧取得方法

items, keys, valuesという種類の取得方法がある。


```python
sample_dict = {"A": 100, "B": 200, "C": 300}

print([*sample_dict.items()])

print([*sample_dict.keys()])

print([*sample_dict.values()])
```

    [('A', 100), ('B', 200), ('C', 300)]
    ['A', 'B', 'C']
    [100, 200, 300]
    

### dictの順序性

要素の順番を保持したい場合は、OrderedDictを使用する必要があった。

- [Pythonの順序付き辞書OrderedDictの使い方 | note.nkmk.me](https://note.nkmk.me/python-collections-ordereddict/)
- [Python 3.7でdictが順序を保存するようになって良かったとしみじみ思う - Qiita](https://qiita.com/tonluqclml/items/db797d9ad03604ae489c)

実際にはPython3.7以降では順番を保持する実装となっている。

## tupleについて詳しく

### tupleの基本操作

tupleはdict, listと違いimmutableとなっている。


```python
sample_tuple = (1, "A", 3.14)
print(type(sample_tuple))
print(sample_tuple)
```

    <class 'tuple'>
    (1, 'A', 3.14)
    

要素へのアクセスは、リストと同じような形で可能。


```python
print(sample_tuple[1])
```

    A
    

関数の戻り値に複数記載する際に、tupleをよく見ることになる。


```python
def main():
    return 1,2,3,4,5

ret_val = main()
print(type(ret_val))
```

    <class 'tuple'>
    

### tupleのアンパック

リストと同じようなアンパックとなる。アンパックによりリストに変換することが可能。


```python
sample_tuple2 = [*sample_tuple]
print(sample_tuple2)
```

    [1, 'A', 3.14]
    

tupleはlistと同じように分解やスライスが可能。


```python
sample_tuple = [1,2,3,4,5]

A, *B, C = sample_tuple
print(A)
print(B)
print(C)

print(sample_tuple[1:3])
```

    1
    [2, 3, 4]
    5
    [2, 3]
    

ただし分解結果はlistになるので注意が必要。

## setについて

### setの基本操作

setは集合を扱うデータ型です。集合ですので重複を削除した操作をする際に便利になります。


```python
sample_set = set([1,2,3])
print(type(sample_set))
print(sample_set)
```

    <class 'set'>
    {1, 2, 3}
    

リストからセットを作成する際は`set()`を使えばOKです。


```python
sample_list = [1,2,3,3,3,4,4,4,5]
sample_set = set(sample_list)
print(sample_set)
```

    {1, 2, 3, 4, 5}
    

更新にはupdateが便利です。(addもあるが、要素数が１つの場合しか使えない)


```python
sample_set = set([1,2,3])

sample_set.update([2,3,4])
print(sample_set)
```

    {1, 2, 3, 4}
    

ただし破壊的変更になるので、後述する和集合を使ってやる方が分かりやすい可能性があります。


```python
sample_set = set([1,2,3])

sample_set = sample_set | set([2,3,4])

print(sample_set)
```

    {1, 2, 3, 4}
    

### setの集合演算

集合に関する演算が可能です。


```python
s1 = set([10, 20, 30, 40, 50])
s2 = set([10, 30, 50, 70, 90])
s3 = set([10, 20, 30])

print(s1 | s2) # 和集合
print(s1 & s2) # 積集合
print(s1 - s2) # 差集合
```

    {70, 40, 10, 50, 20, 90, 30}
    {10, 50, 30}
    {40, 20}
    

subsetかsupersetかなどの判断も可能です。


```python
print(s3.issubset(s1))
print(s3.issubset(s2))
print(s1.issuperset(s3))
```

    True
    False
    True
    
