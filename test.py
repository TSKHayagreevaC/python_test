# Print The String
# print("day-1\nPython Function")

# String Concatination
# print("Hello "+"Srikanth")

# Decleration of Variable and Printing The same
# msg = "Hi! to every one"
# print(msg)

# Taking Input And Printing The Same
# print("Hello "+input("What Is Your Name ?"))

# Code To Caliculate The Number Of Characters In A String
# print(len(input("Enter Your Name Here: ")))

# Python Variables Practice
# name = input("what is your name: ")
# print(name)
# print(len(name))

# name = "Srikanth"
# print(name)
# length = len(name)

# Coding Chalenge Interchange The Variables
# a = input("a: ")
# b = input("b: ")
# c = a
# a = b
# b = c
# print(a)
# print(b)

# Small Program With Display The Code Name Of User
# print("Welcome To The Small Display Project")
# city = input("Enter The City Did You Grow Up In Here:\n")
# name = input("Enter Your Name Here:\n")
# print("Your Code Name Can Be: "+ city + name)

#  Primary Data Operators
# # String
# print("Hello"[4])
# print("123"[2] + "456"[2])

# Integer
# print(123 + 345)
# print(123,123,123 + 123,123,123)

# Float
# print(3.1419)

# Boolean
# print(True)
# print(False)

# # Conversion Of Data Types
# your_name = input("Enter Your Name Here:\n")
# num_char = len(your_name)
# new_num_char = str(num_char)
# print("Hi, " + your_name + " Your Name Has '" + new_num_char + "' Characters.")

# a = str(123)
# print(type(a))
# b = float(123)
# print(type(b))
# print(100 + float("100.5"))
# print(str(100) + str(200))

# # A Simple Calculator
# two_digit_number = input("Enter A Two Digit Number Here: ")
# first_digit = two_digit_number[0]
# second_digit = two_digit_number[1]
# sum = int(first_digit) + int(second_digit)
# # print(sum)
# sub = int(first_digit) - int(second_digit)
# print(sub)
# mul = int(first_digit) * int(second_digit)
# print(mul)
# div = int(first_digit) / int(second_digit)
# print(div)
# square = int(first_digit) ** int(second_digit)
# print(square)

# PEMDAS => () , ** , * , / , + , - .
# print( 3 * 3 + 3 / 3 - 3)

# BMI CALICULATOR CODE
# weight = int(input("Please Enter Your Weight In Kilo Grams:\n"))
# height = float(input("Please Enter Your Height In Meters:\n"))
# bmi =  weight / ((height)**2)
# bmi_int = int(bmi)
# print(bmi_int)

# Number Manipulation
# print(round(8/3, 2))
# print(type(8 // 3))
# result = 4/2
# result /= 2
# print(result)

# F-String
# score = 0
# height = 1.8
# isWinning = True
# print(f"Your Score Is : {score}, Your Height Is : {height}, Your Winning Is : {isWinning}")

# Program TO Look Life In Detail
# age = input("Enter Your Current Age Here:\n")

# age_int = int(age)

# rem_age = 120 - age_int
# days = age_int * 365
# weeks = rem_age * 52
# months = age_int * 12

# days_str = str(days)
# weeks_str = str(weeks)
# months_str = str(months)
# rem_age_str = str(rem_age)
# print("You Have '"+days_str+"' Days, '"+weeks_str+"' Weeks, '"+months_str+"' Months And '"+rem_age_str+"' Years.")

# message = (f"You Have {days} Days, {weeks} Weeks, {months} Months And {rem_age}.")
# print(message)

# Caliculator Program
# print("*** Welcome To Caliculator ***")
# bill = input("Enter The Total Bill :\n")
# bill_int = float(bill)
# tip_per = input("Enter The Percentage Tip :\n")
# tip_int = int(tip_per)
# total_bill = bill_int * (1 + (tip_int/100))
# people = input ("Enter The Number Of People To Split The Bill :\n")
# people_int = int(people)
# per_pay = total_bill / people_int
# per_pay_round = round(per_pay, 2)
# per_pay_round = "{:.2f}".format(per_pay)
# print(f"Amount Per Person is : '{per_pay_round}' Rupees.")

