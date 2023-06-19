class Solution:
    def isHappy(self, n: int) -> bool:
        def calc(v):
            res = 0
            while v >= 10:
                res += (v % 10) ** 2
                v = v // 10
            res += v ** 2
            return res

        dct = dict()
        while n != 1:
            if n in dct:
                return False

            dct[n] = 0
            n = calc(n)
        return True
