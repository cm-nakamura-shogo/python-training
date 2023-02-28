<a href="https://colab.research.google.com/github/cm-nakamura-shogo/python-training/blob/master/doc/lecture/iterator-generator/README.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# iteratorとgenerator

ここでは以下についてやります。

- iteratorとは
- iteratorとiterableの違い
- generatorとは
- yiledってなんだ？
- itertoolsの使い方

## iterator

### iteratorとは

iteratorとはイテレータプロトコルをもつコンテナのこと。`__next__`と`__iter__`というメソッドを持てはiteratorと言ってよい。

自作のiteratorの例をエキPyから持ってきた。


```python
class CountDown:
    def __init__(self, step):
        self.step = step

    def __next__(self):
        if self.step <= 0:
            raise StopIteration
        self.step -= 1
        return self.step

    def __iter__(self):
        return self
```

iteratorは以下のようにfor文でループさせることができる。ループを抜けるタイミングは、`StopIteration`という例外が投げられた時。


```python
count_down = CountDown(3)
for i in count_down:
    print(i)
```

    2
    1
    0
    

この実装では、もう一度繰り返すことはできない。


```python
for i in count_down:
    print(i)
```

繰り返し使用したい場合は、iteratorと状態を分割する。


```python
class CountState:
    def __init__(self, step):
        self.step = step

    def __next__(self):
        if self.step <= 0:
            raise StopIteration
        self.step -= 1
        return self.step

class CountDown:
    def __init__(self, step):
        self.step = step

    def __iter__(self):
        return CountState(self.step)
```


```python
count_down = CountDown(3)
for i in count_down:
    print(i)
for i in count_down:
    print(i)
```

    2
    1
    0
    2
    1
    0
    

### iteratorとiterable

これまででてきたlist, tupleなどはiterableではあるがiteratorではない。

iterableは`iter()`を使うことによりiteratorにすることができる。（iteratorは`iter()`を使ってもiteratorのまま）


```python
sample_list = [0,1,2,3,4]

iterator = iter(sample_list)

try:
    print(iterator.__next__())
    print(iterator.__next__())
    print(iterator.__next__())
    print(iterator.__next__())
    print(iterator.__next__())
    print(iterator.__next__())
except Exception as e:
    print(e)
```

    0
    1
    2
    3
    4
    
    

rangeも実はiterableであり、iteratorではない。


```python
iterable = range(5)

try:
    print(iterable.__next__())
except Exception as e:
    print(e)
```

    'range' object has no attribute '__next__'
    

iterableは、`[3]`のように要素にアクセスできる。


```python
iterable[3]
```




    3




```python
iterator = iter(iterable)
print(iterator.__next__())
```

    0
    

enumerate, zipは、iteratorである。


```python
sample_list = [5,4,3,2,1]

iterator = enumerate(sample_list)
print(iterator.__next__())
```

    (0, 5)
    


```python
sample_list = [5,4,3,2,1]
sample_list2 = [2,5,2,5,2]

iterator = zip(sample_list, sample_list2)
print(iterator.__next__())
```

    (5, 2)
    

### iteratorの要素にアクセスしたい

iteratorはiterableと違い、要素番号で以下のようにアクセスできない。


```python
sample_list = [5,4,3,2,1]

iterator = enumerate(sample_list)

try:
    iterator[3]
except Exception as e:
    print(e)
```

    'enumerate' object is not subscriptable
    

初期はこの`object is not subscriptable`が意味が分からなくてつまずくことが多い。

解決策としてはリスト内包表記で以下のように一度アンパックしてしまう。


```python
sample_list = [5,4,3,2,1]
iterator = enumerate(sample_list)
print([*iterator][3])
```

    (3, 2)
    

まとめると以下のような感じ。

- iterable
  - 要素番号`[n]`で要素アクセス可能。
  - iteratorにするためには`iter()`で囲む
  - 例は、list, tuple, dict, setなど。rangeも。
- iterator
  - 要素番号`[n]`で要素アクセス不可。アンパックして実体化が必要。
  - `iter()`で囲ってもiteratorのまま
  - 例は、zipやenumerateなど。

