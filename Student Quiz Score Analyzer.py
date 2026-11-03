def calculate_average():
    passed = 0
    failed = 0

    total = 0
    students = int(input("Enter number of students: "))
    for i in range(1, students + 1):
        subtotal = float(input(f"Enter score for student {i}: "))
        total = total + subtotal
        average = total / students
        if subtotal >= 75:
            passed = passed + 1
        else:
            failed = failed + 1

    print("----- CLASS PERFORMANCE -----")
    print(f"Class Average: {average:.2f}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")

calculate_average()