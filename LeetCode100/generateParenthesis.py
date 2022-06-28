class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        if n == 1:
            return ['()']
        else:
            res_last = self.generateParenthesis(n-1)
            res = []
            for item in res_last:
                res.append('(' + item + ')')
                res.append('()' + item)
                res.append(item + '()')

        res.remove('()' * n)
        return res


if __name__ == '__main__':
    res = Solution().generateParenthesis(10)
    print(f'{len(res)}: {res}')

, '()((()))', '()(()())',                            '()(())()', '()(())()'

haodhaa , '()((()))', '()(()())',