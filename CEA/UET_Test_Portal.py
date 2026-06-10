import time
import random

# ── Configuration ──────────────────────────────────────────
RIGHT_POINTS = 4
WRONG_POINTS = -1
NO_ATTEMPT_POINTS = 0
LOGIN_TRIES = 3

# ── Login Details ──────────────────────────────────────────
ADMIN_ID = "Admin"
ADMIN_PW = "12345"
STD_ID   = "Dawar"
STD_PW   = "12345"

# ── Updated Physics-Focused Question Bank ─────────────────
quiz_items = [
    {"id":1, "topic":"Physics", "text":"What is the SI unit of pressure?", "opts":{"A":"Pascal", "B":"Joule", "C":"Watt", "D":"Newton"}, "correct":"A"},
    {"id":2, "topic":"Physics", "text":"The formula for potential energy is?", "opts":{"A":"1/2 mv²", "B":"mgh", "C":"mv", "D":"F×d"}, "correct":"B"},
    {"id":3, "topic":"Math", "text":"Cos(0°) equals?", "opts":{"A":"1", "B":"0", "C":"0.5", "D":"-1"}, "correct":"A"},
    {"id":4, "topic":"Physics", "text":"Which law explains why we wear seatbelts?", "opts":{"A":"Newton's 1st Law", "B":"Newton's 2nd Law", "C":"Newton's 3rd Law", "D":"Law of Gravitation"}, "correct":"A"},
    {"id":5, "topic":"Chemistry", "text":"Atomic number of Oxygen?", "opts":{"A":"6", "B":"7", "C":"8", "D":"9"}, "correct":"C"},
    {"id":6, "topic":"Physics", "text":"1 kWh is equal to how many Joules?", "opts":{"A":"3.6×10⁶", "B":"3.6×10⁵", "C":"3.6×10⁷", "D":"3.6×10⁸"}, "correct":"A"},
    {"id":7, "topic":"Math", "text":"Square root of 169?", "opts":{"A":"11", "B":"12", "C":"13", "D":"14"}, "correct":"C"},
    {"id":8, "topic":"Physics", "text":"Reflection of light follows which law?", "opts":{"A":"Angle i = Angle r", "B":"i + r = 90°", "C":"i > r", "D":"i < r"}, "correct":"A"},
    {"id":9, "topic":"Physics", "text":"Unit of frequency?", "opts":{"A":"Hertz", "B":"Newton", "C":"Pascal", "D":"Watt"}, "correct":"A"},
    {"id":10, "topic":"Chemistry", "text":"Symbol of Potassium?", "opts":{"A":"P", "B":"Po", "C":"K", "D":"Pt"}, "correct":"C"},
    {"id":11, "topic":"Physics", "text":"Current is the rate of flow of?", "opts":{"A":"Charge", "B":"Voltage", "C":"Resistance", "D":"Power"}, "correct":"A"},
    {"id":12, "topic":"Physics", "text":"What is the escape velocity on Earth (approx)?", "opts":{"A":"7.8 km/s", "B":"11.2 km/s", "C":"9.8 km/s", "D":"3×10⁸ m/s"}, "correct":"B"},
]

student_records = []

# ── Display Helpers ───────────────────────────────────────
def separator():
    print("=" * 55)

def show_title(title):
    separator()
    print(f"     {title.center(45)}")
    separator()

def performance_grade(percentage):
    if percentage >= 80: return "EXCELLENT"
    if percentage >= 65: return "GOOD"
    if percentage >= 50: return "AVERAGE"
    return "NEEDS IMPROVEMENT"

def compute_result(user_responses):
    right = wrong = skipped = 0
    for index, item in enumerate(quiz_items):
        reply = user_responses.get(index, "S")
        if reply == "S":
            skipped += 1
        elif reply == item["correct"]:
            right += 1
        else:
            wrong += 1
    obtained = right * RIGHT_POINTS + wrong * WRONG_POINTS
    total_possible = len(quiz_items) * RIGHT_POINTS
    percent = round((obtained / total_possible) * 100, 2) if total_possible else 0
    return right, wrong, skipped, obtained, total_possible, percent

