class Solution:
    def checkDistances(self, s: str, distance: list[int]):
        counter = [None for _ in range(26)]
        for i, char in enumerate(s):
            tmp = ord(char) - 97

            if counter[tmp] is None:
                counter[tmp] = -(i+1)
            elif counter[tmp] != -i + distance[tmp]:
                return False

        return True


if __name__ == '__main__':
    res = Solution().checkDistances("abaccb",
                                    [1, 3, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    print(res)
