class Person :
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

p1 = Person("John", 32)

print(p1)
print(p1.age)

del p1

print(p1)