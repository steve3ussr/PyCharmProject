# print((lambda x, y: x+y)(float(input('x=')), float(input('y='))))

def add_score(*args):
    try:
        print(sum(map(float, args)))
    except ValueError:
        print("Fool, enter real number!")
        raise


add_score(15.765, 6543, 674859, 6537)
