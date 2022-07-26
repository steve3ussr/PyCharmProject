import pprint
import sys


class Solution(object):
    def __init__(self, large: int, small: int, expected: int):
        self.path1 = []
        self.path2 = []
        self.l_limit = large
        self.s_limit = small
        self.e = expected
        self.l = 0
        self.s = 0
        self.init_l2s()
        self.init_s2l()


    def l2s(self):
        s_rest = self.s_limit - self.s
        if s_rest == 0:
            self.s = 0

        elif self.l == 0:
            self.l += self.l_limit

        elif s_rest > self.l:
            self.s += self.l
            self.l = 0

        else:
            self.s += s_rest
            self.l -= s_rest

        self.path1.append((self.l, self.s))

    def s2l(self):
        l_rest = self.l_limit - self.l
        if l_rest == 0:
            self.l = 0

        elif self.s == 0:
            self.s += self.s_limit

        elif l_rest > self.s:
            self.l += self.s
            self.s = 0

        else:
            self.l += l_rest
            self.s -= l_rest

        self.path2.append((self.l, self.s))

    def init_l2s(self):
        self.l = self.l_limit
        self.s = 0
        self.path1.append((self.l, self.s))
        while self.l != self.e:
            self.l2s()

    def init_s2l(self):
        self.s = self.s_limit
        self.l = 0
        self.path2.append((self.l, self.s))
        while self.l != self.e:
            self.s2l()

    def exec(self):
        return self.path1 if len(self.path1) <= len(self.path2) else self.path2


if __name__ == '__main__':
    inst = Solution(4, 3, 2)
    pprint.pprint(inst.exec())
