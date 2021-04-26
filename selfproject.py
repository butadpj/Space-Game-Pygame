# Project A1 
# def search(patient_list, patient_name):
#     for name in range(len(patient_list)):
#         if patient_list[name] == patient_name:
#             return True
#     return False


# patient_list = ["Saw, Kyle","Scott, Evan","Simpson, Homer","Smith, John","Snyder, Zack"]
# patient_name = input("Name of Patient: ")

# if search(patient_list, patient_name):
#     print("Patient found")
#     index = patient_list.index(patient_name)
#     print("The patient is patient number", index)
# else:
#     print("Patient not found.")
#     print("Would you like to add him to the patient's log?")
#     log_answer = input(" ")
#     if log_answer =="Yes":
#         patient_list=["Saw, Kyle","Scott, Evan","Simpson, Homer","Smith, John","Snyder, Zack"]
#         print(f'Current Patient List {patient_list}')
#         new_patient = input("Please reenter patient name: ")
#         patient_list.append(new_patient)
#         patient_list.sort()
#         print(patient_list)
#         print("The patient has been added!")
#         print("Program Complete.")
        
#     elif log_answer =="No":
#         print("Ok, sure.")
#         print("Program Complete.")


# need to update the list everytime use, need new code, plausible?  --- research ---


# Project 4a
# print("Addition (A)")
# print("Subtraction (S)")
# print("Multiplication (M)")
# print("Division (D)")
# print("Exponential (E)")

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

# elif operation.upper() == "E":
#     firstnumber = input("First number: ")
#     secondnumber = input("Second number: ")
#     print(int(firstnumber) ** int(secondnumber))


# # Project A2
# temperature = input("What is the temperature today? ")

# if int(temperature) > 30:
#     print("It is a very hot day.")
#     print("Make sure to drink a lot of water.")
# elif int(temperature) > 20:
#     print("It is a nice day.")
# elif int(temperature) > 10:
#     print("It's pretty cold out there, make sure to bundle up!")
# else:
#     print("It's really cold!")

# print("Program Finished.")

import modules
import random
# modules.calculator()



# HOMEWORK FOR APR 9, 2021


# leaders = ["Mohandas Gandhi", "Nelson Mandela", "Martin Luther King Jr.","Abraham Lincoln","Emilio Aguinaldo","Napoleon Bonaparte"
# "Winston Churchill","Joseph Stalin","Alexander the Great","Julius Caesar","Genghis Khan"]
# modules.double_space_t()
# print("Please input the 3 numbers given to find out your random leaders!")
# numbers_given = modules.random_int1to10() 
# fillers = [1,2,3]

# for filler in fillers:
#     random_leaders = input("Number: ")
#     modules.space_t()
#     if int(random_leaders) == 1:
#         print("Mohandas Gandhi")
#     elif int(random_leaders) == 2:
#         print("Nelson Mandela")
#     elif int(random_leaders) == 3:
#         print("Martin Luther King Jr.")
#     elif int(random_leaders) == 4:
#         print("Abraham Lincoln")
#     elif int(random_leaders) == 5:
#         print("Emilio Aguinaldo")
#     elif int(random_leaders) == 6:
#         print("Winston Churchill")
#     elif int(random_leaders) == 7:
#         print("Joseph Stalin")
#     elif int(random_leaders) == 8:
#         print("Alexander the Great")
#     elif int(random_leaders) == 9:
#         print("Julius Caesar")
#     elif int(random_leaders) == 10:
#         print("Genghis Khan")

#     modules.space_t()
# print("Those are your randomly chosen leaders!")
# modules.space_t()
# print("Program Complete")





# index = 0

# filler = []
# for number in answers:
#     index = 0
#     for person in leaders:
        
#         if number == index:
#             print("Leader #", ":", person)
#         index += 1 




modules.choose_leaders()




