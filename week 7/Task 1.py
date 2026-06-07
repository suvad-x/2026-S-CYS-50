c = int(input("Enter Total Number of Students: "))
while c > 0:
    name = input("Enter Student Name : ")
    roll_num = input("Enter Student Roll Number : ")
    a = int(input("Enter Obtained marks : "))
    b = a * 100 / 300
    print(f"Name is {name}")
    print(f"Rollnumber is {roll_num}")
    print(f"Percentage is {b}")
    if b >= 90:
        print("Your grade is A")
    elif b >= 85:
        print("Your grade is A-")
    elif b >= 80:
        print("Your grade is B+")
    elif b >= 75:
        print("Your grade is B")
    elif b >= 70:
        print("Your grade is B-")
    elif b >= 65:
        print("Your grade is C+")
    elif b >= 60:
        print("Your grade is C")
    elif b >= 55:
        print("Your grade is C-")
    elif b >= 50:
        print("Your grade is D")
    else:
        print("Fail")
    c = c - 1
