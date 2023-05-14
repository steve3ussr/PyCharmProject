class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        map = {}
        for v in nums:
            if abs(v) in map:
                pass
            else:
                map[abs(v)] = set()
            map[abs(v)].add(v / abs(v))
        print(map)

        ma = -1
        for k in map:
            if len(map[k]) > 1 and k > ma:
                ma = k
        return ma

if __name__ == '__main__':
    data = [-9,-43,24,-23,-16,-30,-38,-30]
    res = Solution().findMaxK(data)
    print(res)
