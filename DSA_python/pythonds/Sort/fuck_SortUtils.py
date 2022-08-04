import unittest
from .SortUtils import SortUtils
import random
from copy import copy


rand_num_dict = dict()
for i in range(1, 5001):
    tmp_1 = [int(random.random()*1000) for x in range(1, 100)]
    tmp_2 = sorted(tmp_1)
    rand_num_dict[i] = (tmp_1, tmp_2)


class testcase_collection(unittest.TestCase):
    def setUp(self) -> None:
        self.cls = SortUtils

    def test_bubbleSort(self):
        for k, v in rand_num_dict.items():
            self.assertEqual(self.cls.bubbleSort(copy(v[0])), v[1], msg=f'BUBBLE SORT case: {k} ERROR')

    def test_shortBubbleSort(self):
        for k, v in rand_num_dict.items():
            self.assertEqual(self.cls.shortBubbleSort(copy(v[0])), v[1], msg=f'short BUBBLE SORT case: {k} ERROR')

    def test_biBubbleSort(self):
        for k, v in rand_num_dict.items():
            self.assertEqual(self.cls.biBubbleSort(copy(v[0])), v[1], msg=f'BI-BUBBLE SORT case: {k} ERROR')

    def test_selectionSort(self):
        for k, v in rand_num_dict.items():
            self.assertEqual(self.cls.selectionSort(copy(v[0])), v[1], msg=f'SELECTION SORT case: {k} ERROR')

    def test_insertionSort(self):
        for k, v in rand_num_dict.items():
            self.assertEqual(self.cls.insertionSort(copy(v[0])), v[1], msg=f'INSERTION SORT case: {k} ERROR')

    def test_shellSort(self):
        for k, v in rand_num_dict.items():
            self.assertEqual(self.cls.shellSort(copy(v[0]), base=3), v[1], msg=f'SHELL SORT case: {k} ERROR')

    def test_mergeSort(self):
        for k, v in rand_num_dict.items():
            self.assertEqual(self.cls.mergeSort(copy(v[0])), v[1], msg=f'MERGE SORT case: {k} ERROR')

    def test_mergeSort_Opt(self):
        for k, v in rand_num_dict.items():
            self.assertEqual(self.cls.mergeSort_Opt(copy(v[0])), v[1], msg=f'MERGE SORT(low memo ver.) case: {k} ERROR')

    def test_quickSort(self):
        for k, v in rand_num_dict.items():
            self.assertEqual(self.cls.quickSort(copy(v[0])), v[1], msg=f'QUICK SORT case: {k} ERROR')

    def test_quickSort_Opt(self):
        for k, v in rand_num_dict.items():
            self.assertEqual(self.cls.quickSort_Opt(copy(v[0])), v[1], msg=f'QUICK SORT(OPT ver.) case: {k} ERROR')

    def test_bucketSort(self):
        for k, v in rand_num_dict.items():
            self.assertEqual(self.cls.bucketSort(v[0], size=100), v[1], msg=f'BUCKET SORT case: {k} ERROR')

    def test_heapSort(self):
        for k, v in rand_num_dict.items():
            self.assertEqual(self.cls.heapSort(copy(v[0])), v[1], msg=f'HEAP SORT case: {k} ERROR')

    def test_radixSort(self):
        for k, v in rand_num_dict.items():
            self.assertEqual(self.cls.radixSort(copy(v[0])), v[1], msg=f'RADIX SORT case: {k} ERROR')

    def test_countingSort(self):
        for k, v in rand_num_dict.items():
            self.assertEqual(self.cls.countingSort(copy(v[0])), v[1], msg=f'RADIX SORT case: {k} ERROR')

    def test_builtInSort(self):
        for k, v in rand_num_dict.items():
            tmp = copy(v[0])
            tmp.sort()
            self.assertEqual(tmp, v[1], msg=f'QUICK SORT case: {k} ERROR')

    def tearDown(self):
        print('--- PARTIAL --- DONE ---')


if __name__ == '__main__':
    unittest.main()
