from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits:
            pass
        else:
            return []

        phone_dict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        def backtrack(i):
            if i == len(digits):
                comb_sum.append("".join(comb_sub))
            else:
                letters = phone_dict[digits[i]]
                for j in letters:
                    comb_sub.append(j)
                    backtrack(i + 1)
                    comb_sub.pop()

        comb_sub = []
        comb_sum = []
        backtrack(0)
        return comb_sum


nums = '2345'
res = Solution().letterCombinations(nums)
print(res)


