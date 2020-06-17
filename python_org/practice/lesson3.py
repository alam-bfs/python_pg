def less_than_five_elements(base_list):
    return [x for x in base_list if x < 5]


if __name__ == "__main__":
    ll = list()
    ll.append(1)
    ll.append(5)
    ll.append(4)
    ll.append(7)

    print(less_than_five_elements([4, 10, 3, 13]))
