class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return self.v1_kmp(s)

    def v1_kmp(self, s):
        s2 = s + s
        s2 = s2[1:-1]
        assert len(s2) == 2*len(s)-2

        next = [0]
        x = 1
        now = next[x-1]

        while x < len(s):
            if s[x] == s[now]:
                next.append(now+1)
                now += 1
                x += 1
            elif now:
                now = next[now-1]
            else:
                next.append(0)
                x += 1

        idx_pat = 0
        for i, v in enumerate(s2):
            while idx_pat and v != s[idx_pat]:
                idx_pat = next[idx_pat-1]
            if v == s[idx_pat]:
                idx_pat += 1
            if idx_pat == len(s):
                return True
        return False

    def v2_builtin(self, s):
        return True if s in s[1:] + s[:-1] else False