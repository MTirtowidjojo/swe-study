# what is the output of the following?
def test1 () :
    a = [2, 3, 4]
    p = iter(a)
    print(next(p), end=" ")
    p = iter(a)
    print(next(p), end=" ")
    p = iter(a)
    print(next(p))

# what is the output of the following?
def test2 () :
    a = [2, 3, 4]
    p = iter(a)
    print(next(p), end=" ")
    print(next(p), end=" ")
    print(next(p))

# what is the output of the following?
def test3 () :
    a = [2, 3, 4]
    p = iter(a)
    try :
        while True :
            v = next(p)
            print(v, end=" ")
            v += 1
    except StopIteration :
        pass
    print(a)
