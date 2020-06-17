def get_new_list(list_a, list_b):
    return [x for x in list_a if x in list_b]


def get_sub_set(list_a, list_b):
    return [x for x in list_b if x not in list_a]


if __name__ == "__main__":
    print(get_new_list([1, 2, 3], [2, 3, 4, 5]))
    print(get_sub_set([1, 2, 3], [2, 3, 4, 5]))
