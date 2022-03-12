import sys

listA = [1, 2, 3, 4]
IterObj = iter(listA)
while True:
    try:
        print(next(IterObj))
    except StopIteration:
        sys.exit()
        