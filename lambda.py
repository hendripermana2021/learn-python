x = lambda a, b : a + b
number = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(x(1, 2))

def myFunc(x) :
    print("x", x)
    return lambda a : a * x

setFirst = myFunc(3)

multiple = list(map(lambda x:x * 2, number))
filter = list(filter(lambda x:x % 2 == 0, number))



print(multiple)
print(filter)
print(setFirst(2))