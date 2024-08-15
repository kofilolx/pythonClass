"""myDream = ["Ford Mustang", "American Muscle", "estate guru", "Forex trader",
           "CyberSecurity Company"]
myDream[2] = "ducat"
myDream.remove("ducat")
del myDream[1]
popped_dream = myDream.pop(1)
message = "I would like to own a"
for x in myDream:
    print(f"{message} {x.title()} if God permits")
    print(f"This was popped {popped_dream}")
    print(f"This was removed '{popped_dream.upper()}' but still holds in the list")
    """

# # new assignment on list
# guest_list = ["Sammy", "Haliq", "Confidence"]
# welcome_msg = "Welcome to Wick Dinner Party."
# guest_list[0] = "Ken_Azu"
# guest_list.insert(0, "Albert")
# guest_list.insert(2, "Linda Akua")
# guest_list.append("Baron")
# info_msg = "Sorry only two members can join, but stick around you might be given a table to sit next to."
# # print(info_msg)
# popped_member = guest_list.pop(0)
# popped_member2 = guest_list.pop(4)
# popped_member3 = guest_list.pop(2)
# popped_member4 = guest_list.pop(1)
#
# for x in guest_list:
#     print(f"Hello! {x}. {welcome_msg}")
#
# print(f"\n{popped_member} {info_msg}"
#       f"\n{popped_member2} {info_msg}"
#       f"\n{popped_member3} {info_msg}"
#       f"\n{popped_member4} {info_msg}")
#
# del guest_list[0]
# del guest_list[-1]
#
# print(f"\nCurrent list {guest_list}")
# print(f"In any other words i'm inviting {len(guest_list)} "
#       f"people to the party")


# Sorting list
# myCars = ["Benz", "Ford", "Hundai", "Mahindra", "Bentley", "Toyota", "Mistubushi"]
# print(f"Here is the original list: \n{myCars}")
# print(f"Here is the list of sorted list:\n{sorted(myCars)}")
# print(myCars)
# print(myCars.sort(reverse=True))
# print(len(myCars))


# places to visit in the world
# fav_countries = ["Sweden", "Germany", "Norway", "Russia", "Turkey"]
# print(sorted(fav_countries))
# print(fav_countries)
# fav_countries.reverse()
# print(fav_countries)
# fav_countries.reverse()
# print(fav_countries)
# fav_countries.sort()
# print(fav_countries)
# fav_countries.sort(reverse=True)
# print(fav_countries)

# looping through an entire list

# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(magician.title(),"thats a great trick")

# pizzas = ["Pepperoni", "Magaritta", "MeatEater"]
# for pizza in pizzas:
#     print(f"I like {pizza} pizza.")
#
# print("I really love pizza!")
#
# animals = ["Parrot", "Eagle", "Dove"]
# msgPet = "would make a great pet"
# for pet in animals:
#     print(f"A {pet} {msgPet}")
#
# print(f"Any of these animals {msgPet}")
#
# numbers = list(range(1, 6))
# for val in range(1, 10):
#     print(val)
#
# print(numbers)
# squares =[]
# for val in range(1,11):
#     square = val**2
#     squares.append(square)
#
# print(sum(squares)+min(squares)+max(squares))

# # list comprehension
# value = input("Enter a number: ")
# val = int(value)
# squares = [val**2 for val in range(1, 11)]
# print(squares)


# count = [val+1 for val in range(0, 20)]
# print(count)
# def mill():
#     mil = [num +1 for num in range(0,100000000)]
#     return mil
#
# mill()

# odd = []
# for val in range(1,11):
#     oddNum = val*3
#     odd.append(oddNum)
# print(odd)

# players = ['Charles', 'Martin', 'Bullet', 'Britain']
# print(f"Here are the best three names:\n")
# for player in players[:3]:
#     print(player.title())
#
# # copying a list
# myFav = ['banku', 'bread', 'Jollof']
# urFav = myFav[:]
# myFav.append('riverBird')
# del myFav[2]
#
# print(f"Here are my favorite foods\n{myFav}")
# print(f"Here are your favorite food as well\n{urFav}")

