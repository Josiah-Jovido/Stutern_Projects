"""
Name: Josiah Oborekanhwo
Email: josiahjovido@gmail.com
Date: 03-11-2020
Purpose: To Intelligently display information
"""


# Python 3.8 interpreter was used for writing this script
# Creating a function which acts as a container for containing the lines of code to perform task
def greet_user():
    Name = input("What is your name?")  # To get the User name
    Age = input("How old are you?")  # To get the user age
    Gender = (input("Are you a male? (True/False)"))  # To get the User gender

    # To generate the conditions for calling out the Gender parameter
    if 'T' in Gender:
        print(f"Hello, Mr. {Name}, you are {Age} years old.")
    else:
        print(f"Hello, Mrs. {Name}, you are {Age} years old.")

    age = int(Age)
    DOB = 2020 - age  # To get the user date of birth
    print(f"You were born in the year {DOB}.")

    # To Generate the conditions for age grouping
    the_age = float(Age)
    if the_age < 1:
        print(f"As you are {Age} years old, you are an infant.")
    elif the_age <= 17:
        print(f"As you are {Age} years old, you are a child.")
    elif the_age >= 65:
        print(f"As you are {Age} years old, you are an elderly person.")
    elif the_age >= 18:
        print(f"As you are {Age} years old, you are an adult.")
    else:
        print("Incorrrect input.")

    # To calculate the user age a decade ago
    decade = age - 10
    print(f"A decade ago you were {decade} years old.")

    # To get the users age for the next 50 years per 10 years interval
    half_century = age + 10
    print(f"In 2030 you'll be {half_century} years old.")

    half_century_1 = age + 20
    print(f"In 2040 you'll be {half_century_1} years old.")

    half_century_2 = age + 30
    print(f"In 2050 you'll be {half_century_2} years old.")

    half_century_3 = age + 40
    print(f"In 2060 you'll be {half_century_3} years old.")

    half_century_4 = age + 50
    print(f"In 2070 you'll be {half_century_4} years old")


# Calling out the greet_user function
greet_user()
