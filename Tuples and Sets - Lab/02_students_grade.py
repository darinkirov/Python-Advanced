def calculate_average(grades):
    total = sum(grades)
    return total / len(grades)

if __name__ == "__main__":
    N = int(input("Enter the number of students: "))
    student_record = {}

    for _ in range(N):
        name, *grades = input().split()
        grades = list(map(float, grades))
        if name in student_record:
            student_record[name].extend(grades)
        else:
            student_record[name] = grades

    for name, grades in student_record.items():
        average_grade = calculate_average(grades)
        formatted_grades = ' '.join(map(str, grades))
        print(f"{name} -> {formatted_grades} (avg: {average_grade:.2f})")
