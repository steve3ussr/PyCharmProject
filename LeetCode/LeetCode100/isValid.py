class Solution:
    def isValid(self, s: str) -> bool:
        alist = []
        trans_dict = {')': '(', ']': '[', '}': '{'}
        for i in s:
            if i in ('(', '[', '{'):
                alist.append(i)
            else:
                if alist and trans_dict[i] == alist[-1]:
                    alist.pop()
                else:
                    return False

        return False if alist else True


if __name__ == '__main__':
    import time
    from functools import wraps


    def outer(count):
        def mid(afunc):
            def inner(*args, **kwargs):
                start_time = time.time()
                afunc(*args, **kwargs)
                end_time = time.time()
                print(f'{(end_time - start_time) * 1000 / count} ms')
            return inner
        return mid


    @outer(k := 1000000)
    def test_func(k):
        i = 0
        while i<k:
            teststr = '()'
            res = Solution().isValid("()")
            i += 1



    test_func(k)
