

def main():

    sample_dict = {
        "hoge": {'A': 1, 'B': 2, 'C': 3},
        "fuga": {'D': 4, 'E': 5, 'F': 6}, 
        'G': 7, 
        'H': 8, 
        "hage": {'I': 9 , "kuso": {'J': 10, 'K': 11}},
        "ahou": {'L': 12, 'M': 13, 'N': 14}
    }

    output_dict = product(sample_dict, a=2)

    print(output_dict)


def product(sample_dict, a):

    output_dict = {}

    for k,v in sample_dict.items():
        if isinstance(v, dict):
            ret = product(v, a)
            output_dict = {**output_dict, k: ret}

        else:
            if isinstance(v, int) or isinstance(v, float):
                output_dict = {**output_dict, k: v*a}
            else:
                output_dict = {**output_dict, k: v}

    return output_dict

if __name__ == "__main__":
    main()