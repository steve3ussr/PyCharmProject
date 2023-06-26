import operator


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        set_operator = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }
        for v in tokens:

            if v in set_operator:
                # assert len(stack) >= 2
                a = stack.pop()
                b = stack.pop()
                stack.append(int(set_operator[v](b, a)))

            else:
                stack.append(int(v))
            # print(stack)
        return stack[0]



if __name__ == '__main__':
    data = ["4","-2","/","2","-3","-","-"]
    res = Solution().evalRPN(data)
    print(res)
