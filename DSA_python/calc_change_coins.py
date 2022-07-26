import functools
import time


class Solution(object):
    def __init__(self):
        self.cache = dict()
        self.dp = dict()

    def calc_coins_recursion(self, val_list: list, charge: int):
        if charge in val_list:
            return 1
        else:
            return 1 + min(self.calc_coins_recursion(val_list, charge - x) for x in val_list if x < charge)

    def calc_coins_recursion_cache(self, val_list: list, change: int):
        if _ := self.cache.get(change):
            return _
        else:
            pass

        if change in val_list:
            tmp = 1

        else:
            tmp = 1 + min(self.calc_coins_recursion_cache(val_list, change - x) for x in val_list if x < change)

        self.cache[change] = tmp
        return tmp

    def dp_coins(self, val_list, change):
        # build
        for i in range(1, change + 1):
            if i in val_list:
                self.dp[i] = 1
            else:
                self.dp[i] = min((self.dp[i - x] + 1 for x in val_list if x < i))

        return self.dp[change]


if __name__ == '__main__':
    def timer(func):
        @functools.wraps(func)
        def timer_inner(*args, **kwargs):
            start = time.time()
            func(args, kwargs)
            end = time.time()
        return timer_inner


    res_recursion = Solution().dp_coins([1, 5, 10, 25], 12341)
    print(res_recursion)