# #########################################################
# Tuples is just like list but it is initiated using a bracket instead of parenthesis
# dimensions = (500, 23)
# items in a tuple can't be altered but variable can be overridden. example
# dimensions = (170, 152, 56, 89)
# print(dimensions[0])
#
# # looping through a tuple
#
# for dimension in dimensions:
#     print(dimension)

# #### Conditional statement ####
"""cars =["audi", "BMW", "Toyota"]
for car in cars:
    if car == 'audi':
        print(car.upper())
    else:
        print(car.title())

user_age = input("Enter age: ")

if int(user_age) <= 4:
    print(f"Admission for under 4 if free, {user_age} is valid")
elif 4 <= int(user_age) <= 18:
    print(f"Admission for anyone between the ages of 4 and 18 is USD5")
else:
    print(f"Admission for anyone age 18 or older is USD 10")
"""

"""age = 16

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5

print(f"Your admission cost is USD {price}.")

alien_color = ['green', 'yellow', 'red']

if 'yellow' in alien_color:
    print("Correct! you have 5 points")
if 'green' in alien_color:
    print("Correct! you earned 10 points...")
if 'red' in alien_color:
    print("Correct! you earned 15 points.")
else:
    print("aliens are camouflage like/")"""

"""stg_life = "Stage of life app."
user_age = input("Enter age: ")
age = int(user_age)

if age < 2:
    print("You're a  baby")
elif age < 4:
    print("You're a toddler.")
elif age < 13:
    print("You're a kid")
elif age < 20:
    print("You're a teenager")
elif age < 65:
    print("You're an adult")
elif age > 65:
    print("You're an elder")
else:
    print("for your age cat u can discuss w/ Methuselah")"""

# users = ['admin', "Joel", "hSoc13y", "fSociety", "mufasah"]
#
# for user in users:
#     if 'admin' in user:
#         print(f"Hello {user}, would you like to see a status report?")
#         # break
#     else:
#         print(f"Hello {user}, thank you for logging in again.")

"""
current_user = ['Juliet', "Portia", "hSoc13y", "fSociety", "mufasah"]
new_user = ['Fuego', "Joel", "hSoc13y", "fSociety", "nafisah"]

for user in new_user:
    if user in current_user:
        print(f"{user.title()} already exit, enter new username")
    if user not in current_user:
        print(f"{user} is available. ")
    # if user == current_user:
    #     print(f"{user} cannot be accepted.")"""

"""ordinal_num = [x for x in range(1, 10)]
for val in ordinal_num:
    if 1 == val:
        print("1st")
    elif 2 == val:
        print("2nd")
    elif 3 == val:
        print("3rd")
    else:
        print(f"{val}th")"""

# #### dictionaries | variable = {key: value } ####

"""alien_0 = {'x_position':0, 'y_position': 25, 'speed': 'medium'}
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New x-position: {str(alien_0['x_position'])}")"""

# fav_lan = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python'
# }
# print(f"Sarah's favorite language is "
#       f"{fav_lan['sarah'].title()}.")

"""user_details = {
    'first_name': 'joel',
    'last_name': 'count',
    'age': 25,
    'city': 'Accra'
}
for key, value in user_details.items():
    print(f"{key} : {value}")

for value in user_details.values():
    print(value)

for key in user_details.keys():
    print(key)

user_val = input("Just do it: ")
user_val = int(user_val)
print(user_val)

user_num = input("Please enter any number:")
user_num = int(user_num)

if user_num % 2 == 0:
    print(f"\nThe number {str(user_num)} is an even number")
else:
    print(f"\nThe number {str(user_num)} is an odd number")

"""
# practice code self test
# car_rental = input("Your choice of car: ")
# print(f"let me see if i can find you a {car_rental.title()}")
#
# seat_book = input("How many people would be on the table: ")
# seat_book = int(seat_book)
#
# if seat_book > 8:
#     print(f"\nSorry, you would have to wait for us to prepare you a new table")
# else:
#     print(f"\nTable of {seat_book} people is ready.")
#
#
# userNum = input("Enter a value: ")
# userNum = int(userNum)
#
# if userNum % 10 == 0:
#     print(f"The number {userNum} is a multiple of ten.")
# else:
#     print(f"The number {userNum} is not a multiple of ten")


