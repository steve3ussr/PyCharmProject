class Solution:
    def largestValsFromLabels(self, values: list[int], labels: list[int], numWanted: int, useLimit: int) -> int:
        return self.v2(values, labels, numWanted, useLimit)

    def v1(self, values: list[int], labels: list[int], numWanted: int, useLimit: int):
        dict_label_counter = {_: 0 for _ in labels}
        data = list(zip(values, labels))
        data.sort(key=lambda x: x[0], reverse=True)

        res = 0
        cnt = 0

        for _ in data:
            if dict_label_counter[_[1]] < useLimit:
                cnt += 1
                dict_label_counter[_[1]] += 1
                res += _[0]
            else:
                pass

            if cnt == numWanted:
                return res
        return res

    def v2(self, values: list[int], labels: list[int], numWanted: int, useLimit: int):
        dict_label_counter = {_: 0 for _ in labels}
        index = list(range(len(values)))
        index.sort(key=lambda x: -values[x])

        res = 0
        cnt = 0

        for i in index:
            if dict_label_counter[labels[i]] < useLimit:
                cnt += 1
                dict_label_counter[labels[i]] += 1
                res += values[i]
            else:
                pass

            if cnt == numWanted:
                return res
        return res


if __name__ == '__main__':
    values = [2,6,3,6,5]
    labels = [1,1,2,1,1]
    numWanted = 3
    useLimit = 1
    res = Solution().largestValsFromLabels(values, labels, numWanted, useLimit)
    print(res)