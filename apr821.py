# print("NOTES:")

# 1. Python Code gets executed line by line

# DATA TYPES
# 1. String (text in quotation marks)
# 2. Integer (numbers)
# 3. Float (decimal numbers)

# print("This is string")
# print(type (5))
# print(type (5.7))

# method 1, type 

# VARIABLES

# text = "This is text "
# num = 4
# print(text)

# GETTING USER INPUT
# name = input("Type in your name: ")
# print("Welcome, ", name)



# PROJECT 1: A program that asks and displays user's favorite color and number

# favoritecolor = input("What is your favorite color?: ")
# favoritenumber = input("What number do you like the most?: ")
# print(favoritecolor , "is really nice!")
# print("Your favorite number is ", favoritenumber , ", that's mine too!")

# # OPERATORS
# print(1 + 2)
# print(1 - 2)
# print(1 * 2)
# print(1 / 2)

# sumnumbers = (5 + 5 * 2)
# print(sumnumbers)




# PROJECT 2: A program that asks for user's birthday and displays age

# birthyear = input("What is your birthyear?: ")
# currentyear = 2021
# print(2021-int(birthyear) , "is your age!")



# CONDITIONAL STATEMENTS

# if 1 > 5:
#     print(True)
# else:
#     print(False)

# if 1 > 5:
#     print(True)
# elif 1 == 1:
#     print("1 equals 1")



# birthmonth = input("Month: ")
# birthday = input("Day: ")
# birthyear = input("Year: ")


# if 2003 >= int(birthyear):
#     print("You are eligible to enter, welcome!")
# else:
#     print("Please enter an parental email to continue, then open the file there.")
#     email = input("Email: ")
#     print("The file will be sent to " , email, ", thanks!")



# PROJECT 4: Simple Calculator

# print("Addition (A)")
# print("Subtraction (S)")
# print("Multiplication (M)")
# print("Division (D)")
# operation = input("Select Operation To Use: ")

# if operation.upper() == "A":
#     firstnumber = input("First number: ")
#     secondnumber = input("Second number: ")
#     print(int(firstnumber) + int(secondnumber))
# elif operation.upper() == "S":
#     firstnumber = input("First number: ")
#     secondnumber = input("Second number: ")
#     print(int(firstnumber) - int(secondnumber))
# elif operation.upper() == "M":
#     firstnumber = input("First number: ")
#     secondnumber = input("Second number: ")
#     print(int(firstnumber) * int(secondnumber))
# elif operation.upper() == "D":
#     firstnumber = input("First number: ")
#     secondnumber = input("Second number: ")
#     print(int(firstnumber) / int(secondnumber))


# STRING BUILT IN METHODS

# text = "Hey there, welcome!"
    #     012 34567  89 and so on


# print(text.upper())
# print(text.lower())
# print(len(text))
# print(text.capitalize())

# print(text.index("H"))
# print(text[-1])
# print(text[0:4])
# print(text[3:])


# INTEGER METHODS

# import math

# numbertosqrt = input("Number: ")
# print(math.sqrt(int(numbertosqrt)))


# LIST OR ARRAYS - A collection of something

# name1 = "John"
# name2 = "Paul"
# name3 = "Brent"
# names = ["John","Paul","Brent"]

# print(names[1])
# print(names[0:])

# LOOPS 

# names = ["John","Paul","Brent"]
# for name in names:
#     print(name)
    
# print(names[0],names[1],names[2])

# numbers = [1,2,3,4,5,6]
# total_sum = 0

# for number in numbers:
#     total_sum = total_sum + number
#     print(total_sum)

# for number in numbers:
    # total_sum += number
# print(total_sum)


# PROJECT 5: A program that asks a user to choose somethng inside the list

# cars = ["Toyota","Ferrari","Honda","Hyundai","Kia"]
# index = 0
# print("Choose a car from the following list: ")
# for car in cars:
#     print(cars[index])
#     index += 1
# car_answer = input(" ")
# if car_answer.lower() == "toyota":
#     print("Your car of choice is Toyota!")
# elif car_answer.lower() == "ferarri":
#     print("Your car of choice is Ferrari!")
# elif car_answer.lower() == "honda":
#     print("Your car of choice is Honda!")
# elif car_answer.lower() == "hyundai":
#     print("Your car of choice is Hyundai!")
# elif car_answer.lower() == "kia":
#     print("Your car of choice is Kia!")   
# else:
#     print("You did not choose a car from the list, sorry.")

    
# for car in cars:
#     print(cars[index])
#     index += 1
# car_choice = input("Choose a car from the list. ")
# print(car_choice,"is the car you chose.")


# FUNCTIONS

# See modules and selfproject.py for more

# PROJECT 6: Create a function or method that returns True 
#             if input string is uppercase and returns False
#             if input string is not uppercase/ lowercase

# WHILE LOOP

# num = 1
# while num <= 5:
#     print("ok")
#     num += 1



# PROJECT 7: Build a guessing game

# import random
# numbers = [1,2,3,4,5,6,7,8,9,10]
# random_answer = (random.sample(range(0,9),3))
# initial_score = 0
# print(random_answer)
# i = 1
# while i <=3:
#     guessed = input("Select a number from 1-10: ")
#     if int(guessed) in random_answer:
#         print("You got it right!")
#         initial_score += 1
#         print(f"Current Score: {initial_score}")
#     else:
#         print("That's not given, try something else.")
#         print(f"Current Score: {initial_score}")
#     i += 1

# CLASSES
# class Random():
#     number = 21
# class Calcu():
#     first = int(input("first number: "))
#     second = int(input("second number: "))

#     def calculate(self):
#         answer = self.first + self.second + Random().number
#         if answer < 30:
#             return True
# name = Calcu()

# print(Calcu().calculate())









