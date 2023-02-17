
test_list = [ ['A', 'B', 'C'], ['D', 'E', 'F'], 'G', 'H', ['I', ['J', 'K'], ['L', 'M', 'N']]]

# 作りたい関数メモ
# list型がlist型でなくなるまでアンパックして、list型でなくなった時点で新リストに挿入、次の要素の処理へ
def flaten(test_list):
    test_flaten_list =  []
    for test_list_element in test_list:
        while type(test_list_element) is list:
            # print(*test_list_element)
            # print(type(test_list_element))
            test_flaten_list= [*test_flaten_list, *test_list_element]
            # print(test_flaten_list)
            break
        test_flaten_list = [*test_flaten_list, test_list_element]

        # test_flaten_list = [*test_flaten_list,*test_list_element]
        # print(test_flaten_list)
    print(test_flaten_list)
flaten(test_list)