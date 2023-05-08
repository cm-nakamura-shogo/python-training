<a href="https://colab.research.google.com/github/cm-nakamura-shogo/python-training/blob/master/doc/lecture/lambda/README.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# lambda式と高階関数

ここでは以下についてやります。

- ラムダ式ってなんぞ？
- map, filter, reduceなどの高階関数の使い方
- maxやsortedなどその他の高階関数

高階関数とは関数を引数にとる関数のことと理解すればOK。

> 高階関数（higher-order function）っていうのは、他の関数を引数として受け取ったり、<br>
> 結果として関数を返す関数のことにゃん。<br>
> プログラミング言語によっては、無名関数（ラムダ式）と一緒に使うことが多いにゃん。<br>
> たとえば、JavaScriptやTypeScriptにおける高階関数でよく使われる例は、<br>
> 配列の`.map()`や`.filter()`といったメソッドにゃん。<br>
> これらのメソッドは関数を引数に取り、配列の各要素に対して何らかの処理を実行したり、<br>
> 特定の条件を満たした要素だけ抽出したりするために使われるにゃん。<br>


## lambda式

すでにでてきてるかもしれませんが、無名関数とも呼ばれます。

よくmapなどと組み合わせて使用されたり、pandasだとapplyでユーザ定義関数を使う場合に見られます。

簡易な例ですが、以下のような感じで作ります。


```python
def myfunc(func_conv, input):
    return func_conv(input)

ret_val = myfunc(lambda x: x+1, 100)

print(f"{ret_val=}")
```

    ret_val=101
    

引数を2個にしたい場合は以下のようにカンマ区切りで設定します。


```python
def myfunc(func_conv, x, y):
    return func_conv(x, y)

ret_val = myfunc(lambda x,y: x+y, 100, 1)

print(f"{ret_val=}")
```

    ret_val=101
    

lambda式は簡単な処理の関数をサクッと作成したい場合に使います。

複数行の実行処理をもてないため、複雑な処理を行うことはできません。

ちなみに、ここで作ったmyfuncのように関数を引数にもつ関数を、高階関数と呼ぶようです。

以降のmap, filter, reduceはそれも高階関数になります。

## map, filter, reduceについて

map, filter, reduceはlistなどのiterableに対する処理を行います。

mapは全要素に同じ操作を、filterはある条件での抽出操作を、reduceはなんでもできます。

なお、同名の処理はJavaScriptでも出没するので覚えておいておくと後々役立ちます。

特にreduceはこの機会にマスターしましょう。（mapとfilterはそもそもそんなにむずくない）

### map

全要素に同じ操作を実施します。戻り値はiteratorになっているので、アンパックで実体化すると値が取れます。


```python
it = map(lambda x: x+1, [1,2,3,4,5])

print([*it])
```

    [2, 3, 4, 5, 6]
    

iterableを複数渡すと、入力を複数取ることが可能です。その場合lambda式も引数が2個必要になります。

（ちなみに長さが違う場合は、短い方に合わせられます）


```python
it = map(lambda x,y: x+y, [1,2,3,4,5], [5,5,5,5,5])

print([*it])
```

    [6, 7, 8, 9, 10]
    

むろん、lambda式ではなく普通の関数を使ってもできます。


```python
def myfunc(x,y):
    return x+y

it = map(myfunc, [1,2,3,4,5], [5,5,5,5,5])

print([*it])
```

    [6, 7, 8, 9, 10]
    

まあでも関数型で副作用のないデータ変換を実施する際にmapなどを使うため、lambda式で書けるような変換の用途の方が向いているともいえる。

starmapとmapの違い


```python
import itertools

list(itertools.starmap(pow, [[2,3],[3,4],[4,5]]))
```




    [8, 81, 1024]




```python
list(map(pow, [2,3,4],[3,4,5]))
```




    [8, 81, 1024]



### filter

要素を抽出する処理です。


```python
it = filter(lambda x: x % 2==0, [1,2,3,4,5])

print([*it])
```

    [2, 4]
    

逆のfalsefilterというものが、iteratortoolsにありましたね。

こういった処理は、リスト内包表記で同じことができるためどっちが良いのかって話はあるかなと思いますが、どうでしょう？

### reduce

reduceはさまざまな変換を書くことができます。

mapやfilterの代用も可能です。ただし返ってくるのがiteratorではなく、iterableになる点が注意が必要です。

そのため唯一代用できないことは、無限シーケンスに対して動作させることができない点です（mapとfilterは無限シーケンスでも動作可能）

reduceは関数、入力シーケンス、初期値を与えます。

関数の引数は２個必要なのがポイントです。関数は順次先頭から要素を処理し、前回の処理結果を引き継ぎます。

前回の結果は、関数は第一引数に格納され、第二引数がシーケンスの現在の要素の入力になります。

そのため、第一引数の初期値がreduceの引数として必要になります（必要でないケースももちろんあります）。

これらの引数は分かりやすいようにaccとcurで書いてあることも多いです。(acc: Accumulator 累積値の意味、cur: current valueで現在の値)

