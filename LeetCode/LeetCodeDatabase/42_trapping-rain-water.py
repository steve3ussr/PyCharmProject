class Solution:
    def trap(self, height: list[int]):
        st_inc = []
        res = 0
        for i in range(len(height)):
            h = []
            index = []
            while st_inc and st_inc[-1][1] < height[i]:
                _ = st_inc.pop()
                h.append(_[1])
                index.append(_[0])
            st_inc.append([i, height[i]])

            if h:
                lo = min(index)
                hi = max(index)

                res += max(h) * (hi-lo+1) - sum(h)
            print(st_inc, res, index, h)


        return res




if __name__ == '__main__':
    h2 = [4, 2, 0, 3, 2, 5]
    h = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    h3 = [2, 3, 3, 2]
    hk = [2, 1, 0, 2]
    res = Solution().trap(h)
    print(f'res = {res}')
