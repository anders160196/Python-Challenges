shape = input("Input shape: ") #T = Triangle, R = Rectangle, C = Circle

if shape == "T":
    b = int(input("Input the base : "))
    h = int(input("Input the height : "))
    area = b*h/2
elif shape == "R":
    w = int(input("Input the width : "))
    h = int(input("Input the height : "))
    area = w*h
elif shape == "C":
    r = int(input("Input the radius : "))
    area = 3.14*r*r

print("area = ", area)
