class Person :
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def printname(self) :
        print(self.fname, self.lname)

class Child(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduation = 2011
    
    def check_nama(self, fname, lname) :
        if fname == self.fname and lname == self.lname:
            return True
        else:
            return False
    

check = Child("pertama", "Kedua")
check.printname()
print(check.graduation)
print(check.check_nama("pertama", "Kedua"))