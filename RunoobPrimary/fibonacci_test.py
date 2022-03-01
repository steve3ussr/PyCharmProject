def fibo_func(k):
    list_fibo = [1, 1]
    for i in range(2, k):
        list_fibo.append(list_fibo[i - 1] + list_fibo[i - 2])
    print(list_fibo)
    return


try:
    n = int(input("enter an int num"))
    if n <= 0:
        print("please enter a number > 0")
    elif n == 1:
        print(1)
    elif n == 2:
        print(1, '\000', 1)
    else:
        fibo_func(n)
except ValueError:
    print("not an int num")
