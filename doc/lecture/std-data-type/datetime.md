<a href="https://colab.research.google.com/github/nokomoro3/book-ml-transformers/blob/main/ml-transformers-chap01-introduction.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# datetime型

## datetime型について

### 基本操作

datetime型は日付を扱うデータ型である。スカラー量なのでimmutableである。

基本的な使い方を見ていく。

現在の取得。


```python
from datetime import datetime

print(datetime.now())
```

    2022-12-27 11:50:24.279760
    

以降よくあるフォーマットについて、datetimeとstrの相互変換を見ていく。

まずは日本でよくあるやーつ。


```python
now = datetime.now()

dt_str = datetime.strftime(now, "%Y/%m/%d %H:%M:%S")
print(dt_str)

dt = datetime.strptime(dt_str, '%Y/%m/%d %H:%M:%S')
print(dt)
```

    2022/12/27 11:50:24
    2022-12-27 11:50:24
    

米国でよくあるやーつ。


```python
now = datetime.now()

dt_str = datetime.strftime(now, '%b %d %Y %I:%M%p')
print(dt_str)

dt = datetime.strptime(dt_str, '%b %d %Y %I:%M%p')
print(dt)
```

    Dec 27 2022 11:50AM
    2022-12-27 11:50:00
    

RFC2822形式。


```python
from datetime import timezone

now = datetime.now(timezone.utc)

dt_str = datetime.strftime(now, '%a, %d %b %Y %H:%M:%S %z')
print(dt_str)

dt = datetime.strptime(dt_str, '%a, %d %b %Y %H:%M:%S %z')
print(dt)
```

    Tue, 27 Dec 2022 02:50:24 +0000
    2022-12-27 02:50:24+00:00
    

ISO 8601形式は個別に関数が準備されている。（ただし`fromisoformat`はPython3.7以降で追加されている）


```python
now = datetime.now(timezone.utc)
dt_str = now.isoformat()
print(dt_str)

dt = datetime.fromisoformat(dt_str)
print(dt)
```

    2022-12-27T02:50:24.674754+00:00
    2022-12-27 02:50:24.674754+00:00
    

### timezoneについて

基本的に、tzinfoが出力されてないものはnaiveであり、tzinfoが出力されているものはawareである。

（たまにnativeと書いてある記事を見つけるが、naiveが正しい）

以下にnaiveな例とawareな例を列挙する。


```python
from datetime import timezone

print(datetime.now())

print(datetime.now(timezone.utc))
```

    2022-12-27 11:50:24.784754
    2022-12-27 02:50:24.784754+00:00
    

UTC以外のtimezoneを設定するにはいくつかの方法があり、dateutilを使うのが無難らしい。

