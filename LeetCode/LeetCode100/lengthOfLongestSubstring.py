class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        map = {}
        start = 0
        ans = 0
        win = 0
        for i, v in enumerate(s):
            if (map.get(v) == 0 or map.get(v)) and map.get(v) >= start:  # repeat

                start = map.get(v) + 1
                win = i - start + 1
            else:
                win += 1

            map[v] = i
            ans = win if win > ans else ans

        return ans

