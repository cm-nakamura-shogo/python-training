import struct

def main():

    lines = []
    with open("exercise3_input.txt", "rt") as f:
        lines = f.readlines()

    for l in lines:
        bytes_data = str_to_bytes(l)
        for v in [i[0] for i in struct.iter_unpack('<f', bytes_data[:-2])]:
            print(v, end=" ")
        print(struct.unpack('<h', bytes_data[-2:])[0])

def str_to_bytes(str_data: str):

    # 前後の"とbを削除してencodeする。
    str_data = str_data.encode()[2:-2]

    bytes_data = b""
    for idx, _b in enumerate(str_data):
        if _b == 92 or _b == 120: # \とxはスキップ
            continue
        else:
            # \xの直後は、2文字で1byte情報となっている前半部分。ここで文字列を数値に変換する。
            if str_data[idx-2] == 92 and str_data[idx-1] == 120:
                a = str_data[idx]
                b = str_data[idx+1]

                # 一旦16新数文字列に変換し、整数にする
                value = int("0x{}{}".format(chr(a), chr(b)), 0) # chrはアスキーコード(int)を文字に変換する

                value = value.to_bytes(length=1, byteorder="little", signed=False)
                bytes_data = bytes_data + value

            # \xの2個後ろは、2文字で1byte情報となっている後半部分。変換済みなのでスキップ
            elif str_data[idx-2] == 120 and str_data[idx-3] == 92: # 2
                continue

            # どちらでもない場合、1文字で1byteの情報となっているため、そのまま数値として読み込みbyte変換する。
            else:
                value = str_data[idx]
                value = value.to_bytes(length=1, byteorder="little", signed=False)
                bytes_data = bytes_data + value

    return bytes_data

if __name__ == "__main__":
    main()