# When print_i is called outside of function it only has access to value of i in global

def make_functions():
    flist = []

    for i in [1, 2, 3]:
        def print_i(x):
            print(x)

        flist.append((print_i, i))

    return flist


functions = make_functions()
for f, i in functions:
    f(i)
