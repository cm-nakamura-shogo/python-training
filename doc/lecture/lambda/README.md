<a href="https://colab.research.google.com/github/cm-nakamura-shogo/python-training/blob/master/doc/lecture/lambda/README.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# lambda式とmap, filter, reduce

ここでは以下についてやります。

- ラムダ式ってなんぞ？
- map, filter, reduceの使い方

## lambda式

すでにでてきてるかもしれませんが、無名関数とも呼ばれます。

よくmapなどと組み合わせて使用されたり、pandasだとapplyでユーザ定義関数を使う場合に見られます。

あまり意味のある実装ではないですが、以下のような感じで作ります。


```python
def myfunc(func_conv, input):
    return func_conv(input)

ret_val = myfunc(lambda x: x+1, 100)

print(f"{ret_val=}")
```

    ret_val=101
    

引数を2個にしたい場合は以下のようにします。


```python
def myfunc(func_conv, x, y):
    return func_conv(x, y)

ret_val = myfunc(lambda x,y: x+y, 100, 1)

print(f"{ret_val=}")
```

    ret_val=101
    

ちなみに、ここで作ったmyfuncのように関数を引数にもつ関数を、高階関数と呼ぶようです。

以降のmap, filter, reduceはそれも高階関数になります。

## map, filter, reduceについて

map, filter, reduceはlistなどのiterableに対する処理を行います。

mapは全要素に同じ操作を、filterはある条件での抽出操作を、reduceは全知全能です。

なお、同名の処理はJavaScriptでも出没するので覚えておいておくと後々役立ちます。

特にreduceはこの機会にマスターしましょう。（mapとfilterはそもそもそんなにむずくない）

## map

全要素に同じ操作を実施します。


```python
it = map(lambda x: x+1, [1,2,3,4,5])

gen.__next__()
gen.__next__()
gen.__next__()
gen.__next__()
gen.__next__()
gen.__next__()
```


    ---------------------------------------------------------------------------

    StopIteration                             Traceback (most recent call last)

    Cell In[9], line 8
          6 gen.__next__()
          7 gen.__next__()
    ----> 8 gen.__next__()
    

    StopIteration: 


WIP

- [Pythonのreduceと内包表記／ジェネレータ式を比較してみた | DevelopersIO](https://dev.classmethod.jp/articles/python-reduce-vs-generator)


