import unittest
from distribution_calculate import DistributionCalculate


def judge_prime_check(x: int) -> int:
    if isinstance(x, int) and x > 0:
        pass
    else:
        raise TypeError('x应为正整数')

    cnt = 0
    for i in range(1, x + 1):
        cnt += 1 if DistributionCalculate(1, i).judge_prime() else 0

    return cnt


class MyTestCase(unittest.TestCase):
    def test_judge_prime(self):
        self.assertEqual(judge_prime_check(k := 100), 25, f'{k}以内素数数量判断错误')
        self.assertEqual(judge_prime_check(k := 1000), 168, f'{k}以内素数数量判断错误')
        self.assertEqual(judge_prime_check(k := 10000), 1229, f'{k}以内素数数量判断错误')


if __name__ == '__main__':
    unittest.main()
