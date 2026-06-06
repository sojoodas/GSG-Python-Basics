# Training Center Performance System

def calculate_final_grade(attendance, homework, quiz, participation):
    final_grade = (attendance * 0.20) + (homework * 0.35) + (quiz * 0.35) + (participation * 0.10)
    return final_grade

def get_student_status(final_grade, attendance):
    if attendance < 50:
        return "Failed because of low attendance"
    elif final_grade >= 85:
        return "Excellent"
    elif final_grade >= 70:
        return "Good"
    elif final_grade >= 50:
        return "Needs Improvement"
    else:
        return "Failed"

def get_student_advice(attendance, homework, quiz, participation):
    if attendance < 50:
        return "You need to attend more sessions."
    elif homework < 50:
        return "You need to focus more on homework."
    elif quiz < 50:
        return "You need to study more for quizzes."
    elif participation < 50:
        return "Try to participate more during sessions."
    else:
        return "Keep up the good work."

def print_student_report(name, final_grade, status, advice):
    print(50 * "-")
    print("Student Report")
    print(f"Name: {name}")
    print(f"Final Grade: {final_grade}")
    print(f"Status: {status}")
    print(f"Advice: {advice}")
    print(50 * "-")

def get_valid_score(message):
    while True:
        score = int(input(message))

        if score >= 0 and score <= 100:
            break
        else:
            print("Invalid score. Please enter a number between 0 and 100.")

    return score

def get_valid_students_number():
    while True:
        students_number = int(input("How many students do you want to evaluate? "))

        if students_number > 0:
            break
        else:
            print("Invalid number. Please enter a number greater than 0.")

    return students_number


students_number = get_valid_students_number()

excellent_students = 0
good_students = 0
students_needs_improvement = 0
failed_students = 0

total_grades = 0
highest_grade = 0
lowest_grade = 0

for student_number in range(1, students_number + 1):
    print()
    print(f"Student {student_number}")

    name = input("Enter student name: ")
    attendance = get_valid_score("Enter attendance score: ")
    homework = get_valid_score("Enter homework score: ")
    quiz = get_valid_score("Enter quiz score: ")
    participation = get_valid_score("Enter participation score: ")

    final_grade = calculate_final_grade(attendance, homework, quiz, participation)
    status = get_student_status(final_grade, attendance)
    advice = get_student_advice(attendance, homework, quiz, participation)

    print()
    print_student_report(name, final_grade, status, advice)

    total_grades += final_grade

    if student_number == 1:
        highest_grade = final_grade
        lowest_grade = final_grade
    else:
        if final_grade > highest_grade:
            highest_grade = final_grade

        if final_grade < lowest_grade:
            lowest_grade = final_grade

    if status == "Excellent":
        excellent_students += 1
    elif status == "Good":
        good_students += 1
    elif status == "Needs Improvement":
        students_needs_improvement += 1
    else:
        failed_students += 1

class_average = total_grades / students_number

print(50 * "=")
print("Final Group Summary")
print(f"Total students: {students_number}")
print(f"Excellent students: {excellent_students}")
print(f"Good students: {good_students}")
print(f"Needs improvement: {students_needs_improvement}")
print(f"Failed students: {failed_students}")
print(f"Class average: {class_average}")
print(f"Highest grade: {highest_grade}")
print(f"Lowest grade: {lowest_grade}")
print(50 * "=")

# DONE_SOJOOD_ABUSAADA :)