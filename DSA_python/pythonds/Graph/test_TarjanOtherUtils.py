import unittest

from DSA_python.pythonds.Graph import TarjanOtherUtils
from DSA_python.pythonds.Graph.DFSGraph import DFSGraph


class MyTestCase(unittest.TestCase):

    case_dict = {
        1: [
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
            [['A', 'B'],
             ['A', 'C'],
             ['A', 'G'],
             ['B', 'H'],
             ['H', 'A'],
             ['C', 'F'],
             ['G', 'F'],
             ['F', 'A'],
             ['C', 'D'],
             ['D', 'E']
             ],
            {'A', 'C', 'D'}
        ],
        2: [
            ['B', 'A', 'C', 'D', 'E', 'F', 'G', 'H'],
            [['A', 'B'],
             ['B', 'C'],
             ['C', 'D'],
             ['D', 'A'],
             ['D', 'E'],
             ['E', 'F'],
             ['F', 'G'],
             ['G', 'H'],
             ['H', 'F']
             ],
            {'D', 'E', 'F'}
        ],
        3: [
            ['B', 'A', 'C', 'D', 'E'],
            [['A', 'B'],
             ['A', 'C'],
             ['B', 'C'],
             ['B', 'D'],
             ['B', 'E'],
             ['D', 'E'],
             # ['E', 'F']
             ],
            {'B'}
        ],
        4: [
            ['B', 'A', 'C', 'D', 'E', 'F'],
            [['A', 'B'],
             ['A', 'C'],
             ['B', 'C'],
             ['B', 'D'],
             ['B', 'E'],
             ['D', 'E'],
             ['E', 'F']
             ],
            {'B', 'E'}
        ],
        5: [
            ['B', 'A', 'C', 'D', 'E', 'F'],
            [
                ['A', 'B'],
                ['A', 'F'],
                ['B', 'C'],
                ['B', 'D'],
                ['C', 'D'],
                ['C', 'E'],
                ['E', 'F']
            ],
            set()
        ]
    }

    def test_cutVtxTarjan(self):
        for k, item in self.case_dict.items():
            tmp_graph = DFSGraph().build_undirected(item[0], item[1])
            res = TarjanOtherUtils.cutVtxTarjan(tmp_graph)
            self.assertEqual(res, item[2])

    def test_cutVtxTarjan_opt(self):
        for k, item in self.case_dict.items():
            tmp_graph = DFSGraph().build_undirected(item[0], item[1])
            res = TarjanOtherUtils.cutVtxTarjan_opt(tmp_graph)
            self.assertEqual(res, item[2])


if __name__ == '__main__':
    unittest.main()
