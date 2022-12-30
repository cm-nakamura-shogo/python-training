import pathlib
import numpy as np
import uuid
import pandas as pd
import argparse

def create_random_dataframe(seed=42, size=100) -> pd.DataFrame:
    np.random.seed(seed)
    col_id = [str(uuid.uuid4()) for _ in range(size)]
    col_1 = np.random.randn(size)
    col_2 = np.random.uniform(size=size)
    return pd.DataFrame({"uuid": col_id, "col1": col_1, "col2": col_2})

def output_dataframe(df: pd.DataFrame, out_dir: pathlib.Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    file_name = str(uuid.uuid4())
    out_file_path = out_dir.joinpath(f"{file_name}.csv")
    df.to_csv(out_file_path, index=None)

def main(out_dir: str):

    out_root_path = pathlib.Path(out_dir)
    out_dir_path = out_root_path

    for j in range(3):
        dirname = str(uuid.uuid4())
        out_dir_path = out_dir_path.joinpath(dirname)
    
        for i in range(3):
            df = create_random_dataframe(seed=42 + i + j, size=100)
            output_dataframe(df, out_dir_path)

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", default="outputs", type=str)
    args = parser.parse_args()
    main(args.out_dir)