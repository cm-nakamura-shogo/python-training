
import argparse
import pathlib

def main(in_dir: str, output_file: str, mul: float):
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
                    fw.writelines(lines[0:1])

                lines_no_header = lines[1:]
                for idx2, l in enumerate(lines_no_header):
                    tok = l.split(",")
                    output = f"{tok[0]}"
                    for t in tok[1:]:
                        output = output + "," + str(float(t)*mul)
                    lines_no_header[idx2] = output + "\n"

                fw.writelines(lines_no_header)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--in-dir', required=True, type=str)
    parser.add_argument('--output-file', required=True, type=str)
    parser.add_argument('--mul', required=False, default=1.0, type=float)
    args = parser.parse_args()

    main(**args.__dict__)
