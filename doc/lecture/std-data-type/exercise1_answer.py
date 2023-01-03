

def main():

    sample_list = [ ['A', 'B', 'C'], ['D', 'E', 'F'], 'G', 'H', ['I', ['J', 'K'], ['L', 'M', 'N']]]

    flatten_list = flatten(sample_list)

    print(flatten_list)


def flatten(sample_list):

    flatten_list = []

    for i in sample_list:
        if isinstance(sample_list, list):
            v = flatten(i)
            flatten_list = [*flatten_list, *v]
        else:
            flatten_list = [*flatten_list, i]

    return flatten_list

if __name__ == "__main__":
    main()