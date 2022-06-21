import unittest
from simp_func import add_one


class TestAfunc(unittest.TestCase):



    def test_add_one(self):
        in_var = [1, 2, 5, 'a', 114.514]
        out_var = [2, 3, 666, 'a', 114.514]
        print(f'共 {len(in_var)} 个测试用例')
        i = 0
        for u, v in zip(in_var, out_var):
            i += 1
            self.assertEqual(add_one(u), v, msg=f'测试用例 {i} 异常')


if __name__ == '__main__':
    unittest.main(argv=['first-arg-ignored'], exit=False)
