<a href="https://colab.research.google.com/github/nokomoro3/book-ml-transformers/blob/main/ml-transformers-chap01-introduction.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# mutableと参照渡し（浅いコピー）

## mutableなものを浅いコピーした場合の注意点

### 現象：変更が元の変数にも影響する

ここまで見てきたように、list型とdict型はmutableである。

またPythonでは、変数で別の変数にイコールで代入すると、必ず参照渡し（浅いコピー）となる。

mutableなものが参照渡しされた場合、コピー先の変数を変更すると、コピー元の変数も変わるという現象に注意が必要。

参照渡を厳密にチェックするために、オブジェクトIDを`id`で確認して、サンプルを実行する。


```python
sample_list = ["A", "B", "C"]
print(id(sample_list))

print(f"{id(sample_list):016x}") 

sample_list_ref = sample_list
print(f"{id(sample_list_ref):016x}") 
```

    2399533861760
    0000022eaf5d0b80
    0000022eaf5d0b80
    

この場合に、コピーされた側を変更すると、元の変数も変更される。


```python
sample_list_ref.append("D")
print(sample_list_ref)

print(sample_list)
```

    ['A', 'B', 'C', 'D']
    ['A', 'B', 'C', 'D']
    

dictでも同様


```python
sample_dict = {"A": 100, "B": 200}
print(f"{id(sample_dict):016x}")

sample_dict_ref = sample_dict
print(f"{id(sample_dict_ref):016x}")

sample_dict_ref["C"] = 300
print(sample_dict_ref)

print(sample_dict)
```

    0000022eaf5f7140
    0000022eaf5f7140
    {'A': 100, 'B': 200, 'C': 300}
    {'A': 100, 'B': 200, 'C': 300}
    

### 対策１：`.copy()`を使う

`.copy()`で複製すると、新しいオブジェクトとなるため、編集しても影響を及ぼさなくなる。


```python
sample_list = ["A", "B", "C"]
print(f"{id(sample_list):016x}") 

sample_list_ref = sample_list.copy()
print(f"{id(sample_list_ref):016x}") 
```

    0000022eaf1cab00
    0000022eaf2fcd00
    


```python
sample_list_ref.append("D")
print(sample_list_ref)

print(sample_list)
```

    ['A', 'B', 'C', 'D']
    ['A', 'B', 'C']
    

さて、一見落着でしょうか…？どう思いますか？

次のようなlistの内部にlistがある例を見てみましょう。


```python
sample_list = [["A", "B", "C"],["D", "E", "F"]]
print(f"{id(sample_list):016x}") 

sample_list_ref = sample_list.copy()
print(f"{id(sample_list_ref):016x}")

sample_list_ref[0].append("D")
print(sample_list_ref)

print(sample_list)
```

    0000022eaf5df480
    0000022eaf6060c0
    [['A', 'B', 'C', 'D'], ['D', 'E', 'F']]
    [['A', 'B', 'C', 'D'], ['D', 'E', 'F']]
    

あれ？値の更新が影響を及ぼしている…？？

これが落とし穴でより深刻なデバッグしにくいケースになります。

`.copy()`だけでは、その要素の参照は維持されたままになるということを覚えておく必要があります。

### 対策２：`copy.deepcopy()`を使う

こういった要素の参照もきちんと別オブジェクトとしてコピーするには、copyモジュールのdeepcopyを使う必要があります。


```python
import copy

sample_list = [["A", "B", "C"],["D", "E", "F"]]
print(f"{id(sample_list):016x}") 

sample_list_ref = copy.deepcopy(sample_list)
print(f"{id(sample_list_ref):016x}")

sample_list_ref[0].append("D")
print(sample_list_ref)

print(sample_list)
```

    0000022eaf5ef300
    0000022eaf628f80
    [['A', 'B', 'C', 'D'], ['D', 'E', 'F']]
    [['A', 'B', 'C'], ['D', 'E', 'F']]
    

## immutableなものはなぜ問題ないか

immutableな変数の場合も別の変数に代入した時点では参照渡し（浅いコピー）であることには変わりがない。

以下のように同じオブジェクトを指している。


