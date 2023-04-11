class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        curr = [0, 0, 1]

        for instruction in instructions:

            # move
            if instruction == 'G':
                if curr[2] == 1:
                    curr[1] += 1
                elif curr[2] == 2:
                    curr[0] -= 1
                elif curr[2] == 3:
                    curr[1] -= 1
                else:
                    curr[0] += 1
            elif instruction == 'L':
                curr[2] = (curr[2] + 1) if curr[2] <= 3 else 1
            else:
                curr[2] = (curr[2]-1) if curr[2] > 1 else 4

        return False if curr[0]**2 + curr[1]**2 > 0 and curr[2] == 1 else True


if __name__ == '__main__':
    data = "GG"
    res = Solution().isRobotBounded(data)
    print(res)
