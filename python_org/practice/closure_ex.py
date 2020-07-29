def outer_func():
    message = 'Hi There'

    def inner_func1(name):
        print(message, name)

    return [inner_func1]


func_list = outer_func()
name_lst = ['Kaiser', 'John']

for f in func_list:
    for n in name_lst:
        f(n)
