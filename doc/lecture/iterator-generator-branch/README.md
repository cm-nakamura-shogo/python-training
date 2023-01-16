<a href="introduction.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# ループと条件分岐

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

for v1, v2 in zip(sample_list1, sample_list2):
    print(v1, v2)
```

    10 100
    20 200
    30 300
    


```python

```
