def myfunc():
    x=300
    def myInnerFunc():
        print(x)
    myInnerFunc()

myfunc()

"""ANOTHER SECTIOn FOR NON LOCAL SCOPE"""
def myfunc():
    x = "Jane"
    def myfunc2():
        nonlocal x
        x = "Hello"
    myfunc2()
    return x

print(myfunc())