class Solution:
    def baseNeg2(self, n: int) -> str:
        bin_pos = bin(n)[2:]
        print(bin_pos)

        bin_pos_odd = []
        bin_pos_even = []
        for i, v in enumerate(bin_pos):
            if (len(bin_pos) - i) % 2 == 1:
                bin_pos_odd.append(v)
                bin_pos_even.append('0')
            else:
                bin_pos_odd.append('0')
                bin_pos_even.append(v)

        print(f"{bin_pos} --> {bin_pos_odd} + {bin_pos_even}")

        bin_pos_even.reverse()
        for i in range(1, len(bin_pos_even), 2):
            if bin_pos_even[i] == '1':
                if i < len(bin_pos_even) - 1:
                    bin_pos_even[i + 1] = '1'
                else:
                    bin_pos_even.append('1')
        bin_pos_even.reverse()

        print(f"{bin_pos} --> {bin_pos_odd} + {bin_pos_even}")
        dec_pos_odd = int("".join(bin_pos_odd), 2)
        dec_pos_even = int("".join(bin_pos_even), 2)
        res = bin(dec_pos_odd + dec_pos_even)[2:]
        print(f"{bin_pos} --> {res}")
        if not len(res) % 2:
            res = '1' + res

        print(res)
        return res


if __name__ == '__main__':
    Solution().baseNeg2(14)
