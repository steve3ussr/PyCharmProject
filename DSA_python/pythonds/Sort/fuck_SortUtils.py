import unittest
from .SortUtils import SortUtils
import random


class testcase_collection(unittest.TestCase):
    def setUp(self) -> None:
        self.cls = SortUtils
        self.case = dict()
        for i in range(1, 11):
            tmp_1 = [int(random.random() * 1000) for x in range(1, 5000)]
            tmp_2 = sorted(tmp_1)
            self.case[i] = (tmp_1, tmp_2)

    def test_bubbleSort(self):
        for k, v in self.case.items():
            self.assertEqual(self.cls.bubbleSort(v[0]), v[1], msg=f'BUBBLE SORT case: {k} ERROR')

    def test_shortBubbleSort(self):
        for k, v in self.case.items():
            self.assertEqual(self.cls.shortBubbleSort(v[0]), v[1], msg=f'short BUBBLE SORT case: {k} ERROR')

    def test_selectionSort(self):
        for k, v in self.case.items():
            self.assertEqual(self.cls.selectionSort(v[0]), v[1], msg=f'SELECTION SORT case: {k} ERROR')

    def test_insertionSort(self):
        for k, v in self.case.items():
            self.assertEqual(self.cls.insertionSort(v[0]), v[1], msg=f'INSERTION SORT case: {k} ERROR')

    def test_shellSort(self):
        for k, v in self.case.items():
            self.assertEqual(self.cls.shellSort(v[0]), v[1], msg=f'SHELL SORT case: {k} ERROR')

    def test_mergeSort(self):
        for k, v in self.case.items():
            self.assertEqual(self.cls.mergeSort(v[0]), v[1], msg=f'MERGE SORT case: {k} ERROR')

    def test_mergeSort_Opt(self):
        for k, v in self.case.items():
            self.assertEqual(self.cls.mergeSort_Opt(v[0]), v[1], msg=f'MERGE SORT(low memo ver.) case: {k} ERROR')

    def tearDown(self):
        print('--- PARTIAL --- DONE ---')
        """         
         def test_quickSort(self):
             for k, v in self.case.items():
                 self.assertEqual(self.cls.quickSort(v[0]), v[1], msg=f'QUICK SORT case: {k} ERROR')

         def test_quickSort_Opt(self):
             for k, v in self.case.items():
                 self.assertEqual(self.cls.quickSort_Opt(v[0]), v[1], msg=f'QUICK SORT(OPT ver.) case: {k} ERROR')



         """


def gen_suite():
    suite = unittest.TestSuite()
    suite.addTest(testcase_collection)
    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    gen_suite()
