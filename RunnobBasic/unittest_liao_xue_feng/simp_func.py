

def add_one(x):
    if isinstance(x, int):
        return x + 1
    else:
        return x


if __name__ == '__main__':
    res = add_one(1)
    print(res)
