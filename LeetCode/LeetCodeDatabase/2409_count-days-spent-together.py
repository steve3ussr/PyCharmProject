class Solution:

    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        id = []
        num_month = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        id.append(num_month[int(arriveAlice[0:2]) - 1] + int(arriveAlice[-2:]))
        id.append(num_month[int(leaveAlice[0:2]) - 1] + int(leaveAlice[-2:]))
        id.append(num_month[int(arriveBob[0:2]) - 1] + int(arriveBob[-2:]))
        id.append(num_month[int(arriveBob[0:2]) - 1] + int(arriveBob[-2:]))

        days = id[1] - id[0] + 1 + id[3] - id[2] - max(id) + min(id)

        return days if days > 0 else 0


if __name__ == '__main__':
    res = Solution().countDaysTogether("10-20", "12-22", "06-21", "07-05")
    print(res)
