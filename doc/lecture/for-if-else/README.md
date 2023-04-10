<a href="https://colab.research.google.com/github/cm-nakamura-shogo/python-training/blob/master/doc/lecture/for-if-else/README.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# ループと条件分岐

ここでは主に以下をやります。

- forなどの基本的なループとrange, enumerate, zipなど
- if-elseなどの基本的な条件分岐
- ついでに条件分岐で浮動小数の丸め誤差について
- リスト内包表記について

## 基本のループ

### inで要素毎のループをまわす

listやtupleやsetなどはforで直接まわすことができる。


```python
sample_list = [100, 200, 300]

for i in sample_list:
    print(i)
```

    100
    200
    300
    


```python
sample_tuple = ("A", 200, "B")

for i in sample_tuple:
    print(i)
```

    A
    200
    B
    


```python
sample_set = set([100, 200, 300])

for i in sample_set:
    print(i)
```

    200
    100
    300
    

dictはitemsで回すほか、keysやvaluesでまわすことができる。


```python
sample_dict = {'A': 100, 'B': 200, 'C': 300}

for k, v in sample_dict.items():
    print(k, v)
```

    A 100
    B 200
    C 300
    


```python
for element in sample_dict.items():
    print(element)
```

    ('A', 100)
    ('B', 200)
    ('C', 300)
    


```python
a, b = (10, 20)
print(a)
print(b)
```

    10
    20
    


```python
sample_dict = {'A': 100, 'B': 200, 'C': 300}

for k in sample_dict.keys():
    print(k)

for v in sample_dict.values():
    print(v)
```

    A
    B
    C
    100
    200
    300
    

### rangeで固定回数回す


```python
for i in range(5):
    print(i)
```

    0
    1
    2
    3
    4
    

start, stopやstepを指定することも可能


```python
for i in range(5,10,2):
    print(i)
```

    5
    7
    9
    

### enumerateで要素番号とともに回す

enumerateを使うことで要素番号が得られる。


```python
sample_list = [100, 200, 300]

for i, v in enumerate(sample_list):
    print(i, v)
```

    0 100
    1 200
    2 300
    

### zipで複数のリスト等を回す


```python
sample_list1 = [10, 20, 30]
sample_list2 = [100, 200, 300]
sample_list3 = ["A", "B", "C"]

for v1, v2, v3 in zip(sample_list1, sample_list2, sample_list3):
    print(v1, v2, v3)
```

    10 100 A
    20 200 B
    30 300 C
    

## 基本の条件分岐

### if- elif - else

例えば典型的には以下のように書ける。


```python
A = 90

if A < 10:
    print("A < 10")
elif A < 100:
    print("10 <= A < 100")
else:
    print("100 <= A")


```

    10 <= A < 100
    

elifは実は存在しなくてもかならずelseとifで表現は可能。


```python
A = 90

if A < 10:
    print("A < 10")
else:
    if A < 100:
        print("10 <= A < 100")
    else:
        print("100 <= A")
```

    10 <= A < 100
    

コードを見直す際は、elseが無い場合などに無くて本当によいか、などをチェックした方が良い。

### 浮動小数のif文

浮動小数は条件分岐に書くときに注意が必要（特に`==`では不成立となることが多い）。


```python
A = 0.2 + 0.4 + 0.3 + 0.1
print(f"{A=:.5f}")

if A == 1:
    print("A is 1")
else:
    print("A is not 1")
```

    A=1.00000
    A is not 1
    

これは浮動小数には丸め誤差（偶数丸め等）が発生するためである。


```python
print(f"{A=:.20f}")
print(f"{1=:.20f}")
```

    A=0.99999999999999988898
    1=1.00000000000000000000
    

浮動小数は無限個のパターンの数値を取りうるので、有限な情報（32bit）などで表現するために必ず丸め誤差が生じる。

それ以外に、仮数部や指数部など浮動小数のモデルをもっと知りたい方は以下などを参照。

- [数値の表現](http://ss.sguc.ac.jp/~rider/basic/float.html)

いわゆる金融系などこういった演算を正確に行いたい場合は、Decimalを使用する必要がある。

Decimalにより各演算は10進数に丸められる。


```python
from decimal import Decimal

A = Decimal("0.1") + Decimal("0.5") + Decimal("0.3") + Decimal("0.1")
print(A)

if A == Decimal("1"):
    print("A is 1")
else:
    print("A is not 1")
```

    1.0
    A is 1
    

## for - else

forにelseが使えるという情報を観測したため念のため書いておく（まれに観察される）。

ループをbreakで抜けたか、全部走査し終わって終了したかで処理を分ける際に使用できる。


```python
arr = [1,2,3,4,5,6,7,8,9]

for i in arr:
    if i==10:
        find_flag = 1
        break
else:
    find_flag = 0

print(f"{find_flag=:}")

```

    find_flag=0
    

## リスト内包表記

普通のリスト内包表記から


```python
sample_list = [0,1,2,3,4,5,6]
sample_list_2 = [ i*2 for i in sample_list] # 各要素を倍にする
sample_list_2
```




    [0, 2, 4, 6, 8, 10, 12]



if/elseとの組み合わせで条件によって結果を変える（配列サイズ不変）。


```python
sample_list = [0,1,2,3,4,5,6]
sample_list_3 = [ i*2 if i%2==1 else -1 for i in sample_list] # 奇数は倍に、偶数は-1にする
sample_list_3
```




    [-1, 2, -1, 6, -1, 10, -1]



ここまでの書き方は要素数は変わらないものであったが、要素数を変える抽出が以下のように記述できる。

末尾にif文があることが特徴。英文表記に近いのかも？


```python
sample_list = [0,1,2,3,4,5,6]
sample_list_4 = [ i*2 for i in sample_list if i%2==1] # 奇数のみ倍にして抽出する
sample_list_4
```




    [2, 6, 10]



一般的に普通のforよりもリスト内包表記の方が高速と言われるが、可読性とのトレードオフともいえる。（たとえば複数階層のリスト内包表記は理解しづらい）

使いどころだが、各要素に均等な処理をする場合、リスト内包表記で、それ以外は普通のfor文というイメージで良いと思う。

各要素に均等な処理をするってのが、コード的に分かりやすいということも含めて上記の意見。

（JavaScriptもfor文滅多に使わずmapとかreduceでやるからにているのかな、ここら辺は）

### 速度の検証


```python
N = 100000000
```


```python
%%timeit
A = [i*2 for i in range(N)]
```

    6.39 s ± 209 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
    


```python
%%timeit
A = []
for i in range(N):
    A.append(i*2)
```

    8.92 s ± 343 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
    


```python
import numpy as np
```


```python
%%timeit
A = [*(np.arange(N) * 2)]
```

    3.88 s ± 273 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
    


```python

```
