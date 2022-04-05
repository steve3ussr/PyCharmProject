def dec2bin_div2(a):
    from pythonds.basic.Stack import Stack
    res = Stack()
    ans = ''
    while a > 0:
        res.push(a % 2)
        a = a // 2

    while not res.isEmpty():
        ans += str(res.pop())

    return ans


if __name__ == '__main__':
    test_num_dec = 173
    test_num_binstr = dec2bin_div2(test_num_dec)
    print(test_num_binstr)
