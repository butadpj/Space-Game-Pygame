

# def greeting():
#     print("Welcome, Traveler!")

# def calculator():
#     print("Addition (A)")
#     print("Subtraction (S)")
#     print("Multiplication (M)")
#     print("Division (D)")
#     print("Exponential (E)")

#     operation = input("Select Operation To Use: ")

#     if operation.upper() == "A":
#         firstnumber = input("First number: ")
#         secondnumber = input("Second number: ")
#         print(int(firstnumber) + int(secondnumber))

#     elif operation.upper() == "S":
#         firstnumber = input("First number: ")
#         secondnumber = input("Second number: ")
#         print(int(firstnumber) - int(secondnumber))

#     elif operation.upper() == "M":
#         firstnumber = input("First number: ")
#         secondnumber = input("Second number: ")
#         print(int(firstnumber) * int(secondnumber))

#     elif operation.upper() == "D":
#         firstnumber = input("First number: ")
#         secondnumber = input("Second number: ")
#         print(int(firstnumber) / int(secondnumber))

#     elif operation.upper() == "E":
#         firstnumber = input("First number: ")
#         secondnumber = input("Second number: ")
#         print(int(firstnumber) ** int(secondnumber))


# def uppercase_checker(input_string):
#     if input_string == input_string.upper():
#         return True 
#     return False

# answer = input("")
# print(uppercase_checker(answer))


def random_int1to10():
    import random
    for numbers in range(3):
        value = random.randint(1,10)
        print(value)


def space_t():
    print("  ")

def double_space_t():
    print(" ")
    print(" ")

def choose_leaders():
    import random
    leaders = ["Mohandas Gandhi", "Nelson Mandela", "Martin Luther King Jr.","Abraham Lincoln","Emilio Aguinaldo","Napoleon Bonaparte", "Winston Churchill","Joseph Stalin","Alexander the Great","Julius Caesar","Genghis Khan"]
    answers = (random.sample(range(0,9),3))
    filler = []
    for number in answers:
        index = 0
        for person in leaders:
            if number == index:
                filler.append(person)
                filler.sort()
            index += 1 

    for chosen in filler:
        print(f"Leader #{filler.index(chosen)+1}: {chosen}")