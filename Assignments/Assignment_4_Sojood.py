# Python loops Assignment

# Question 1: Multiplication Table

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

    
# Question 2: Count Even Numbers

counter = 0

for number in range(1, 31):
    if number % 2 == 0:
        print(number)
        counter += 1

print(f"\nTotal even numbers: {counter}")


# Question 3: Password Attempts

correct_password = "python123"

attempts = 0

is_wrong_password = True

while attempts < 3 and is_wrong_password:
    password = input("Enter password: ")

    if password == correct_password:
        print("Access granted")
        is_wrong_password = False
    else:
        attempts += 1

if attempts == 3 and is_wrong_password:
    print("Account locked")


# Question 4: Calculate Average Marks

marks_count = int(input("How many marks do you want to enter? "))
print()

total = 0

for i in range(1, marks_count + 1):
    mark = int(input(f"Enter mark {i}: "))
    total += mark

average = total / marks_count
print(f"\nAverage: {average}")


# Question 5: Number Guessing Game

secret_number = 7

guess_number = 0

while guess_number != secret_number:
    guess_number = int(input("\nGuess the number: "))

    if guess_number > secret_number:
        print("Too high")
    elif guess_number < secret_number:
        print("Too low")
    else:
        print("Correct!")


# Question 6: Simple ATM Menu

balance = 1000

continue_menu = True

while continue_menu:
    print("1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")

    choice = int(input("Choose a number from the menu: "))

    if choice == 1:
        print(f"Current balance: {balance}")

    elif choice == 2:
        deposit_amount = int(input("Enter amount to deposit: "))
        balance += deposit_amount
        print(f"New balance: {balance}")

    elif choice == 3:
        withdraw_amount = int(input("Enter amount to withdraw: "))

        if withdraw_amount > balance:
            print("Insufficient balance")
        else:
            balance -= withdraw_amount
            print(f"New balance: {balance}")

    elif choice == 4:
        print("Thank you!")
        continue_menu = False

    else:
        print("Invalid choice")


# Bonus 1: Shopping Cart System

total = 0
count = 0
maximum = 0
minimum = 0

is_shopping = True

while is_shopping:
    item_price = int(input("Enter item price or 0 to finish: "))

    if item_price == 0:
        is_shopping = False
    else:
        total += item_price
        count += 1

        if count == 1:
            maximum = item_price
            minimum = item_price
        else:
            if item_price > maximum:
                maximum = item_price

            if item_price < minimum:
                minimum = item_price

if count == 0:
    print("No items were added.")
else:
    average = total / count

    print(f"Number of items: {count}")
    print(f"Total price: {total}")
    print(f"Average item price: {average}")
    print(f"Most expensive item: {maximum}")
    print(f"Cheapest item: {minimum}")


# Bonus 2: Simple Student Grading System

students_count = int(input("How many students do you want to enter? "))
print()

passed_students = 0
failed_students = 0
highest_average = 0
top_student = ""

for student_number in range(1, students_count + 1):

    if student_number > 1:
        print()

    student_name = input("Enter student name: ")
    marks_count = int(input(f"How many marks for {student_name}? "))

    total = 0

    for mark_number in range(1, marks_count + 1):
        mark = int(input(f"Enter mark {mark_number}: "))
        total += mark

    average = total / marks_count

    print(f"\n{student_name}'s average is: {average}")

    if average >= 50:
        print("Result: Passed")
        passed_students += 1
    else:
        print("Result: Failed")
        failed_students += 1

    if student_number == 1 or average > highest_average:
        highest_average = average
        top_student = student_name

print("\nSummary:")
print(f"Total students: {students_count}")
print(f"Passed students: {passed_students}")
print(f"Failed students: {failed_students}")
print(f"Highest average: {highest_average}")
print(f"Top student: {top_student}")

# DONE_SOJOOD_ABUSAADA :)