def even_number_list(num_list):
    return [x for x in num_list if x % 2 == 0]


if __name__ == "__main__":
    print(even_number_list([2, 3, 5, 8, 10, 7]))
