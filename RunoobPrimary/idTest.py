key1 = 44
key2 = 'abc'
key3 = 42

dictA = {key1: 1, key2: 2, key3: 3}
print(dictA)

a = 21
print("a(21) ID =", end=" "), print(id(a))
a *= 2
print("key3(42) ID =", end=" "), print(id(key3))
print("a(42) ID =", end=" "), print(id(a))
print(dictA[a])

b = 22
print("b(22) ID =", end=" "), print(id(b))
b *= 2
print("key1(44) ID =", end=" "), print(id(key1))
print("b(44) ID =", end=" "), print(id(b))
print(dictA[b])
`
