from DSA_python.pythonds.Graph.Graph import Graph
from DSA_python.pythonds.Graph.Vertex import Vertex
from DSA_python.pythonds.basic.Stack import Stack


class KnightTourSolution(object):
    def __init__(self, r, c):
        self.row = r
        self.col = c
        self.ktGraph = Graph()
        self.mv = ((2, 1), (1, 2), (-1, 2), (-2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1))
        self._genKnightGraph()

    def _genKnightGraph(self):
        """
            KnighT's Tour -> kt
            :param r: row
            :param c: column
            :return: a chess graph
            """
        for i in range(self.row):
            for j in range(self.col):
                currId = self._pos2id(i, j)
                self.ktGraph.addVertex(currId)

                nextList = self._genMove(i, j)
                for k in nextList:
                    self.ktGraph.addEdge(currId, self._pos2id(k[0], k[1]))

    def _judgeRange(self, i, j):
        return True if 0 <= i <= (self.row - 1) and 0 <= j <= (self.col - 1) else False

    def _pos2id(self, i, j):
        """
        transfer position to vertex id
        :param i: position
        :param j: position
        :return: a int(vertex id)
        """
        if self._judgeRange(i, j):
            pass
        else:
            raise IndexError(f'position({i}, {j} out of range)')

        return i * self.col + j

    def _genMove(self, i, j):
        lst = []
        for item in self.mv:
            newX = i + item[0]
            newY = j + item[1]

            if self._judgeRange(newX, newY):
                lst.append((newX, newY))
            else:
                pass
        return lst

    def DFS_primarySolve(self, i, j):
        """
        specify initial position
        :param i: x coord
        :param j: y coord
        :return: path
        """
        path = Stack()
        st_id = self._pos2id(i, j)
        path.push(self.ktGraph.getVertex(st_id))
        limit = self.row * self.col - 1

        def _solve(length):
            currVtx = path.peek()
            print(length)
            currVtx.accessed = True
            if length == limit:
                return True
            else:
                pass

            nextList = list(currVtx.getConnections())
            finish_flg = False
            for nextVtx in nextList:
                if finish_flg:
                    break

                if nextVtx.accessed:
                    continue
                else:
                    path.push(nextVtx)
                    finish_flg = _solve(length+1)

            if not finish_flg:
                currVtx.accessed = False
                path.pop()
            return finish_flg

        print(_solve(0))

    def DFS_primaryCircleSolve(self, i, j):
        """
        specify initial position
        :param i: x coord
        :param j: y coord
        :return: path
        """
        path = Stack()
        st_id = self._pos2id(i, j)
        path.push(self.ktGraph.getVertex(st_id))

        def _solve():
            currVtx = path.peek()
            print(currVtx.id)
            currVtx.accessed = True
            if currVtx.id == st_id and path.size() != 1:
                return True
            else:
                pass

            nextList = list(currVtx.getConnections())
            finish_flg = False
            for nextVtx in nextList:
                if finish_flg:
                    break

                if nextVtx.id == st_id:
                    return True
                elif nextVtx.accessed:
                    continue
                else:
                    path.push(nextVtx)
                    finish_flg = _solve()

            if not finish_flg:
                currVtx.accessed = False
                path.pop()
            return finish_flg

        print(_solve())

    def DFS_WarnsdorffSolve(self, i, j):
        """
               specify initial position
               :param i: x coord
               :param j: y coord
               :return: path
               """
        path = Stack()
        st_id = self._pos2id(i, j)
        path.push(self.ktGraph.getVertex(st_id))
        limit = self.row * self.col - 1

        def _nextSort(aVtx: Vertex):
            orinList = list(aVtx.connectedTo.keys())
            return sorted(orinList, key=lambda x: len(list(x.connectedTo.keys())))

        def _solve(length):
            currVtx = path.peek()
            print(length)
            currVtx.accessed = True
            if length == limit:
                return True
            else:
                pass

            nextList = _nextSort(currVtx)
            finish_flg = False
            for nextVtx in nextList:
                if finish_flg:
                    break

                if nextVtx.accessed:
                    continue
                else:
                    path.push(nextVtx)
                    finish_flg = _solve(length + 1)

            if not finish_flg:
                currVtx.accessed = False
                path.pop()
            return finish_flg

        print(_solve(0))


if __name__ == '__main__':
    inst = KnightTourSolution(8, 8)
    inst.DFS_WarnsdorffSolve(0, 0)
