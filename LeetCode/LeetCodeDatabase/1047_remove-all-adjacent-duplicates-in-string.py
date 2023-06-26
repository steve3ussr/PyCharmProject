class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = []
        for _ in s:
            if res and _ == res[-1]:
                res.pop()
            else:
                res.append(_)
        return "".join(res)