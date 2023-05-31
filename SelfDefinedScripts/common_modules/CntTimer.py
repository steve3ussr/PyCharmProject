from threading import Timer


class CntTimer(Timer):
    def __init__(self, cnt_max, time_sub, func, *args, **kwargs):
        super(CntTimer, self).__init__(time_sub, func, args, kwargs)
        self.cnt_max = cnt_max

    def run(self):
        cnt = 0
        while not self.finished.is_set() and cnt < self.cnt_max:
            self.finished.wait(self.interval)
            self.function(*self.args, **self.kwargs)
            cnt += 1


if __name__ == '__main__':
    def f(*args):
        print(sum(args))
    t = CntTimer(10, 2, f, 6, 3)
    t.start()