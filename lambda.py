a=int(input("Enter the sides of squares:"))
s_area=lambda a:a*a
print("Area of square is:",s_area(a))
l=int(input("Enter the length of rectangle:"))
b=int(input("Enter the breadth of rectangle:"))
r_area=lambda l,b:l*b
print("Area of rectangle is:",r_area(l,b))
b=int(input("Enter the base of the triangle:"))
h=int(input("Enter the height of the triangle:"))
t_area=lambda b,h:(h*b)/2
print("Area of triangle is:",t_area(b,h))







