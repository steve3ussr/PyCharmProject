class Solution:
    def numMovesStonesII(self, stones: list[int]) -> list[int]:
        data = sorted(stones)
        op_min = 0
        op_max = 0

        while stones[-1] - stones[0] > len(stones) - 2:
            pass

        return [op_min, op_max]




if __name__ == '__main__':
    # TODO:
    #  1. lookup solve
    data = [1, 5, 2, 9]
    res = Solution().numMovesStonesII(data)
    print(res)