# Roller Coster Projedt
# print("***Welcome To Roller Coster Project***")
# height = int(input("Enter Your Height In Centi Meters:\n"))

# if height >= 120:
#     print("Roller Coster")
# else:
#     print("Sorry, Height Is Not Enough.")

# Odd Or Even Finder
# num = int(input("Enter The Number Here:\n"))
# com = num % 2
# if com == 0:
#     print("This Number Is Even Number.")
# else:
#     print("This Number Is Odd Number")

# Nested If & elif Condition
# print("***Welcome To Roller Coster Project***")
# height = int(input("Enter Your Height In Centi Meters:\n"))

# if height >= 120:
#     print("Roller Coster")
#     age = int(input("Enter Your Age:\n"))
#     if age <= 12:
#         print("You Need To Pay 10 Rupees.")
#     elif age <= 18:
#         print("You Need To Pay 20 Rupees.")
#     else:
#         print("You Need To Pay 30 Rupees")
# else:
#     print("Sorry, Height Is Not Enough.")

# Body Mass Calculator 2.0
# weight = int(input("Please Enter Your Weight In Kilo Grams:\n"))
# height = float(input("Please Enter Your Height In Meters:\n"))
# bmi =  round(weight / ((height)**2))
# if bmi < 18.5:
#     print(f"Your BMI is '{bmi}', Hence You Are 'UNDERWEIGHT'.")
# elif bmi < 25:
#     print(f"Your BMI is '{bmi}', Hence You Are 'NORMALWEIGHT'.")
# elif bmi < 30:
#     print(f"Your Weight is '{bmi}', Hence You Are 'OVERWEIGHT'")
# elif bmi <35:
#     print(f"Your BMI is '{bmi}', Hence You Are 'OBESE'.")
# else:
#     print(f"Your BMI is '{bmi}', Hence You Are 'CLINICALLY OBESE'.")

# Code To Caliculate Leap Year
# year = int(input("Enter Year Here:\n"))

# year_4 = year % 4
# year_100 = year % 100
# year_400 = year % 400

# if year_4 == 0:
#     if year_100 != 0:
#         print(f"Year '{year}' Is LEAP YEAR")
#     else:
#         if year_400 == 0 :
#             print(f"Year '{year}' Is LEAP YEAR")
# else:
#     print(f"Year '{year}' Is Not LEAP YEAR.")
            
# Multiple if Conditions // Roler Coast Program
# print("***Welcome To Roller Coster Project***")
# height = int(input("Enter Your Height In Centi Meters:\n"))
# bill = 0

# if height >= 120:
#     print("Welcome To Roller Coster")
#     age = int(input("Enter Your Age:\n"))
#     if age <= 12:
#         bill = 10
#         print("CHILD TICKET: You Need To Pay 10 Rupees Only.")
#     elif age <= 18:
#         bill = 20
#         print("YOUTH TICKET: You Need To Pay 20 Rupees Only.")
#     else:
#         bill = 30
#         print("ADULT TICKET: You Need To Pay 30 Rupees Only.")
    
#     photo = input("Do You Want To Have Photo Of Your Ride? Type Y (for yes) or N (for no):\n")
#     if photo == "Y":
#         bill += 5
#     print(f"Your Final Bill Is {bill} Rupees Only.")

# else:
#     print("Sorry, Height Is Not Enough To Ride Roller Coster.")

# PIZZA ORDER PROJECT

# print("*** Welcome To Samosa Deliveries ***")
# size = input("Enter Size Of Samosa You Want : S(for small), M(for medium), L(for large) :\n")
# add_aalu = input("Do You Want AALU : Y(for yes) and N(for no) :\n")
# add_onion = input("Do You Want ONION : Y(for yes) and N(for no) :\n")

