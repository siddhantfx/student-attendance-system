from storage import load_s, save, load_a, asave


def add():
    r = input("Enter roll no.: ")
    n = input("Enter name: ")
    c = input("Enter class: ")
    save(r, n, c)
    print("Saved!")


def sview():
    s = load_s()
    if len(s) == 0:
        print("No student added till now.")
        return
    print("All students are:")
    for i in s:
        print(i[0], "-", i[1], "-", i[2])
    print()


def mark():
    s = load_s()
    if len(s) == 0:
        print("No students added yet.")
        return
    date = input("Enter date (DD-MM-YYYY): ")
    for i in s:
        status = input("Mark attendance for " + str(i[1]) + " (" + str(i[0]) + ") - Present/Absent: ")
        asave(i[0], date, status)
    print("Attendance marked")


def aview():
    att = load_a()
    r = input("Enter roll no.: ")
    found = False
    for i in att:
        if str(i[0]) == str(r):
            print(i[1], "-", i[2])
            found = True
    if not found:
        print("No record found")
    print()


def genr():
    s = load_s()
    att = load_a()
    for stu in s:
        r = stu[0]
        total = 0
        present = 0
        for a in att:
            if str(a[0]) == str(r):
                total += 1
                if a[2] == "Present":
                    present += 1
        if total > 0:
            per = (present / total) * 100
        else:
            per = 0
        print(stu[1], "of roll", r, "have attendance =", round(per, 2), "%")
        if per < 75:
            print(stu[1], "have attendance below 75%")
    print()


def menu():
    while True:
        print("Student Attendance Management System")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. View All Students")
        print("4. View Attendance (by student)")
        print("5. Generate Report")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add()
        elif choice == "2":
            mark()
        elif choice == "3":
            sview()
        elif choice == "4":
            aview()
        elif choice == "5":
            genr()
        elif choice == "6":
            print("Data saved.")
            break
        else:
            print("Invalid choice, try again.")


menu()
