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

# Mersenne Twister
# import random
# import my_module

# random_integer = random.randint(1, 10)
# print(random_integer)

# random_float = random.random() * 5
# print(random_float)

# random_love_score = random.randint(1, 100)
# print(f"Your Love Score Is {random_love_score}")

# print(my_module.pi)


# Heads And Tails Program

# import random

# random_side = random.randint(0, 1)
# if random_side == 1:
#     print(f"HEADS")
# else:
#     print(f"TAILS")

# TO DO LIST USING PYTHON

# states_of_India = ["UtterPradesh", "MadhyaPradesh", "Rjasthan", "WestBengal", "TamilNadu"]
# print(states_of_India[4])
# print(states_of_India[-2])
# states_of_India[4] = "AndhraPradesh"
# states_of_India.append("Karnataka")
# print(states_of_India)

# Banker Roulette Who Will Pay The Bill
# import random

# names_string = input("Give Every Body's Name, Seperated BY A Comma : \n")
# names = names_string.split(", ")
# num_items = len(names)

# print(num_items)
# print(names)
# random_choice = random.randint(0, num_items - 1)
# person_to_pay_bill = names[random_choice]
# print(f"Person Who Will Pay The Bill Is:'{person_to_pay_bill}'.")

# Index Errors With Nested Lists

# dozen_fruits = ["mango", "apple", "banana", "orange", "apricot", "kiwi", "grapes", "kashew", "jackfruit", "watermilon", "muskmilon", "jamoon"]
# dozen_vegetables = ["spinach", "tomatoes", "potato", "onion", "brinjal", "curryleaves"]
# fruits_and_vegetables = [dozen_fruits, dozen_vegetables]
# print(fruits_and_vegetables)

# TREASURE MAP --- CODING CHALLENGE

# row1 = ["😀", "😀", "😀"]
# row2 = ["😀", "😀", "😀"]
# row3 = ["😀", "😀", "😀"]

# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where Do You Want To Put The Treasure?\n")

# horizonatl = int(position[0])
# vertical = int(position[1])

# map[vertical - 1][horizonatl - 1] = "X"

# print(f"{row1}\n{row2}\n{row3}")

# Rock Papers Scissors Game
# import random

# rock = '''
#     _________
# ---'   ______)
#       (_______)
#       (_______)
#       (______)
# ---.__(_____)
# '''
# paper = '''
#     _______
# ---'    ____)_________
#            ___________)_
#           ______________)
#          ______________)
# ---._______________)
# '''
# scissors = '''
#     _______
# ---'   ____)________
#           __________)__
#        ________________)
#      ______)
# ---.__(____)
# '''

# game_images = [rock, paper, scissors]

# user_choice = int(input("What Do You Choose ? Type 0 For Rock, 1 For Paper or 2 For Scissor:\n"))
# if user_choice >= 3 or user_choice < 0:
#     print("You Typed An Invalid Number, You Lose!")
# else:
#     print(game_images[user_choice])

#     computer_choice = random.randint(0, 2)
#     print("computer Choose:\n")
#     print(game_images[computer_choice])

#     if user_choice == 0 and computer_choice == 2:
#         print("You Won!")
#     elif computer_choice == 0 and user_choice == 0:
#         print("You Lose!")
#     elif computer_choice > user_choice:
#         print("You Lose!")
#     elif computer_choice < user_choice:
#         print("You Won!")
#     elif computer_choice == user_choice:
#         print("It Is A Draw!")

# Loops // for loop
# papers = ["TheHindu", "TimesNow", "DeccanChronical", "Tribune", "NewYorkExpress" , "IndianExpress"]
# for paper in papers:
#     print("Every Day Read News Paper: "+paper)
# print(papers)

# Code To Caliculate The Aerage Height Of A List Of Students

# student_heights = input("Enter A List Of Students Heights:\n").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])

# total_height = 0
# for height in student_heights:
#     total_height += height

# number_of_students = 0
# for student in student_heights:
#     number_of_students += 1

# average_height = total_height / number_of_students
# print(f"Average Height Of Students Is : {average_height}")

# Highest Score Exercise

# student_scores = input("Enter The List Of Student Scores:\n").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)

# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
# print(f"The Highest Score In The Class Is : {highest_score}")

# for loops with range function

# for number in range(1, 11):
#     print(number)

# total = 0
# for number in range(1, 101):
#     total += number
# print(total)

# Program To Add Even Numbers

# total = 0
# for number in range(2, 101, 2):
#     total += number
# print(f"Total Of The Numbers Is : {total}")

# total2 = 0
# for number in range(1, 101):
#     if number % 2 == 0:
#         total2 += number

# print(total2)

# fizz buzz // job interview question

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0 :
#         print("Fizz Buzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

# # Create A PassWord Generator

# import random

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!','#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome To My PassWord Generator")
# nr_letters = int(input("How Many Letters You Want In Your PassWord ?\n"))
# nr_numbers = int(input("How Many Numbers You Want In Your PassWord ?\n"))
# nr_symbols = int(input("How Many Symbols You Want In Your PassWord ?\n"))

# # Type One PassWord Generator
# PassWord = ""

