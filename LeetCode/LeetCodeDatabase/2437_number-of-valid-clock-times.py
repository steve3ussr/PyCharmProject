class Solution:
    def countTime(self, time: str) -> int:
        res = 1

        if time[0] == time[1] == '?':
            res *= 24
        elif time[0] == '?':
            res *= 3 if int(time[1]) <= 3 else 2
        elif time[1] == '?':
            res *= 4 if int(time[0]) == 2 else 10
        else:
            pass

        if time[3] == '?':
            res *= 6
        if time[4] == '?':
            res *= 10

        return res


if __name__ == '__main__':
    data = "?5:24"
    res = Solution().countTime(data)
    print(res)
