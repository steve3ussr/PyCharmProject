import operator
from collections import Counter, defaultdict
from functools import reduce
from itertools import accumulate


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # minimal return condition
        if len(s) < len(t):
            return ""

        # initial hashmap
        hs, ht = defaultdict(int), defaultdict(int)
        for chr in t:
            ht[chr] += 1

        # initial res
        res = ""

        # initial pnt
        # cnt: satisfied chr number in curr window
        lo = hi = cnt = 0

        while hi < len(s):
            v_hi = s[hi]
            hs[v_hi] += 1

            #    >=1         >=0
            if hs[v_hi] <= ht[v_hi]:
                # 如果能满足这个条件，说明t中对这个新的元素有需求
                # 同时能保证不多选元素，也就是窗口到这里刚好能满足对这个字符的需求
                cnt += 1

            while lo <= hi and hs[s[lo]] > ht[s[lo]]:
                # 看能不能缩短前指针，得到一个尽量短的字符串
                hs[s[lo]] -= 1
                lo += 1

            if cnt == len(t):
                if not res or (hi - lo + 1) < len(res):
                    res = s[lo:hi + 1]
            hi += 1
        return res


if __name__ == '__main__':
    source = 'AA'
    target = 'AA'
    res = Solution().minWindow(source, target)
    print(res)
