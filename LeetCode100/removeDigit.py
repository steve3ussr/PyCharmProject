class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        eleRes = None  # 应该删除的index
        eleLast = None  # 上一个相同的元素index
        eleCurrent = None  # 当前相同的元素index
        for i, v in enumerate(number[:number.rindex(digit)+1]):
            if v == digit:
                # 先解决各种情况下的赋值问题
                if eleCurrent is None:
                    eleCurrent = i
                    eleRes = i
                    continue
                else:
                    eleLast = eleCurrent
                    eleCurrent = i

                # case 1: Last和Curent一样，那就没有区别，continue
                if eleCurrent == eleLast + 1:
                    continue
                # case 2: Last和Curent不一样，比较last和last+1
                else:
                    if number[eleLast + 1] > number[eleLast]:
                        eleRes = eleLast
                        break  # 越往后越没用，所以可以break
                    else:
                        eleRes = eleCurrent

            else:
                pass

        res = list(number)
        res.pop(eleRes)
        return "".join(res)


if __name__ == '__main__':
    test_number = "5453511111"
    a_digit = "5"
    ans = Solution().removeDigit(test_number, a_digit)
    print(ans)

