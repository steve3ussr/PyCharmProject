from DSA_python.pythonds.Graph.DFSGraph import DFSGraph


def muffinMaking():
    muffinGraph = DFSGraph()
    muffinGraph.addVertex('3/4杯牛奶')
    muffinGraph.addVertex('一个鸡蛋')
    muffinGraph.addVertex('一勺油')
    muffinGraph.addVertex('一杯松饼粉')
    muffinGraph.addVertex('加热枫糖浆')
    muffinGraph.addVertex('加热平底锅')
    muffinGraph.addVertex('倒入1/4杯')
    muffinGraph.addVertex('出现气泡时翻面')
    muffinGraph.addVertex('开始享用')

    muffinGraph.addEdge('3/4杯牛奶', '一杯松饼粉')
    muffinGraph.addEdge('一个鸡蛋', '一杯松饼粉')
    muffinGraph.addEdge('一勺油', '一杯松饼粉')
    muffinGraph.addEdge('一杯松饼粉', '倒入1/4杯')
    muffinGraph.addEdge('一杯松饼粉', '加热枫糖浆')
    muffinGraph.addEdge('加热平底锅', '倒入1/4杯')
    muffinGraph.addEdge('倒入1/4杯', '出现气泡时翻面')
    muffinGraph.addEdge('出现气泡时翻面', '开始享用')
    muffinGraph.addEdge('加热枫糖浆', '加热枫糖浆')

    muffinGraph.dfs()

    res = sorted(muffinGraph, key=lambda x: x.finTime, reverse=True)
    for i in res:
        print(i.id)


if __name__ == '__main__':
    muffinMaking()
