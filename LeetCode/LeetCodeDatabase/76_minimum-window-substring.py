import operator
from collections import Counter
from functools import reduce
from itertools import accumulate


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # minimal return requirement
        if len(s) < len(t):
            return ""

        # target char set filter
        target_set = set(t)

        # init counter. value means:
        # 0: satisfied
        # +int: l than req
        # -int: g than req
        cnt_curr = Counter(t)
        for i in range(len(t)):
            if s[i] in target_set:
                cnt_curr[s[i]] -= 1
        # return reduce(lambda x, y: (x > 0 or y > 0), cnt_curr.values())

        # init res
        res_len = len(t)
        res_idx = [0, 0]

        # init slide window
        lo = 0
        for hi in range(len(t) - 1, len(s)):
            if


if __name__ == '__main__':
    source = 'ADOBECODEBANC'
    target = 'ABC'
    res = Solution().minWindow(source, target)
    print(res)
