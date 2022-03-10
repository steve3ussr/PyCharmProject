def input_score(i):
    if isinstance(i, int):
        return i
    else:
        raise ValueError("You fool, int only")


fee = input_score(11.8)
print(fee)
