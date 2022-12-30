# input-output

## 座学

### CLIのおまじないについて

CLIでpythonスクリプトを呼び出す場合、以下をファイル末尾に記述することが多い。

```python
if __name__ == "__main__":
    # ここがCLIで最初に呼び出される
```

詳細は以下を読む。

- [【Python】　if __name__ == “__main__” とはなにか | AI Academy Media](https://aiacademy.jp/media/?p=1478)

### argparse

argparseはコマンドライン引数をパースする標準ライブラリ。

まずは以下を読む。

- [【python】コマンドライン引数を扱うargparseを丁寧に - gotutiyan’s blog](https://gotutiyan.hatenablog.com/entry/2020/09/28/003910)

以下例示と補足。

```python
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--in-dir', required=True, default=None, type=str, help='入力フォルダのパス')
    args = parser.parse_args()

    # ハイフンはアンダーバーに置き換わるので注意
    print(args.in_dir)

    # 引数群全体をdictに変換することも可能
    print(args.__dict__)
```

### open

基本的にはwithを使って以下のような形で記述する。

```python
def main():
    # 読み込み
    with open("sample.txt", "rt") as f:
        lines = f.readlines()
    
    # 書き込み
    with open("output.txt", "wt") as f:
        f.writelines(lines)
```

`rt`・`wt`はテキスト読み込み・書き込み用のオプション。

バイナリの場合は`rb`・`wb`を使う。

追加書き込みのオプションもあり`at`・`ab`と記述する。

### pathlib

ファイル操作用のライブラリで主な操作は以下。

```python
import pathlib

# 文字列をpathクラスにする
root_path = pathlib.Path(".")

# サブフォルダのパス結合
input_path = root_path.joinpath("input")
input_file = root_path.joinpath("input", "sample.txt")
output_path = root_path.joinpath("output")

# フォルダの一覧（ファイル・フォルダ）取得
files = input_path.glob("**")

# フォルダの作成（サブ階層OK、存在してもエラーにしない）
output_path.mkdir(parents=True, exit_ok=True)

# ファイル有無のチェック
input_file.exists()

# 空ファイルの作成
input_file.touch()

# 実はopenもできる（前述のopenを代用可能）
with input_file.open(mode="wt") as f:
    f.writelines(["aaa\n", "bbb\n", "ccc\n"])

# read_text, write_textというものもあるらしい
input_file.read_text()
input_file.write_text(["aaa\n", "bbb\n", "ccc\n"])

# ファイルとシンボリックリンクはunlinkで削除可能
input_file.unlink()

# 親ディレクトリをpathクラスで取得
print(str(input_file.parent))
# => ./input

# ファイル名そのものを取得
print(input_file.name)
# => sample.txt

# 拡張子なしのファイル名を取得
print(input_file.stem)
# => sample

# 拡張子を取得
print(input_file.suffix)
# => .txt

# 拡張子の付け替え
print(str(input_file.with_suffix(".csv"))
# => ./input/sample.csv
```

サブフォルダごと削除したい場合のみ、shutilを使う必要がある。

```python
import shutil

shutil.rmtree("./aaaa")
```

以下参考リンク

- [Python, pathlibでファイルの作成・open・読み書き・削除 | note.nkmk.me](https://note.nkmk.me/python-pathlib-file-open-read-write-unlink/)
- [Python, pathlibでファイル名・拡張子・親ディレクトリを取得 | note.nkmk.me](https://note.nkmk.me/python-pathlib-name-suffix-parent/)
- [Pythonでファイル・ディレクトリを削除するos.remove, shutil.rmtreeなど | note.nkmk.me](https://note.nkmk.me/python-os-remove-rmdir-removedirs-shutil-rmtree/)

## 演習

### 問１

- 入力フォルダ内のファイルをすべて結合して１ファイルとするCLIツールを作成してください。
- 入力フォルダ内のファイルのカラム数などは同じ前提とします。
- CLIの引数は入力フォルダ名、出力ファイル名です。
- 出力ファイル名にはデフォルト値を与えてもOKです。
- サンプルデータは`./input`に配置されているものを使用ください。

### 問２

- 問１のつづきで、入力ファイルの一番左端以外のデータにある係数を掛ける処理を追加してください。
- CLIの引数には係数の情報を指定できるようにします。
- 係数にはデフォルト値を与えてもOKです。
