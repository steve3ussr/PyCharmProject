class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []

        for _ in s:
            if _ == '#':
                if len(stack_s) > 0:
                    stack_s.pop()
                else:
                    pass
            else:
                stack_s.append(_)

        for _ in t:
            if _ == '#':
                if len(stack_t) > 0:
                    stack_t.pop()
                else:
                    pass
            else:
                stack_t.append(_)

        return False if stack_s != stack_t else True



