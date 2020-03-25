def gen():
    for c in 'AB':
        yield c
    for i in range(1, 3):
        yield i

def gen2():
    """ gen2 等价于 gen """
    yield from 'AB'             # yield from x 其实就是 x 的迭代(循环)
    yield from range(1, 3)

# ------------------------------

def chain(*iterables):          # iterables 是不定项参数，即想给多少个参数都可以
    for it in iterables:
        yield from it           # for i in it: yield i
   

if __name__ == "__main__":
    ret = list(gen())
    ret2 = list(gen2())
    print(ret)
    print(ret2)

    # ------------------------------
    s = 'ABC'
    t = tuple(range(3))
    ret = list(chain(s, t))
    print(ret)                  # ['A', 'B', 'C', 0, 1, 2]