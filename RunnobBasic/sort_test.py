def by_name(a_tup):
    return a_tup[0]


def by_score(a_tup):
    return a_tup[1]


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L, key=by_score, reverse=True))


# -------------------------

