class Solution:
    def trap(self, height: list[int]):
        peek_list = []
        res_list = []
        res = 0
        for i in range(1, len(height[1:-1]) + 1):
            res += height[i]
            if height[i + 1] < height[i] > height[i - 1]:
                peek_list.append(i)
                res_list.append(res - height[i])
                res = 0

        tmp = 0
        for i in range(1, len(peek_list)):
            tmp += ((peek_list[i] - peek_list[i - 1] - 1) * min(height[peek_list[i]], height[peek_list[i - 1]]) -
                    res_list[i])
        print(tmp)
        print(res_list)

        return peek_list

    def trap_test(self, height: list[int]):
        peek_list = []
        rest_stone = 0

        height.append(0)
        h = [0]
        h.extend(height)

        tmp_sum = 0
        for i in range(1, len(h) - 1):
            tmp_sum += h[i]

            if h[i + 1] < h[i] > h[i - 1]:
                peek_list.append(i)
                rest_stone += (tmp_sum - h[i])
                tmp_sum = 0

        tmp_water = 0
        for i in range(1, len(peek_list)):
            tmp_water += (peek_list[i] - peek_list[i - 1] - 1) * min(h[peek_list[i]], h[peek_list[i - 1]])
            print(f'{(peek_list[i] - peek_list[i - 1] - 1)} * {min(h[peek_list[i]], h[peek_list[i - 1]])}')
        tmp_water -= rest_stone
        print(h)
        print(tmp_water)
        print(rest_stone)

        return peek_list

    def test_max(self, height):
        max_val = max(height)
        sum_stone = sum(height)

        first_max_index = 0
        final_res = 0
        tmp_max = 0
        for i, v in enumerate(height):
            if v == max_val:
                first_max_index = i
                break
            else:
                tmp_max = max(tmp_max, v)
                final_res += tmp_max



        second_max_index = len(height) - 1

        if first_max_index == second_max_index:
            return final_res - sum_stone + max_val

        tmp_max = 0
        for i in range(len(height) - 1, -1, -1):
            v = height[i]
            if v == max_val:
                second_max_index = i
                break
            else:
                tmp_max = max(tmp_max, v)
                final_res += tmp_max

        return final_res - sum_stone + max_val * (second_max_index - first_max_index +1)

    def test_max_opt(self, height):
        height.insert(0, 0)
        max_val = max(height)
        sum_stone = sum(height)

        first_max_index = None
        final_res = 0
        tmp_max = 0
        for i, v in enumerate(height):
            if not first_max_index:
                if v == max_val:
                    first_max_index = i
                if v >= tmp_max:
                    tmp_max = v
                final_res += tmp_max
            else:
                break

        if first_max_index == len(height) - 1:
            return final_res - sum_stone
        else:

            second_max_index = None

            tmp_max = 0
            for i in range(len(height) - 1, first_max_index - 1, -1):
                v = height[i]

                if not second_max_index:
                    if v == max_val:
                        second_max_index = i
                    if v >= tmp_max:
                        tmp_max = v

                    final_res += tmp_max

            return final_res - sum_stone + max_val * (second_max_index - first_max_index - 1)


if __name__ == '__main__':
    h2 = [4, 2, 0, 3, 2, 5]
    h = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    h3 = [2, 3, 3, 2]
    hk = [2, 1, 0, 2]
    res = Solution().test_max_opt(hk)
    print(f'res = {res}')