# for char in range(1, nr_letters + 1):
#     PassWord += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#     PassWord += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#     PassWord += random.choice(numbers)

# print(f"Type One Password is : {PassWord}")

# # Type Two Password Generator

# PassWord_list = []

# for char in range(1, nr_letters + 1):
#     PassWord_list += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#     PassWord_list += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#     PassWord_list += random.choice(numbers)

# print(f"Type Two Password is : {PassWord_list}")
# random.shuffle(PassWord_list)
# print(PassWord_list)

# PassWord = ""
# for char in PassWord_list:
#     PassWord += char

# print(f"Your Final Password Is : {PassWord}")

# Python Functions

# print("Hello!")
# num_char = len("Hello!")
# print(num_char)

# def my_function():
#     print("Hello")
#     print("Welcome To My Function")
#     print("Bye")

# my_function()

# While Loop

# number_of_hurdles = 6
# while number_of_hurdles > 0:
#     number_of_hurdles -= 1
#     print(f"Number Of Hurdles Are: {number_of_hurdles}")

# number_of_ways = 3
# while not number_of_ways == 3:
#     number_of_ways += 1
#     print("Hi, Number Of Ways Is Three...")

# for and while loops combination
# test_value = 3
# test_integers = [1, 2]
# while test_value > 0:
#     test_value -= 1
#     print("While Loop Executed...")
#     for test_integer in test_integers :
#         test_integer -= 1
#         print("For Loop executed...")

# HANGMAN Game

# import random
# import hangman_art
# import hangman_words

# print(hangman_art.logo)

# print(f"Welcome To HANGMAN GAME You Have SIX Lives Try And Complete The Game...")

# choosen_word = random.choice(hangman_words.word_list)
# print(f"The Solution Is : {choosen_word}")

# display = []
# word_length = len(choosen_word)
# for _ in range(word_length):
#     display += "_"
# print(display)

# lives = 5
# end_of_game = False

# while not end_of_game:
#     guess = input("Guess A Letter:\n").lower()

#     for position in range(word_length):
#         letter = choosen_word[position]
#         # print(f"Current Position: {position} \n Curent Letter: {letter} \n Guessed Letter: {guess}")
#         if letter == guess:
#             display[position] = letter
#         # else:
#         #     print("Not Match...Try Again")

#     if guess in display:
#         print(input(f"You Already Guessed This Letter: {guess}"))

#     if guess not in choosen_word:
#         print(f"You Guessed {guess}, That's Not In The Word. You Lost A Life... ")
#         lives -= 1
#         if lives == 0:
#             end_of_game = True
#             print("You Lost The Game...")

#     print(f"{' '.join(display)}")

#     if "_" not in display:
#         end_of_game = True
#         print("You Won The Game...")

#     print(hangman_art.stages[lives])

# Functions And Paramater

# def greet():
#     print("Hello!")
#     print("How Are You...")
#     print("How Is To Day...")
# greet()

# def greet_name(name):
#     print(f"Hello {name}, Welcome To You...")
# greet_name("srikanth")

# def greet_name_location(name, location):
#     print(f"Hello {name}, You Are From {location}.")
# greet_name_location("srikanth","hyderabad")
# greet_name_location(name="srikanth",location="hyderabad")
# greet_name_location(location="secunderabad", name="hayagreeva")

# Area Calculation

# import math

# def paint_calculator(height, width, cover):
#     area = height * width
#     num_cans= math.ceil(area / cover)
#     print(f"Number Of Cans Required Is : {num_cans}")

# test_h = int(input("Enter Height Of Wall:\n"))
# test_w = int(input("Enter Width Of Wall: \n"))
# coverage = 5
# paint_calculator(height = test_h, width= test_w, cover= coverage)

# Prime Number Checker

# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print("Number Entered Is A Prime Number")
#     else:
#         print("Number Entered Is Not A Prime Number.")

# n = int(input("Enter The Number To Be Checked:\n"))
# prime_checker(number=n)

# Ceaser Cipher Project

# import cypher_art

# print(cypher_art.logo)
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def caesar(start_text, shift_amount, cipher_direction):
#     end_text = ""
#     if cipher_direction == "decode":
#         shift_amount *= -1
#     for char in start_text:
#         if char in alphabet:
#             position = alphabet.index(char)
#             new_position = position + shift_amount
#             end_text += alphabet[new_position]
#         else:
#             end_text += char
#     print(f"{cipher_direction}ed Message is: '{end_text}'")

# should_continue = True
# while should_continue:
#     direction = input("Enter preference Either Encode Or Decode:\n")
#     text = input("Enter Your Message:\n").lower()
#     shift = int(input("Enter The Shift Number:\n"))

#     shift = shift % 26
#     caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

#     result = input("Type 'yes' If You Wanr To Go Again, Otherwise Type 'no':\n")
#     if result == "no":
#         should_continue = False
#         print("Good Bye...")

# Lengthy And Extra Code For Ceaser Cipher Program...

# def encrypt(plain_text, shift_amount):
#     cypher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cypher_text += new_letter
#     print(f"Encoded Message is :{cypher_text}")

# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         plain_text += alphabet[new_position]
#     print(f"Decoded Message is: {plain_text}")

# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(cipher_text=text, shift_amount=shift)