以下は総和を求める処理です。


```python
from functools import reduce

sum = reduce(lambda acc, cur: acc + cur, [1,2,3,4,5], 0)
sum
```




    15



このようにreduceは処理結果が返り値になり、iteratorではありません。そのため、無限イテレータに対して使うことができません。

練習のため別の例をみてみます。全ての要素を２倍にする処理です（mapで実装するような処理）。


```python
from functools import reduce

values = reduce(lambda acc, cur: [*acc, cur*2], [1,2,3,4,5], [])
values
```




    [2, 4, 6, 8, 10]



次に偶数のみを抽出してみます（filterのような処理）。


```python
from functools import reduce

values = reduce(lambda acc, cur: [*acc, cur] if cur%2==0 else acc, [1,2,3,4,5], [])
values
```




    [2, 4]



このようにアンパックを駆使すれば様々な処理が実現できる。

### 速度の話

始めに言っておきますが、reduceは特に速くないです。

なので単純な処理では全くメリットがないので、あくまでリーディング時の知識として使うことが多いと思います。（知らないと読めないため）

以降、処理時間を比較していきます。


```python
import random

sample_list = [random.randint(-2, 2) for _ in range(100000)]
```


```python
%%timeit
values = reduce(lambda acc, cur: [*acc, cur] if cur%2==0 else acc, sample_list, [])
```

    3.79 s ± 112 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
    


```python
%%timeit
values = [ i for i in sample_list if i%2==0]
```

    3.78 ms ± 128 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
    

リスト内包表記が1000倍くらい速そうです。

これは実際はフェアな比較ではなく、reduceはlambda式でワンライナーで表現するために変数を作り直しているからです。

なのでlambda式を使わず、変数を新規作成せずにappendするといくぶんかマシになります。（2倍程度の処理時間におさまりました）


```python
%%timeit
def myfunc(acc, cur):
    acc.append(cur)
    return acc
values = reduce(myfunc, sample_list, [])
```

    7.45 ms ± 110 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
    

ただしそれでもリスト内包表記の方が速いです。

## その他の高階関数

### sorted

sortedは割とよく使います。globなどのファイル一覧の結果が順序不定なのは有名な話ですが、これを整列させるときにも使います。


```python
sample_list = [1,5,4,7,3,4,5,1]

sample_list2 = sorted(sample_list)

print(sample_list2)
```

    [1, 1, 3, 4, 4, 5, 5, 7]
    

このままでは高階関数とはいえませんが、keyにソートするルールを書くことができます。このルールが関数なので、高階関数となります。

keyは要素毎に処理され、返す値が小さい順に前（昇順）に来ます。

以下は反転させるので、大きい順となる。


```python
sample_list = [1,5,4,7,3,4,5,1]

sample_list2 = sorted(sample_list, key=lambda x: -x)

print(sample_list2)
```

    [7, 5, 5, 4, 4, 3, 1, 1]
    

なお、sortedにはreverseという引数があり、降順にすることも可能。


```python
sample_list = [1,5,4,7,3,4,5,1]

sample_list2 = sorted(sample_list, reverse=True, key=lambda x: -x)

print(sample_list2)
```

    [1, 1, 3, 4, 4, 5, 5, 7]
    

### max

maxは要素の最大値を求める処理です。


```python
sample_list = [1,5,4,7,3,4,5,1]

max_val = max(sample_list)

print(max_val)
```

    7
    

こちらも、keyに最大として評価するルールを書くことができ、これが関数なので高階関数となります。

sortedと実施される処理はにており、要素毎に処理され、返す値が一番大きい要素を抽出します。要するに、sortedした場合の末尾の値を取ってくる感じですね。


```python
sample_list = [1,5,4,7,3,4,5,1]

max_val = max(sample_list, key=lambda x: -x)

print(max_val)
```

    1
    

## 演習

演習問題１：次のリストが与えられたときに、高階関数を使って偶数だけを取り出し、それらを2乗し、最後に昇順で並べた結果を出力せよ

```python
sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

<br>
<br>
<br>
<br>
<br>
解答例


```python
sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

it = sorted(map(lambda x: x*x, filter(lambda x: x%2==0, sample_list)))

print([*it])
```

    [4, 16, 36, 64, 100]
    

演習問題２：次のようなリストが与えられたときに、偶数のみを累積和するような処理を高階関数`reduce`を使って実装せよ。

```python
sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

の場合、以下が出力される。

```
[0, 2, 2, 6, 6, 12, 12, 20, 20, 30]
```

なお無名関数での実装は難しいと思われるので、別途関数を定義し、reduceに処理させても良い。
<br>
<br>
<br>
<br>
<br>
解答例


```python
from functools import reduce

sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = reduce(lambda acc, cur: [*acc, acc[-1] + cur if len(acc)!=0 else cur] if cur%2==0 else [*acc, acc[-1] if len(acc)!=0 else 0], sample_list, [])
result
```




    [0, 2, 2, 6, 6, 12, 12, 20, 20, 30]



ここまで


