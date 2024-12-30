class Student:
    tutor=("Bindu")
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def display(self):
        print(__class__.tutor)
        print(self.name)
        print(self.age)

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False
s1=Student("Anu",19)
s1.display()
s2=Student("Manu",20)
s2.display()
print(s1.compare(s2))