# bill = 0

# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25

# if add_aalu == "Y":
#     if size == "S":
#         bill += 3
#     elif size == "M":
#         bill += 3
#     else:
#         bill += 5

# if add_onion == "Y":
#     if size == "S":
#         bill += 2
#     elif size == "M":
#         bill += 4
#     else:
#         bill += 6

# print(f"Your Final Bill Is {bill} Rupees.")

# LOGICAL OPERATORS
# print("***Welcome To Roller Coster Project***")
# height = int(input("Enter Your Height In Centi Meters:\n"))
# bill = 0

# if height >= 120:
#     print("Welcome To Roller Coster")
#     age = int(input("Enter Your Age:\n"))
#     if age <= 12:
#         bill = 10
#         print("CHILD TICKET: You Need To Pay 10 Rupees Only.")
#     elif age <= 18:
#         bill = 20
#         print("YOUTH TICKET: You Need To Pay 20 Rupees Only.")
#     elif age >= 45 and age <= 55:
#         print("Every Thing Is Ok, You Have A Free Entry.")
#     else:
#         bill = 30
#         print("ADULT TICKET: You Need To Pay 30 Rupees Only.")
    
#     photo = input("Do You Want To Have Photo Of Your Ride? Type Y (for yes) or N (for no):\n")
#     if photo == "Y":
#         bill += 5
#     print(f"Your Final Bill Is {bill} Rupees Only.")

# A LOVE CALCULATOR
# print("***WELCOME TO THE LOVE CALCULATOR***")
# name1 = input("First Name :\n")
# name2 = input("Second Name :\n")

# combined_name = name1 + name1
# lower_case_name = combined_name.lower()

# t = lower_case_name.count("t")
# r = lower_case_name.count("r")
# u = lower_case_name.count("u")
# e = lower_case_name.count("e")

# true = t + r + u + e

# l = lower_case_name.count("l")
# o = lower_case_name.count("o")
# v = lower_case_name.count("v")
# e = lower_case_name.count("e")

# love = l + o + v + e

# love_score = int(str(true) + str(love))

# if (love_score < 10) or (love_score > 90):
#     print(f"Your Love Score Is '{love_score}' => You Go To Gether Like Salt And Fire.")
# elif (love_score >= 40) and (love_score <= 50):
#     print(f"Your Love Score Is '{love_score} => You Are Alright Together. '")
# else:
#     print(f"Your Score Is '{love_score}'")

# TREASURE ISLAND
# print("WELCOME TO TREASURE ISLAND")
# print(''' 
#  _                                     _     _                 _ 
# | |                                   (_)   | |               | |
# | |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
# | __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
# | |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
#  \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|''')

# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/______/_
# *******************************************************************************''')

# print("WELCOME TO TREASURE ISLAND")
# print("Your Mission Is To Find The Treasure...")
# choice1 = input("You Are At A Cross Road, Where Do You Want To Go? Type 'left' or 'right' :\n").lower()

# if choice1 == "left":
#     choice2 = input("You Have Come TO A Lake, There Is A Island In The Middle Of The Lake. Type 'Wait' To Wait for A Boat, Type 'Swim' To Swim Aross :\n").lower()
#     if choice2 == "wait":
#         choice3 = input("You Have Arrived At The Island Unarmed. There Is A House With 3 Doors. One Red, One Yellow and One Blue. Choose One Colour:\n").lower()
#         if choice3 == "red":
#             print("It Is A Room Full Of Fire...Game Over...")
#         elif choice3 == "yellow":
#             print("You Found The Tressure => You Won The Game...")
#         elif choice3 == "blue":
#             print("You Entered The Empty Room...Game Over...")
#         else:
#             print("You Choose A Door Which Does Not Exist...Game Over...")
#     else:
#         print("You Got Attacked By An Angry Trout.")
# else:
#     print("You Fell Into A Hole, Game Over.")
