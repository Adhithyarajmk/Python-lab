class Rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        return(self.length * self.breadth)
    def perimeter(self):
        return 2 *(self.length+ self.breadth)
    def compare(self,other):
        if self.area()==other.area():
            return " Area is same"
        else:
            return "Area is different"
l1=int(input("enter the length1:"))
b1=int(input("enter the breadth1:"))
l2=int(input("enter the length2:"))
b2=int(input("enter the breadth2:"))
r1=Rectangle(l1,b1)
r2=Rectangle(l2,b2)
r1.area()
r1.perimeter()
print("area of r1 is",r1.area())
print(" perimeter of r1 is",r1.perimeter())
r2.area()
r2.perimeter()
print("area  of r2 is",r2.area())
print("perimeter  of r2 is",r2.perimeter())
print(r1.compare(r2))