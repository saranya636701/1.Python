def triangle():
    Height = int(input("Height: "))
    Breadth = int(input("Breadth: "))
    print("Area formula: (Height*Breadth)/2")
    Area = (Height*Breadth)/2
    print("Area of triangle: ", Area)
    Height1 = int(input("Height1: "))
    Height2 = int(input("Height2:"))
    Breadth1 = int(input("Breadth1: "))
    print("Perimeter formula: Height1+Height2+Breadth1")
    Perimeter = Height1 + Height2 + Breadth1
    print("Perimeter of triangle: ", Perimeter)
triangle()

