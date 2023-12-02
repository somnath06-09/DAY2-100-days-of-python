# print('hello'[4])
# print(3*(3+3)/3-3)
# **
# *
# /
# +
# -
# print(round(8/3,2))
# print(8//3)
# print(type(8//3))

# score=0
# score += 1
# print(score)

'''score=0
height=1.8
iswinning=True
#f-string
print(f"your score is {score},your height is {height},you are winning  {iswinning}")'''
# print(6+4/2-(1*2))


#tip calculator
print("Welcome to the tip calculator")
bill=float(input("What was the total bill? $"))
tip=int(input("What percentage tip would you like to give? 10,12 or 15? "))
split=int(input("How many people to split the bill?  "))
tip_as_percent=tip/100
total_tip_amount=bill*tip_as_percent
total_bill=bill+total_tip_amount
bill_per_person=total_bill/split
final_amount=round(bill_per_person, 2)
final_amount='{:.2f}'.format(bill_per_person)
print(f'each person should pay: ${final_amount}')
