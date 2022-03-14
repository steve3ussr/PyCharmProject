def add_score(i):
    try:
        i = float(i)
        print(f"the square root of {i} is {i ** 0.5}")
    except TypeError:
        print("must be a real number")
    finally:
        print("JOB DONE")


add_score(input("a real num"))
