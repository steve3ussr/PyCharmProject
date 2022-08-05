from DSA_python.pythonds.Graph.Graph import Graph
from english_words import english_words_lower_set as words_set
from pprint import pprint as pp
import re


def buildGraphWordLadder(word1, word2):
    """
    :param word1: a from word
    :param word2: a  to  word
    :return:      a word ladder, class <'graph'>
    """

    # args verify
    if len(word1) != len(word2):
        raise SyntaxError(f'{word1} and {word2} have different length')
    else:
        pass

    # word dict filter
    same_len_list = list(filter(lambda x: len(x) == len(word1), words_set))

    # define a graph
    word_graph = Graph()

    def _buildGraphWordLadder(aword):
        """
        :param aword: a word like 'hape'
            reg match '.ape', 'h.pe', 'ha.e', 'hap.', and connect

        :return: None
        """
        for _ in range(len(aword)):
            match_word_list = []
            regexp = aword[:_] + '.' + aword[_ + 1:]

            # put matched in a bucket
            for pot in same_len_list:
                if re.match(regexp, pot):
                    match_word_list.append(pot)
                    word_graph.addVertex(pot)

            # connect
            for item_1 in match_word_list:
                for item_2 in match_word_list:
                    if item_1 != item_2:
                        word_graph.addEdge(item_1, item_2)

    for item in same_len_list:
        _buildGraphWordLadder(item)

    return word_graph


if __name__ == '__main__':
    res_graph = buildGraphWordLadder('fool', 'sage')