def authenticate(portal_type, valid_id, valid_pw):
    show_title(f"{portal_type} Login")
    for trial in range(1, LOGIN_TRIES + 1):
        uid = input("Enter Username : ").strip()
        pwd = input("Enter Password : ").strip()
        if uid == valid_id and pwd == valid_pw:
            print("\n✅ Login Successful!\n")
            time.sleep(0.7)
            return True
        print(f"❌ Wrong credentials. Attempt {trial}/{LOGIN_TRIES}")
    print("⛔ Login failed. Try again later.\n")
    return False

# ── Admin Features ────────────────────────────────────────
def show_all_questions():
    show_title("Question Bank")
    for num, item in enumerate(quiz_items, 1):
        print(f"\nQ{num}. [{item['topic']}] {item['text']}")
        for let, txt in item["opts"].items():
            print(f"   {let}) {txt}")
        print(f"   Correct: {item['correct']}")

def add_new_item():
    show_title("Add New Question")
    sub = input("Subject: ").strip()
    que = input("Question Text: ").strip()
    opts = {}
    for ch in ["A","B","C","D"]:
        opts[ch] = input(f"Option {ch}: ").strip()
    ans = input("Correct Option (A/B/C/D): ").strip().upper()
    if ans not in "ABCD":
        print("Invalid option!")
        return
    quiz_items.append({"id": len(quiz_items)+1, "topic": sub, "text": que, "opts": opts, "correct": ans})
    print("✅ Question added successfully!")

def remove_item():
    show_all_questions()
    try:
        idx = int(input("\nEnter question number to remove: ")) - 1
        if 0 <= idx < len(quiz_items):
            quiz_items.pop(idx)
            print("✅ Question removed!")
        else:
            print("Invalid number.")
    except:
        print("Please enter a valid number.")

def bank_overview():
    show_title("Bank Overview")
    print(f"Total Questions : {len(quiz_items)}")
    count_map = {}
    for q in quiz_items:
        count_map[q["topic"]] = count_map.get(q["topic"], 0) + 1
    for sub, cnt in count_map.items():
        print(f"   {sub}: {cnt}")

def show_records():
    show_title("All Student Records")
    if not student_records:
        print("No records available yet.")
        return
    print(f"{'No':<3} {'Name':<15} {'Roll':<10} {'Marks':<7} {'%':<6} {'Grade':<15} {'Date'}")
    separator()
    for i, rec in enumerate(student_records, 1):
        print(f"{i:<3} {rec['name']:<15} {rec['roll']:<10} {rec['marks']:<7} {rec['perc']:<6} {rec['grade']:<15} {rec['timestamp']}")

def detailed_view():
    show_records()
    if not student_records: return
    try:
        pos = int(input("\nEnter record number: ")) - 1
        rec = student_records[pos]
    except:
        print("Invalid choice.")
        return
    show_title(f"Review - {rec['name']}")
    for i, item in enumerate(quiz_items):
        ans_given = rec["responses"].get(i, "S")
        mark = "✅" if ans_given == item["correct"] else ("—" if ans_given == "S" else "❌")
        print(f"Q{i+1}. {item['text']}")
        print(f"   Answered: {ans_given}   Correct: {item['correct']}   {mark}")

def overall_stats():
    show_title("Class Performance")
    if not student_records:
        print("No data yet.")
        return
    marks_list = [r["marks"] for r in student_records]
    perc_list = [r["perc"] for r in student_records]
    passed_count = sum(1 for p in perc_list if p >= 50)
    print(f"Highest Marks : {max(marks_list)}")
    print(f"Lowest Marks  : {min(marks_list)}")
    print(f"Average Marks : {sum(marks_list)/len(marks_list):.1f}")
    print(f"Pass Percentage : {passed_count}/{len(student_records)}")
    for g in ["EXCELLENT","GOOD","AVERAGE","NEEDS IMPROVEMENT"]:
        print(f"   {g}: {sum(1 for r in student_records if r['grade']==g)}")

