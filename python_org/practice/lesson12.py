def first_last_item(num_list):
    print([num_list[0], num_list[len(num_list) - 1]])
    print(num_list[:1], num_list[-1:])


if __name__ == "__main__":
    first_last_item([1, 2, 3, 5, 6, 8])