## #### While loops | while (condition) ####

# current_num = 7
# while current_num <= 5:
#     print(current_num)
#     current_num += 1
#
# prompt = f"\nTell me somehting, and i will repeat it back to you:" \
#          f"\nEnter 'quit' to end the program.\n"

# message = ""
# while message != 'quit':
#     message = input(prompt)
#     print(message)

# using a flag
"""active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
        print(f"You just ended the fun with {message}")
    else:
        print(message)

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}.")
"""

# Using continue in a loop

# current_num = 0
# while current_num < 10:
#     current_num += 1
#     if current_num % 2 == 0:
#         continue
#     print(current_num)

# self test
"""customer_name = input("customer: ")
pizza_type = input("Pizza: ")
prompt_msg = f"\n{customer_name.title()} add extra toppings to your {pizza_type}." \
             f"\nquit to grab {pizza_type} without extra toppings.\n: "

pizza_top= ""
active = True
while active:
    pizza_top = input(prompt_msg)
    if pizza_top == 'quit':
        active = False
    else:
        print(f"\nHello {customer_name.title()}!\n"
              f"{pizza_top.title()} would be added to your {pizza_type}"
              f"\nThank You.")

print(f"\n{customer_name} enjoy your {pizza_type} pizza!")"""

# movie tickets

"""wlc_msg = "Welcome to Wick theater!"
prompt = "\nWould you like to buy another ticket (y|n): "

active = True
while active:
    customer_age = input("\nHow old are you: ")
    customer_age = int(customer_age)
    if customer_age < 3:
        print(f"{wlc_msg} Free entry for kids!")
    elif customer_age < 12:
        print(f"{wlc_msg} Teenage ticket is USD10")
    else:
        print(f"{wlc_msg} Adult ticket is USD15")

    repurchase = input(prompt)
    if repurchase == 'n':
        active = False
        
print("Enjoy the climax!")

ticket = ""
while ticket != 'n':
    customer_age = input("How old are you: ")
    customer_age = int(customer_age)

    if customer_age < 3:
        print(f"{wlc_msg} Free entry for kids!")
    elif customer_age < 12:
        print(f"{wlc_msg} Teenage ticket is USD10")
    else:
        print(f"{wlc_msg} Adult ticket is USD15")

    ticket = input(prompt)

print("Enjoy the climax!")"""


# #### using a while loop with lists and dictionaries ####
# users = []
# active = True
# while active:
#     name = input("Enter name: ")
#     users.append(name)
#     if name == 'quit':
#         active = False
#
# del users[-1]
# users.sort()
# for user in users:
#     print(user)


# unconfirmed_users = ['alice', 'bod', 'trudy']
# confirmed_users  =[]
#
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#
#     print(f"Verifying user: {current_user.title()}")
#     confirmed_users.append(current_user)
#
# print(f"\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())
#
# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# # print(pets)
#
# while 'dog' in pets:
#     pets.remove('dog')
#
# print(pets)

# #### Self test ####
"""sandwich_orders = ["Pastrami", "Pastrami", "Pastrami", "meat sandwich", "vegan Sandwich", "Tuna Sandwich", "Salmon sandwich", "chicken fillet sandwich"]
finished_sandwiches = []

for sandwich in sandwich_orders:
    print(f"I made your {sandwich}")

print("\nThe Deli has run out of pastrami sandwich\n")

while sandwich_orders:
    current_orders = sandwich_orders.pop()
    finished_sandwiches.append(current_orders)

while 'Pastrami' in finished_sandwiches:
    finished_sandwiches.remove("Pastrami")

for sandwich in finished_sandwiches:
    print(f"{sandwich.title()} was made.")


polls_prompt = "If you could visit one place in the world, where would you go?" \
               "\nQuit to exit. \n"

dream_vacation = []
polls_active = True

while polls_active:
    user_opt = input(polls_prompt)
    dream_vacation.append(user_opt)
    if user_opt == 'quit':
        polls_active = False

del dream_vacation[-1]
dream_vacation.sort()

for opt in dream_vacation:
    print(f"You dream of visiting {opt}")
"""
