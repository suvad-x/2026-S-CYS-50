a = int(input("Enter obtained Marks: "))
b = int(input("Enter total number: "))

c = a * 100 / b
print(c)

if c == 0:
    print("Invalid")
elif c < 0:
    print("Invalid")
elif a > b:
    print("Invalid")
elif c >= 90:
    print("Your grade is A")
elif c >= 85:
    print("Your grade is A-")
elif c >= 80:
    print("Your grade is B+")
elif c >= 75:
    print("Your grade is B")
elif c >= 70:
    print("Your grade is B-")
elif c >= 65:
    print("Your grade is C+")
elif c >= 60:
    print("Your grade is C")
elif c >= 55:
    print("Your grade is C-")
elif c >= 50:
    print("Your grade is D")
else:
    print("Fail")