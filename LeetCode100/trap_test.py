import unittest
from trap import Solution


class TestTrap(unittest.TestCase):
    def test_trap_opt(self):
        case_dict = {
            1: ([4, 2, 0, 3, 2, 5], 9),
            2: ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
            3: ([2, 3, 3, 2], 0),
            4: ([2, 0, 2], 2),
            5: ([2, 1, 0, 2], 3),
            6: ([4, 2, 3], 1)
        }
        inst = Solution()
        for k, v in case_dict.items():
            self.assertEqual(inst.test_max_opt(v[0]), v[1], msg=f'TEST OPT CASE {k} ERROR!')

    def test_trap(self):
        case_dict = {
            1: ([4, 2, 0, 3, 2, 5], 9),
            2: ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
            3: ([2, 3, 3, 2], 0),
            4: ([2, 0, 2], 2),
            5: ([2, 1, 0, 2], 3),
            6: ([4, 2, 3], 1)
        }
        inst = Solution()
        for k, v in case_dict.items():
            self.assertEqual(inst.test_max(v[0]), v[1], msg=f'TEST normal CASE {k} ERROR!')


if __name__ == '__main__':
    unittest.main()

