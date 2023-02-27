
import argparse
import pathlib

def main(in_dir: str, output_file: str):
    """メイン

    Args:
        in_dir (str): 入力ディレクトリ
        output_file (str): 出力ファイル
    """

    in_files = sorted([*pathlib.Path(in_dir).glob("**/*.csv")])

    with open(output_file, "wt") as fw:
        for idx, f in enumerate(in_files):
            with open(f, "rt") as f:
                lines = f.readlines()
                if idx == 0:
                    fw.writelines(lines)
                else:
                    fw.writelines(lines[1:])

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--in-dir', required=True, type=str)
    parser.add_argument('--output-file', required=True, type=str)
    args = parser.parse_args()

    main(args.in_dir, args.output_file)
