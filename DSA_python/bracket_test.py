def bracket_test(s):

    """
    只在字符串里匹配圆括号，语法正确就T，否则False
    """
    from pythonds.basic.Stack import Stack
    bracket = Stack()
    cnt = 0
    for i in range(len(s)):
        try:
            if s[i] == '(':
                bracket.push(s[i])
                cnt += 1
            elif s[i] == ')':
                if bracket.isEmpty():
                    return False
                else:
                    cnt -= 1
                    bracket.pop()
            else:
                pass
        except IndexError:
            raise

    if bracket.isEmpty() and cnt == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    test_str = '(((((()'
    res = bracket_test(test_str)
    print(res)