```python
sample_float = 3.14
print(f"{id(sample_float):016x}")

sample_float_copy = sample_float
print(f"{id(sample_float_copy):016x}")
```

    0000022eaf1ff8f0
    0000022eaf1ff8f0
    

ただしimmutableなため変更はできず、新しい値を与えることしかできない。（この場合オブジェクトは新規に作成される）

なので、実用上は参照渡し（浅いコピー）でも問題になることはないという話。


```python
sample_float_copy = 3.141592
print(sample_float_copy)

print(sample_float)
```

    3.141592
    3.14
    

…本当に問題ないのでしょうか？

スカラーならそうなんですが、immutableのなかでtupleというやつに気を付ける必要があります。

## immutableでも要素はmutableである場合も注意

floatと同様、変数を代入しただけでは同じオブジェクトIDを示したままです。


```python
sample_tupe = (1, 3.14, ["A", "B", "C"])
print(f"{id(sample_tupe):016x}")

sample_tupe_copy = sample_tupe
print(f"{id(sample_tupe_copy):016x}")
```

    0000022eaf61af80
    0000022eaf61af80
    

tuple自体はimmutableなのですが、その要素にlistを持たせれば要素をmutableにすることが可能です。

ですので、変数の変更が元の変数に波及させることができます。


```python
sample_tupe_copy[2].append("D")
print(sample_tupe_copy)

print(sample_tupe)
```

    (1, 3.14, ['A', 'B', 'C', 'D'])
    (1, 3.14, ['A', 'B', 'C', 'D'])
    

このケースでも、`copy.deepcopy()`を使えば解決することができます。


```python
import copy

sample_tupe = (1, 3.14, ["A", "B", "C"])
print(f"{id(sample_tupe):016x}")

sample_tupe_copy = copy.deepcopy(sample_tupe)
print(f"{id(sample_tupe_copy):016x}")

sample_tupe_copy[2].append("D")
print(sample_tupe_copy)

print(sample_tupe)
```

    0000022eaf61b2c0
    0000022eaf5d7280
    (1, 3.14, ['A', 'B', 'C', 'D'])
    (1, 3.14, ['A', 'B', 'C'])
    

## クラスの場合もmutableなので注意

自作したクラスなどの場合も、もちろんmutableになっているため、影響を与えないようにするためには`copy.deepcopy()`を使う必要があります。


```python
class Person:
    def __init__(self, age):
        self.age = age
    def set_age(self, age):
        self.age = age
    def print_age(self):
        print(f"age: {self.age}")

person_A = Person(30)
person_A.print_age()

person_B = person_A
person_B.set_age(40)
person_B.print_age()

person_A.print_age()
```

    age: 30
    age: 40
    age: 40
    


```python
import copy

person_A = Person(30)
person_A.print_age()

person_B = copy.deepcopy(person_A)
person_B.set_age(40)
person_B.print_age()

person_A.print_age()
```

    age: 30
    age: 40
    age: 30
    

## listのスライスは新しいオブジェクトになっている

当然ではあるが、スライスなどでlistの一部をコピーする場合は、新しいオブジェクトになっているため問題は発生しない。

（もちろん要素がmutableなものを含んでいる場合は、注意が必要）


```python
sample_list = [0,1,2,3,4,5,6,7,8,9]
print(f"{id(sample_list):016x}")

sample_list2 = sample_list[2:5]
print(f"{id(sample_list2):016x}")

sample_list2[0] = -1

print(sample_list2)

print(sample_list)
```

    0000023736aa6ac0
    0000023736a6e400
    [-1, 3, 4]
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    

## 教訓としては

結局のところmutableな扱いで、値を編集するのはスコープの狭い、見える範囲にとどめておく方が良い。

間違っても関数外で編集したりすることは避けるべきだろう。

クラスの場合は、避けるのが難しい実装も考えられるが、設計をきちんと行い、内部が状態が更新されても周りには影響がないような設計にすべきと考えられる。

またMLなどの場合は、モデルを複製したい場合などに`copy.deepcopy()`を使うべきかもしれない。

### 参考

- [Pythonの浅いコピーと深いコピー: copy(), deepcopy() | note.nkmk.me](https://note.nkmk.me/python-copy-deepcopy/)
