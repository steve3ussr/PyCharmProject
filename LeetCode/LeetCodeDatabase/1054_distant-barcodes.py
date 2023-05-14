from collections import Counter


class Solution:
    def rearrangeBarcodes(self, barcodes: list[int]) -> list[int]:
        cnt = Counter(barcodes)
        barcodes.sort(key=lambda x: (cnt[x], x))
        n = len(barcodes)
        res = [0] * n
        res[0::2] = barcodes[:(n+1)//2]
        res[1::2] = barcodes[(n+1)//2:]
        return res




if __name__ == '__main__':
    data = [1,3,3,3,2,2,2]
    res = Solution().rearrangeBarcodes(data)
    print(res)

