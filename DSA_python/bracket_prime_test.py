def bracket_prime_test(s):
    """
    确保括号的正常，包括([{, }])
    """
    from pythonds.basic.Stack import Stack

    i = 0
    balance = True
    b = Stack()
    left_bracket = "([{"
    right_bracket = ")]}"

    while balance and i < len(s):
        syms = s[i]
        if syms in left_bracket:
            b.push(syms)
        elif syms in right_bracket:
            top = b.peek()
            # print(f'top is {top}, syms is {syms}')
            if left_bracket.index(top) == right_bracket.index(syms):
                b.pop()
            else:
                balance = False

        else:
            pass

        i += 1
    # print(f'balance is {balance}')
    # print(f'b is {b}')

    if b.isEmpty() and balance:
        return True
    else:
        return False


if __name__ == '__main__':
    test_str = '({)}'
    print(bracket_prime_test(test_str))
