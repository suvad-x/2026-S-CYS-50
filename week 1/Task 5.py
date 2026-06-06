import math
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
D = b*b - 4*a*c
print("Discriminant =", D)
if D > 0:
    print("Roots are real and distinct")
elif D == 0:
    print("Roots are real and equal")
else:
    print("Roots are imaginary")
if D >= 0:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print("Root 1 =", x1)
    print("Root 2 =", x2)
else:
    real = -b / (2*a)
    imag = math.sqrt(-D) / (2*a)
    print("Root 1 =", real, "+", imag, "i")
    print("Root 2 =", real, "-", imag, "i")