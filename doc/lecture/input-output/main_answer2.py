import typing as T
import argparse
import pathlib

def parse_value_from_line(line: str, col_idx: int) -> str:
    """ラインから指定カラムのデータを取得

    Args:
        line (str): ラインのデータ
        col_idx (int): カラムのインデックス

    Returns:
        str: 取得結果
    """
    return line.split(",")[col_idx].rstrip("\n")

def main(in_dir: str, coeff: float, out_file: str):
    """メイン

    Args:
        in_dir (str): 入力フォルダ名
        coeff (float): 乗算する係数
        out_file (str): 出力ファイル名
    """

    # strをpathに変換
    input_path = pathlib.Path(in_dir)

    # csvファイル一覧を取得
    input_files = sorted([*input_path.glob("**/*.csv")])

    # すべてのファイルを読み込み
    header = ""
    all_lines: T.List[str] = []
    for idx, file in enumerate(input_files):
        lines = file.read_text().rstrip("\n").split("\n")
        if idx == 0:
            header = lines[0] 
        lines = lines[1:]
        all_lines.extend(lines)

    # headerをパース
    col_name = header.split(",")
    col_num = len(col_name)

    # 係数を掛ける
    all_lines_output = []
    for line in all_lines:

        # 最初のカラムはuuidなのでそのまま取得
        line_output = f"{parse_value_from_line(line, 0)}"

        # 残りのカラムはデータなので係数をかける
        for col_idx in range(1, col_num):
            value = parse_value_from_line(line, col_idx)
            line_output = line_output + f",{float(value)*coeff}"

        # データ追加
        all_lines_output.append(line_output)

    # 出力
    pathlib.Path(out_file).write_text("\n".join([header, *all_lines_output]) + "\n")

    return

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--in-dir'  , required=True , default=None        , type=str  , help='入力フォルダのパス')
    parser.add_argument('--coeff'   , required=False, default=2.0         , type=float, help='乗算する係数')
    parser.add_argument('--out-file', required=False, default="output.txt", type=str  , help='出力ファイルのパス')

    args = parser.parse_args()

    main(**args.__dict__)