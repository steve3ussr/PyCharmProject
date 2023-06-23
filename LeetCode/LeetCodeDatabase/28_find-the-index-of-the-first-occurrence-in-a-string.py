class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return self.v3_kms_normal(haystack, needle)

    def v1_complex(self, haystack, needle):
        len_all = len(haystack)
        len_nee = len(needle)

        if len_all < len_nee:
            return -1

        i = 0
        while i <= len_all - len_nee:
            if haystack[i] != needle[0]:
                i += 1
                continue

            j = 0
            flg_succ = 1
            while j < len_nee:
                if haystack[i + j] != needle[j]:
                    i += 1
                    flg_succ = 0
                    break
                j += 1

            if flg_succ:
                return i
        return -1

    def v2_re(self, haystack, needle):
        import re
        res = re.search(f"(?P<prefix>.*?)({needle}).*", haystack)
        if res:
            return len(res.group('prefix'))
        else:
            return -1

    def v3_kms_normal(self, haystack, needle):
        len_pat = len(needle)
        len_tar = len(haystack)

        if len_pat == 0 or len_pat > len_tar:
            return -1

        # build next
        next = [0]
        x = 1
        now = 0

        while x < len_pat:
            if needle[x] == needle[now]:
                next.append(now + 1)
                now += 1
                x += 1

            elif now:
                now = next[now - 1]

            else:
                x += 1
                next.append(0)

        # main
        idx_pat = 0
        idx_tar = 0

        for idx_tar in range(len_tar):
            while idx_pat > 0 and haystack[idx_tar] != needle[idx_pat]:
                idx_pat = next[idx_pat - 1]
            if haystack[idx_tar] == needle[idx_pat]:
                idx_pat += 1
            if idx_pat == len_pat:
                return idx_tar - idx_pat + 1
        return -1


if __name__ == '__main__':
    print(Solution().strStr('mississippi', 'issipi'))
