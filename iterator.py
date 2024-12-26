mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

for x in mytuple:
    print(x)


""" THIS SECTION and SEPARATED METHOD OR THEORY OF THIS SECTION"""
class MyNumber:
    def __iter__(self):
        self.a = 1
        print("masuk di __iter__, a:", self.a)
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        print("masuk di __next__, x: " , x)
        return x
    
myclass = MyNumber()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


""" THIS SECTION and SEPARATED METHOD OR THEORY OF THIS SECTION"""
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else : 
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter : 
    print(x)