def admin_section():
    if not authenticate("Admin", ADMIN_ID, ADMIN_PW): return
    options = {
        "1": ("Show All Questions", show_all_questions),
        "2": ("Add Question", add_new_item),
        "3": ("Remove Question", remove_item),
        "4": ("Bank Overview", bank_overview),
        "5": ("All Records", show_records),
        "6": ("Detailed Review", detailed_view),
        "7": ("Class Statistics", overall_stats),
        "8": ("Logout", None)
    }
    while True:
        show_title("Admin Dashboard")
        for num, (label, _) in options.items():
            print(f"  {num}. {label}")
        sel = input("\nEnter choice: ").strip()
        if sel == "8": break
        if sel in options and options[sel][1]:
            options[sel][1]()
        else:
            print("Invalid choice.")

# ── Student Section ───────────────────────────────────────
def display_rules():
    show_title("Examination Guidelines")
    print("• Choose A, B, C or D")
    print("• Type S to skip a question")
    print(f"• +{RIGHT_POINTS} for correct | {WRONG_POINTS} for wrong | {NO_ATTEMPT_POINTS} for skip")
    print("• You can type SUBMIT to finish early")

def begin_test(stu_name, stu_roll):
    show_title("ECAT Test in Progress")
    responses = {}
    for idx, item in enumerate(quiz_items):
        print(f"\nQ{idx+1}/{len(quiz_items)}. [{item['topic']}] {item['text']}")
        for k, v in item["opts"].items():
            print(f"   {k}) {v}")
        while True:
            reply = input("\nYour Answer (A/B/C/D/S | SUBMIT): ").strip().upper()
            if reply == "SUBMIT":
                print("Test submitted early.")
                break
            if reply in ["A","B","C","D","S"]:
                responses[idx] = reply
                break
            print("Invalid input. Please try again.")
        if reply == "SUBMIT": break

    right, wrong, skip, marks, total, perc = compute_result(responses)
    grd = performance_grade(perc)
    current_time = time.strftime("%d-%b-%Y %H:%M")

    student_records.append({
        "name": stu_name,
        "roll": stu_roll,
        "marks": marks,
        "perc": perc,
        "grade": grd,
        "timestamp": current_time,
        "responses": responses,
        "right": right,
        "wrong": wrong,
        "skip": skip
    })

    show_title("Test Result")
    print(f"Student    : {stu_name}")
    print(f"Roll No.   : {stu_roll}")
    print(f"Score      : {marks} / {total}")
    print(f"Percentage : {perc}%")
    print(f"Grade      : {grd}")
    print(f"\nCorrect : {right} | Wrong : {wrong} | Skipped : {skip}")
    separator()
    print("\nQuestion-wise Review:")
    for i, item in enumerate(quiz_items):
        given = responses.get(i, "S")
        res = "✅" if given == item["correct"] else ("—" if given == "S" else "❌")
        print(f"Q{i+1}. {res}  Your Ans: {given}   Correct: {item['correct']}")

def student_section():
    if not authenticate("Student", STD_ID, STD_PW): return
    show_title("Student Dashboard")
    name = input("Enter Full Name : ").strip()
    roll = input("Enter Roll No   : ").strip()
    options = {"1": "Start Test", "2": "View Rules", "3": "Logout"}
    while True:
        show_title("Student Menu")
        for k, v in options.items():
            print(f"  {k}. {v}")
        choice = input("\nSelect option: ").strip()
        if choice == "1":
            begin_test(name, roll)
        elif choice == "2":
            display_rules()
        elif choice == "3":
            break
        else:
            print("Invalid option.")

# ── Main Entry Point ──────────────────────────────────────
def main():
    while True:
        show_title("ECAT TEST PORTAL")
        print("  1. Admin Dashboard")
        print("  2. Student Dashboard")
        print("  3. Exit Application")
        sel = input("\nChoose Portal: ").strip()
        if sel == "1":
            admin_section()
        elif sel == "2":
            student_section()
        elif sel == "3":
            print("\nThank you for using ECAT Portal. Goodbye!")
            break
        else:
            print("Please select a valid option.")

if __name__ == "__main__":
    main()