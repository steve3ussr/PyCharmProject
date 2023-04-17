class Solution:
    def camelMatch(self, queries: list[str], pattern: str) -> list[bool]:

        def aux(query, pat) -> bool:
            curr_q = 0

            for char in pat:
                if ord(char) < 97:  # capital
                    flg = 0
                    while curr_q < len(query):

                        if ord(query[curr_q]) < 97:
                            if query[curr_q] != char:
                                return False
                            else:
                                print(f"pattern::{char} == query[{curr_q}] == {query[curr_q]}")
                                curr_q += 1
                                flg = 1
                                break
                        else:
                            pass
                        curr_q += 1
                    if flg:
                        pass
                    else:  # cannot match capital char
                        return False

                else:  # lower
                    flg = 0
                    while curr_q < len(query) and ord(_ := query[curr_q]) >= 97:
                        if _ == char:
                            print(f"pattern::{char} == query[{curr_q}] == {query[curr_q]}")
                            flg = 1
                            curr_q += 1
                            break
                        else:
                            pass
                        curr_q += 1
                    if flg:
                        pass
                    else:
                        return False

            while curr_q < len(query):
                if ord(query[curr_q]) < 97:
                    return False
                curr_q += 1

            return True

        return [aux(_, pattern) for _ in queries]


if __name__ == '__main__':
    p = "FB"
    q_list = ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"]
    res = Solution().camelMatch(q_list, p)
    print(res)
