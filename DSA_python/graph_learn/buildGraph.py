from DSA_python.pythonds.Graph.Graph import Graph
from english_words import english_words_lower_set as words_set

for _ in words_set:
    print(_)

print(len(words_set))
print(type(words_set))
print(sorted(words_set))
