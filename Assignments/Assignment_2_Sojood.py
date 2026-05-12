#Conditions Basics Assignment

math = float(input("Enter Math mark: "))
if math >= 50:
    print("Math is Pass")
else:
    print("Math is Fail")

science = float(input("Enter Science mark: "))
if science >= 50:
    print("Science is Pass")
else:
    print("Science is Fail")

history = float(input("Enter History mark: "))
if history >= 50:
    print("History is Pass")
else:
    print("History is Fail")

geography = float(input("Enter Geography mark: "))
if geography >= 50:
    print("Geography is Pass")
else:
    print("Geography is Fail")

english = float(input("Enter English mark: "))
if english >= 50:
    print("English is Pass")
else:
    print("English is Fail")

print("========================================")    

final_average = (math + science + history + geography + english) / 5
print(f"Final average percentage is {final_average}%")

if final_average >= 85:
    print("Final Grade is Excellent")

if final_average >= 75 and final_average < 85:
    print("Final Grade is Very Good")    

if final_average >= 65 and final_average < 75:
    print("Final Grade is Good")      

if final_average >= 50 and final_average < 65:
    print("Final Grade is Pass")

if final_average < 50:
    print("Final Grade is Fail")

print("========================================") 

high_average = final_average >= 85
can_join = (high_average and math >= 80) or (not high_average and math >= 90)

if can_join:
    print("The student can join the competition")
else:
    print("The student cannot join the competition")

#DONE_SOJOOD_ABUSAADA :)
