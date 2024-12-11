def get_student_data():
    student_grade = {}
    while True:
        name = input("Enter sudent name(or type 'done' to finish):").strip()
        if name.lower()=='done':
            break
        try:
            grade = float(input(f'Enter grade for {name}:'))
            student_grade[name] = grade
        except  ValueError:
            print("Invalidd grade. Please enter a number.")
    return student_grade

def calculate_statistics(student_grade):
    if not student_grade:
        return None
    
    average_grade = sum(student_grade.values()) / len(student_grade)
    highest_student = max(student_grade, key=student_grade.get)
    lowest_student = min(student_grade, key=student_grade.get)
    return{
        'average': average_grade,
        'highest': (highest_student, student_grade[highest_student]),
        'lowest' : (lowest_student, student_grade[lowest_student])
    }

def display_result(student_grade, statistics):
    if not student_grade:
        print("No student data to display")
        return
    
    print("\n --- Student Grades ---")
    for student, grade in student_grade.items():
        print(f"{student}: {grade}")

    print("\n--- Statistics ---")
    print(f"Average grade: {statistics['average']: .2f}")
    print(f"Highest grade: {statistics['highest'][0]}({statistics['highest'][1]})")
    print(f"Lowest grade: {statistics['lowest'][0]}({statistics['lowest'][1]})")


if __name__ == "__main__":
    student_grade = get_student_data()
    statistic = calculate_statistics(student_grade)
    display_result(student_grade, statistic)