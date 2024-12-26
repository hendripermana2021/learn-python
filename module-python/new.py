import mymodule
import platform

mymodule.greeting("Jonathan")

a = mymodule.person1["age"]
print(a)

x = platform.system()
c = platform.architecture()
b = dir(platform)
print("Operating System:", x, c)
print("List of Modules:", b)