- [datetime の UTC / JSTの変換についてまとめ | Python Snippets](https://python.civic-apps.com/datetime-utc-jst-convert/)


```python
from dateutil import tz

JST = tz.gettz('Asia/Tokyo')
UTC = tz.gettz("UTC")

print(datetime.now(UTC))
print(datetime.now(JST))
```

    2022-12-27 02:50:24.951792+00:00
    2022-12-27 11:50:24.952793+09:00
    

後付けする（naive⇒aware変換）には、astimezoneを使う。（その場合、時刻側は変わらないので注意）


```python
now = datetime.now()
print(now)

print(now.astimezone(JST))
```

    2022-12-27 11:50:25.065793
    2022-12-27 11:50:25.065793+09:00
    

変更する場合も、astimezoneを使う。（この場合は時刻側が変わる）


```python
now = datetime.now()
print(now)
print(now.astimezone(JST))
print(now.astimezone(UTC))
```

    2022-12-27 11:50:25.150819
    2022-12-27 11:50:25.150819+09:00
    2022-12-27 02:50:25.150819+00:00
    

時刻を変えたくない場合は、`replace()`で強制的にtimezoneを変更することも可能。

（これは例外的と考えた方がよいので、そもそも設計に問題がないかは確認した方が良い）


```python
now = datetime.now()
print(now)
print(now.astimezone(JST))
print(now.replace(tzinfo=UTC))
```

    2022-12-27 11:50:25.246772
    2022-12-27 11:50:25.246772+09:00
    2022-12-27 11:50:25.246772+00:00
    

timezone自体を削除（aware⇒naive変換）する場合は、Noneを設定すればよい。


```python
now = datetime.now()
print(now)
print(now.astimezone(JST))
print(now.replace(tzinfo=None))
```

    2022-12-27 11:50:25.331772
    2022-12-27 11:50:25.331772+09:00
    2022-12-27 11:50:25.331772
    

### 時間差分(timedelta)について

datetimeどうしを引き算すると、timedeltaクラスが生成される。


```python
time_str = '2021/11/14 14:31:23'
past_datetime = datetime.strptime(time_str, '%Y/%m/%d %H:%M:%S')

delta = datetime.now() - past_datetime

print(type(delta))
print(delta)
```

    <class 'datetime.timedelta'>
    407 days, 21:20:37.535760
    

timedeltaクラスは、クラスの属性値として`days`、`seconds`、`microseconds`しか持たないので注意が必要。

属性をすべて合計すると、実際の差分時間となる。

なのできちんと分離するには以下のような割と面倒な計算が必要になる。


```python
f"{delta.days} days, {delta.seconds // (60*60):02d}:{delta.seconds % (60*60) // (60):02d}:{delta.seconds % (60*60) % (60):02d}.{delta.microseconds}"
```




    '407 days, 21:20:37.535760'



別の単位（時間単位）などで差分を知りたい場合は、以下のように別のtimedeltaで除算すればよい。

- 参考
  - [Pythonのtimedeltaで「xx時間」を一発で計算する方法 - Qiita](https://qiita.com/ksato9700/items/f8a2ea86c20ac0f34538)


```python
from datetime import timedelta

delta / timedelta(hours=1)
```




    9789.31734215861



またdatetimeに加算することで、一週間前の日付などを求めることも可能。


```python
now = datetime.now()
print(now)

delta = timedelta(weeks=-1) # 負の数も指定可能
print(now+delta)
```

    2022-12-27 11:50:25.781773
    2022-12-20 11:50:25.781773
    

timedeltaとして記述できるのはweeksまでで、monthsやyearsは指定できない。

これはなぜかというと、monthsやyearsは基準となる時刻により加算すべき値が異なるため。

（months=1は30日、31日、29日、28日などのバリエーションがある）

なので一か月前という要求仕様は正確かどうか見極める必要がある。それは30日ではダメなのか？などの仕様を詰めるべき。

どうしても１か月前が良い！という話であれば、後述の`relativedelta`を使用する。

### dateutil.relativedelta

以下のようにすれば、１か月前を計算できる。


```python
from dateutil.relativedelta import relativedelta

now = datetime.now()
one_month_ago = now - relativedelta(months=1)
print(now)
print(one_month_ago)
```

    2022-12-27 11:50:25.912773
    2022-11-27 11:50:25.912773
    

ただし、例えば12月31日の場合に11月30日となる、というような動作になるということを認識しておく必要がある。


```python
now = datetime.strptime("2022/12/31 15:00:00", '%Y/%m/%d %H:%M:%S')
one_month_ago = now - relativedelta(months=1)
print(now)
print(one_month_ago)
```

    2022-12-31 15:00:00
    2022-11-30 15:00:00
    

つまり「どうしても１か月前がいい！」という要求仕様は、

言い換えれば「30日前でも31日前でも28日前でも29日前でもいいよ！そこはあいまいで！」と言っていることになる。

それでも良いかどうかはきちんとすり合わせる必要があるということ。

たぶんここがあいまいなので、標準のdatetimeでは扱えるようになっていないと考えられる。
