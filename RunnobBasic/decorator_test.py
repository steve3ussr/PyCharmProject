def add_print(afunc):
    def print_content():
        print("adding")
        afunc()
        print("added")

    return print_content


@add_print
def print_func():
    print('fuck')


print_func()
print(print_func.__name__)
