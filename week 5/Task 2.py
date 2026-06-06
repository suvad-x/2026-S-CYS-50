a = int(input("Enter obtained Marks: "))
b = int(input("Enter total Marks: "))
if b <= 0 or a < 0 or a > b:
    print("Invalid")
else:
    c = (a * 100) / b
    if c >= 90:
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