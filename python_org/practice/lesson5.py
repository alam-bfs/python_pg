def new_list(list_a, list_b):
    result_list = []

    for i in list_a:
        if i in list_b:
            result_list.append(i)
    print(result_list)


if __name__ == "__main__":
    new_list([1, 2, 3, 4], [1, 3, 5, 6])
