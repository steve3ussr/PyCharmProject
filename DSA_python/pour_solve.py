from pprint import pprint as pp


class Solution(object):
    def __init__(self, x, y, e):
        self.__x = x
        self.__y = y
        self.__e = e
        self.__path_l2s = []
        self.__path_s2l = []

    def __l2s(self, i):
        self.__path_l2s.append(i)
        if i == self.__e:
            print('l2s Done')
        else:
            return self.__l2s(i - self.__y) if i > self.__y else self.__l2s(i + self.__x - self.__y)

    def __s2l(self, i):
        self.__path_s2l.append(i)
        if i == self.__e:
            print("s2l Done")
        else:
            return self.__s2l(tmp) if (tmp := i + self.__y) < self.__x else self.__s2l(tmp - self.__x)

    def main(self):
        self.__l2s(self.__x)
        self.__s2l(0)
        pp(self.__path_l2s) if len(self.__path_l2s) < len(self.__path_s2l) else pp(self.__path_s2l)


if __name__ == '__main__':
    Solution(11, 4, 5).main()
