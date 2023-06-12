from collections import defaultdict, Counter


class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        # TODO: https://pic.leetcode.cn/1676554659-UJbbDS-image.png
        cnt = dict()
        lo = res = 0

        for hi, v_hi in enumerate(fruits):
            if v_hi in cnt:
                cnt[v_hi] += 1
            else:
                cnt[v_hi] = 1

            # 确保当前窗口满足条件
            while len(cnt) > 2:
                v_lo = fruits[lo]
                cnt[v_lo] -= 1
                if cnt[v_lo] == 0:
                    cnt.__delitem__(v_lo)
                lo += 1

            res = max(res, hi - lo + 1)
        return res


if __name__ == '__main__':
    data = [0, 1, 2, 2]
    res = Solution().totalFruit(data)
    print(res)
