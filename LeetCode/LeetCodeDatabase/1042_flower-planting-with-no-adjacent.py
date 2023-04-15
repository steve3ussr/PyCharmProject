class Solution:
    def gardenNoAdj(self, n: int, paths: list[list[int]]) -> list[int]:
        graph = [[] for i in range(n)]
        print(graph)

        for _ in paths:
            graph[_[0]-1].append(_[1]-1)
            graph[_[1]-1].append(_[0]-1)

        res = [0] * n

        for id, connect in enumerate(graph):
            tmp = [1, 2, 3, 4]
            for _ in connect:
                if res[_] and res[_] in tmp:
                    tmp.remove(res[_])
            assert len(tmp) >= 1, ValueError
            res[id] = tmp[0]

        return res



if __name__ == '__main__':
    res = Solution().gardenNoAdj(5, [[4,1],[4,2],[4,3],[2,5],[1,2],[1,5]])
    print(res)
