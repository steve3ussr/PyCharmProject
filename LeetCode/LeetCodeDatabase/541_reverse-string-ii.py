class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        return self.v1(s, k)

    def v1(self, s, k):

        s = list(s)
        n = len(s)
        idx_end = 0

        for i in range(n // (2 * k)):
            idx_start = i * 2 * k
            idx_end = idx_start + k - 1
            for _ in range(k // 2):
                s[idx_start + _], s[idx_end - _] = s[idx_end - _], s[idx_start + _]

        redundant = n - n // (2 * k) * (2 * k)
        if redundant:
            print(redundant)
            idx_start = n // (2 * k) * (2 * k)
            idx_end = idx_start + k - 1
            idx_end = min(idx_end, n - 1)
            print(idx_start, idx_end)
            l = idx_end - idx_start + 1
            for i in range(l // 2):
                s[idx_start + i], s[idx_end - i] = s[idx_end - i], s[idx_start + i]

        return "".join(s)

    def v2(self, s, k):
        s = list(s)
        for i in range(0, len(s), 2*k):
            s[i:i+k] = reversed(s[i:i+k])
        return "".join(s)


if __name__ == '__main__':
    print(Solution().reverseStr("abcdefg", 3))
