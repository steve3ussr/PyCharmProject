from pprint import pprint as pp
from pythonds.basic.Stack import Stack


class Solution(object):
    def __init__(self, sheep, lion):
        self.sheep = sheep
        self.lion = lion
        self.dp = []
        self.dp = [[None for j in range(lion + 1)] for i in range(sheep + 1)]
        self.dp[sheep][lion] = 0
        self.move = [(1, 1), (1, 0), (0, 1), (2, 0), (0, 2)]
        self.res = []

    def judge_eat(self, x, y):
        """
        only judge after go and back
        """
        if x == 0 or x == self.sheep or x == y:
            return True if self.judge_index(x, y) else False
        else:
            return False

    def judge_index(self, x, y):
        """
        judge after go and back
        """
        return True if 0 <= x <= self.sheep and 0 <= y <= self.lion else False

    def find_succ(self, a_tuple: tuple):
        x_init = a_tuple[2]
        y_init = a_tuple[3]

        for i in self.move:
            mv1_x = x_init - i[0]
            mv1_y = y_init - i[1]

            if self.judge_index(mv1_x, mv1_y):
                pass
            else:
                continue  # exit

            for j in self.move:
                mv2_x = mv1_x + j[0]
                mv2_y = mv1_y + j[1]

                if (mv2_x, mv2_y) == (x_init, y_init):
                    continue

                if self.judge_index(mv2_x, mv2_y) and (self.dp[mv2_x][mv2_y] is not None):
                    pass
                else:
                    continue

                if (mv1_x, mv1_y) == (0, 0) or (mv2_x, mv2_y) == (0, 0):
                    pass  # append
                else:
                    pass

    def main_search(self):
        path = Stack()
        path.push((3, 3, 3, 3))

        def inner():
            if path.isEmpty():
                return
            elif path.peek()[0] == path.peek()[1] == 0 or path.peek()[2] == path.peek()[3] == 0:  # find exit
                self.res = path
                path.pop()
                return
            elif not (tmp := self.find_succ(path.peek(), path.size())):  # no successor
                path.pop()
                return
            else:
                pass

            for item in tmp:
                path.push(item)
                inner()
            path.pop()

        inner()














if __name__ == '__main__':
    inst = Solution(3, 3)
    print(inst.gen_mv_list((3, 1, 3, 2)))
    inst.passing_DST()
    # pp(inst.res)  (3, 1, 3, 2), (2, 2, 3, 2)