以下もご参考
- [4-2. イテラブルとイテレータ — Pythonプログラミング入門 documentation](https://utokyo-ipp.github.io/4/4-2.html)

## generator

generatorはyieldを伴う関数で実装されたiterator。generator iteratorと公式では呼ばれている。

以下はgeneratorでカウントダウンを実装した例。


```python
def count_down(n: int):
    count = n
    while count>0:
        count = count - 1
        yield count

for i in count_down(5):
    print(i)
```

    4
    3
    2
    1
    0
    


```python
gen = count_down(5)
print(type(gen))
```

    <class 'generator'>
    

iteratorのように`__next__()`で次のデータにアクセスが可能。


```python
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
```

    4
    3
    2
    1
    0
    

generatorはpathlibのglobなどはその実装例である。


```python
import pathlib
gen = pathlib.Path(".").glob("**/*")
print(type(gen))
```

    <class 'generator'>
    

generatorもiteratorの一種であるので、要素へ直接アクセスできない。


```python
gen = count_down(5)
try:
    print(gen[3])
except Exception as e:
    print(e)
```

    'generator' object is not subscriptable
    

iterator同様、要素にアクセスするにはアンパックして実体化させる。


```python
gen = count_down(5)
print([*gen][3])
```

    1
    

### generatorのメリット

いくつかgeneratorのメリットを整理しておく

- generatorは単なる関数なので、容易に実装可能
- メモリにすべてのデータを置く必要がないためメモリ効率がよい（？）
- 上記のため、無限長のiteratorを作成することも可能（？）
- 後述のsendを使ってgenerator側と対話ができる。

ただし通常のiteratorも実装次第では、2,3番目の特性を持つので特有のメリットではないように思える。

4番目の特性も、自身でAPIを作成すれば実装できる。

なので本質的にはそれらを簡易に書けるという1番目の特性がメリットかなと考える。

### generatorのsend処理

generatorはsend処理をすることにより、generator側に値を返すことができる。


```python
def count_down(n: int):
    count = n
    while count>0:
        count = count - 1
        send_value = yield count
        print(f"{send_value=}")

gen = count_down(5)
print(f"{gen.__next__()=}")
print(f"{gen.__next__()=}")
print(f"{gen.send('hoge')=}")
print(f"{gen.send('fuga')=}")
```

    gen.__next__()=4
    send_value=None
    gen.__next__()=3
    send_value='hoge'
    gen.send('hoge')=2
    send_value='fuga'
    gen.send('fuga')=1
    

sendでも__next__のように一つ先に進むので送った後に結果を得るという形になります。

なお、何もsendしていない場合は`None`となっていることが分かる。

### generatorのreturn

generatorでreturnをすると、強制的に終了される。

またreturnすることで、値を`StopIteration`に含めることができる。


```python
def count_down(n: int):
    count = n
    while count>0:
        if count % 2 == 0:
            return "finish"
        count = count - 1
        yield count

try:
    gen = count_down(5)
    print(f"{gen.__next__()=}")
    print(f"{gen.__next__()=}")
except Exception as e:
    print(e)
```

    gen.__next__()=4
    finish
    

### まとめ

- generatorはyieldで値を逐次生成する。
- generatorは関数で実装できるためiteratorよりも簡単に作成できる。
- generatorはiteratorと同様要素のアクセスにアンパックが必要。
- generatorの型には、YieldType, SendType, ReturnTypeがある。

ここら辺の話は以下もご参考

- [Pythonのジェネレータってyieldするだけじゃなかったんだね](https://zenn.dev/alivelimb/articles/20220505-typing-generator)

## itertools

累積和、グループ化、順列、組み合わせなどが求められる。

- [すごいぞitertoolsくん - Qiita](https://qiita.com/anmint/items/37ca0ded5e1d360b51f3)

網羅するならば以下。

- [itertools --- 効率的なループ実行のためのイテレータ生成関数 — Python 3.11.1 ドキュメント](https://docs.python.org/ja/3/library/itertools.html)

itertoolsは基本的にはイテレータを返す。実例を見ていく。

### accumulate : 累積和


```python
import itertools

print([*itertools.accumulate([1,2,3,4,5])])
```

    [1, 3, 6, 10, 15]
    

### chain, chain.from_iterable : 複数のiterableをつなげる。


```python
print([*itertools.chain([1,2,3],[4,5,6])])
```

    [1, 2, 3, 4, 5, 6]
    


```python
print([*itertools.chain.from_iterable([[1,2,3],[4,5,6]])])
```

    [1, 2, 3, 4, 5, 6]
    

### compress : フラグでselectする。


```python
print([*itertools.compress([1,2,3,4,5], [1,0,0,1,1])])
```

    [1, 4, 5]
    

### takewhile, dropwhile : 要素を先頭から辿り、要素が偽になるまで、と偽になった後をそれぞれ抽出する。


```python
print([*itertools.takewhile(lambda x: x!=10, [1,2,3,10,4,3,2,10])])
```

    [1, 2, 3]
    


```python
print([*itertools.dropwhile(lambda x: x!=10, [1,2,3,10,4,3,2,10])])
```

    [10, 4, 3, 2, 10]
    

### filterfalse : 偽になる要素を抽出


```python
print([*itertools.filterfalse(lambda x: x%2==0, [1,2,3,4,5])])
```

    [1, 3, 5]
    

### groupby : 連続した同一要素をグループ化する。


```python
for val, it in itertools.groupby([1,2,2,3,3,3,2,2,2,2,1,1,1,1,1]):
    print(f"{val=}, {[*it]=}")
```

    val=1, [*it]=[1]
    val=2, [*it]=[2, 2]
    val=3, [*it]=[3, 3, 3]
    val=2, [*it]=[2, 2, 2, 2]
    val=1, [*it]=[1, 1, 1, 1, 1]
    

islice : 普通のスライスと同じ。負のindexが使えないので、あまり使うことはない気がする。


```python
print([*itertools.islice([1,2,3,4,5], 1, 4, 2)])
```

    [2, 4]
    

### pairwise : 先頭から2個ずつ取ってくる。これは3.10以降でしか使えない


```python
# print([*itertools.pairwise([1,2,3,4,5,6])])
```

### starmap : ある関数と引数の組で一括処理する。


```python
print([*itertools.starmap(lambda x,y: x+y, [[1,2],[2,3],[3,4]])])
```

    [3, 5, 7]
    

### tee : iterableをn個のiteratorで生成する。複数回iteratorとして使いたいものがある場合に有効。

通常はiteratorは１回iterationすると再度iterationできない。


```python
it = itertools.accumulate([1,2,3,4,5])
print([*it])
print([*it])
```

    [1, 3, 6, 10, 15]
    []
    

これをteeで複数回やることが可能。


```python
for it in itertools.tee(itertools.accumulate([1,2,3,4,5]), 3):
    print([*it])
```

    [1, 3, 6, 10, 15]
    [1, 3, 6, 10, 15]
    [1, 3, 6, 10, 15]
    

### zip_longest : 長さの違うzipを長い方に併せてiterationする。短い側を何で埋めるかは指定可能。


```python
for i in itertools.zip_longest([1,2,3,4,5],"abcdefg", "12345678", fillvalue=-1):
    print(i)
```

    (1, 'a', '1')
    (2, 'b', '2')
    (3, 'c', '3')
    (4, 'd', '4')
    (5, 'e', '5')
    (-1, 'f', '6')
    (-1, 'g', '7')
    (-1, -1, '8')
    

### itertoolsのiteratorは元リストの参照を持っている

基本的に、itertoolsのiteratorは元リストを参照する形で見ている点は注意が必要である。teeなどで複数回使う場合も同様。


```python
sample_list = [1,2,3,4,5]
iters = itertools.accumulate(sample_list)
print([*iters])
iters = itertools.accumulate(sample_list)
sample_list.append(6)
print([*iters])
```

    [1, 3, 6, 10, 15]
    [1, 3, 6, 10, 15, 21]
    

### product : 総当たり


```python
print([*itertools.product([1,2,3], [4,5,6])])
```

    [(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]
    

### permutations : 順列


```python
print([*itertools.permutations([1,2,3,4], 3)])
```

    [(1, 2, 3), (1, 2, 4), (1, 3, 2), (1, 3, 4), (1, 4, 2), (1, 4, 3), (2, 1, 3), (2, 1, 4), (2, 3, 1), (2, 3, 4), (2, 4, 1), (2, 4, 3), (3, 1, 2), (3, 1, 4), (3, 2, 1), (3, 2, 4), (3, 4, 1), (3, 4, 2), (4, 1, 2), (4, 1, 3), (4, 2, 1), (4, 2, 3), (4, 3, 1), (4, 3, 2)]
    

### combination : 組み合わせ


```python
print([*itertools.combinations([1,2,3,4], 3)])
```

    [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]
    

### combinations_with_replacement : 再利用ありの組み合わせ


```python
print([*itertools.combinations_with_replacement([1,2,3,4], 3)])
```

    [(1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 1, 4), (1, 2, 2), (1, 2, 3), (1, 2, 4), (1, 3, 3), (1, 3, 4), (1, 4, 4), (2, 2, 2), (2, 2, 3), (2, 2, 4), (2, 3, 3), (2, 3, 4), (2, 4, 4), (3, 3, 3), (3, 3, 4), (3, 4, 4), (4, 4, 4)]
    

### count : カウントアップする。無限iteratorである。


```python
count = 5
for i in itertools.count(5, 2):
    print(i)
    count = count - 1
    if count == 0:
        break
```

    5
    7
    9
    11
    13
    

### cycle : シーケンスを繰り返す。無限iteratorである。


```python
count = 10
for i in itertools.cycle([1,2,3]):
    print(i)
    count = count - 1
    if count == 0:
        break
```

    1
    2
    3
    1
    2
    3
    1
    2
    3
    1
    

### repeat : 一定値を繰り返す。n未設定の場合は無限iteratorである。


```python
for i in itertools.repeat(1, 5):
    print(i)
```

    1
    1
    1
    1
    1
    
