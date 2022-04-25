from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        hashmap = {}
        for i, k in enumerate(nums):
            if k in hashmap:
                hashmap[k][0] += 1
                hashmap[k][2] = i
            else:
                hashmap[k] = [1, i, i]

        for k in hashmap.keys():
            hashmap[k][0] = - hashmap[k][0]
            hashmap[k][1] = hashmap[k].pop() - hashmap[k][1] + 1

        return min(hashmap.values())[1]


if __name__ == '__main__':
    '[1,2,2,3,1,4,2]'
    testList = [1,2,2,3,1,4,1,2]
    ans = Solution().findShortestSubArray(testList)
    print(ans)




