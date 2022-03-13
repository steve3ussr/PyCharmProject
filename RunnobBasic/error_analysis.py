from functools import reduce


def str2num(s):
    s.replace(' ', '')
    s = s.replace('.', '')
    try:
        return int(s)
    except ValueError:
        pnt_index = len(s) - 1 - s.index('.')
        return reduce((lambda a, b: int(a)*10 + int(b)), s) / (10 ** pnt_index)


def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)


def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)


main()
