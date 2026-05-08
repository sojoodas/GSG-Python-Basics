#Question1 ــ Beginner Level
coffee_price = 25
cake_price = 40
water_price = 10

coffee_count = 2
cake_count = 1
water_count = 3

total_bill = (coffee_price * coffee_count) + (cake_price * cake_count) + (water_price * water_count)

print(total_bill)
print(total_bill > 100)
print(total_bill == 120)

#Bonus
coffee_price += 5
print(coffee_price)

#Question 2 ــ Intermediate Level
points = 40

points += 20
points -= 10
points *= 2

print(points)
is_VIP = points >= 100
print(is_VIP)

total_bill = 170

free_delivery = (total_bill > 150) or is_VIP
print(free_delivery)

#Question 3 ــ Advanced Level
#Part A ــ Math Priority
result = 10 + 5 * 2
print(result)
#Prediction: 20
#Reason: because we prioritize multiplication before addition

result = (10 + 5) * 2
print(result)
#Prediction: 30
#Reason: because parentheses are evaluated first

#Part B ــ Logical Priority
print(True or False and False)
#Prediction: True
#Reason: and before or, so False and False = False, then True or False = True

print((True or False) and False)
#Prediction: False
#Reason: parentheses happen first, so True or False = True, then True and False = False

#Part C ــ Real Life Trap
total_bill = 120
points = 20
premium_member = True

print(total_bill > 150 and points > 50 or premium_member)
#Prediction: True
#Reason: total_bill > 150 = False and points > 50 = False too
#False and False = False
#False or True = True

print(total_bill > 150 and (points > 50 or premium_member))
#Prediction: False
#Reason: parentheses happen first, so points > 50 = False or premium_member = True
#False or True = True
#total_bill > 150 is False
#False and True = False

#DONE_SOJOOD_ABUSAADA :)