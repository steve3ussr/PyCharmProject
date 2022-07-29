from pprint import pprint as pp


class Solution(object):
    def __init__(self, sheep, lion):
        self.sheep = sheep
        self.lion = lion
        self.dp = list([list([None for j in range(lion+1)]) for i in range(sheep+1)])
        self.dp[sheep][lion] = 0
        self.move = [(1, 1), (1, 0), (0, 1), (2, 0), (0, 2)]

    def judge_eat(self, x, y):
        """
        only judge after go and back
        """
        if x == 0 or x == self.sheep or x == y:
            return True
        else:
            return False

    def judge_index(self, x, y):
        """
        judge after go and back
        """
        return True if 0 <= x <= self.sheep and 0 <= y <= self.lion else False

    def passing(self, a_list):
        next_list = set()
        for last_step in a_list:
            a = last_step[0]
            b = last_step[1]
            current_step = self.dp[a][b]

            for mv_f in self.move:
                status_f = (a - mv_f[0], b - mv_f[1])

                if self.judge_index(status_f[0], status_f[1]):
                    pass
                else:
                    continue

                if status_f == (0, 0):
                    print('DONE')
                    return

                for mv_r in self.move:
                    status_r = (status_f[0] + mv_r[0], status_f[1] + mv_r[1])

                    if self.judge_index(status_r[0], status_r[1]) and self.judge_eat(status_r[0], status_r[1]):
                        print(status_r)
                        if self.dp[status_r[0]][status_r[1]] is not None:
                            continue
                        else:
                            self.dp[status_r[0]][status_r[1]] = current_step + 1
                            next_list.add((status_r[0], status_r[1]))

                    else:
                        continue

        temp = list(next_list)
        if temp:
            return self.passing(temp)
        else:
            pass


if __name__ == '__main__':
    inst = Solution(3, 3)
    tmp = inst.passing([(3, 3)])
    print(tmp)
    pp(inst.dp)

