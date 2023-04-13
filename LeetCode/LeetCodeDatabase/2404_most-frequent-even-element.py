class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        dct = {}
        for _ in nums:
            if _ % 2 == 1:
                continue
            else:
                pass

            if _ in dct:
                dct[_] += 1

            else:
                dct[_] = 1

        if len(dct) == 0:
            return -1

        max_v = max(dct.values())
        return min([[k, v] for k, v in dct.items() if v == max_v], key=lambda x: x[0])[0]


if __name__ == '__main__':
    data = [0, 1, 2, 2, 4, 4, 1]
    res = Solution().mostFrequentEven(data)
    print(res)
