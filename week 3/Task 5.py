def calculate_gpa():
    subjects = int(input("Enter number of subjects: "))
    total_grade_points = 0
    total_credits = 0
    for i in range(subjects):
        print("\nSubject", i + 1)
        gp = float(input("Enter Grade Point: "))
        credit = int(input("Enter Credit Hours: "))
        total_grade_points += gp * credit
        total_credits += credit
    if total_credits == 0:
        print("Total credits cannot be zero!")
    else:
        gpa = total_grade_points / total_credits
        print("\nYour GPA for this semester is:", round(gpa, 2))
calculate_gpa()