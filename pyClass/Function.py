import random

def greet_user(username):
    print(f"Hello, {username.title()}!\n")


# user_name = input("Username: ")
# greet_user(user_name)


def display_message():
    print(f"I'm very delighted to learn a programming language call Python")


# display_message()


def fav_book(title):
    print(f"One of my favorite books is {title}.")


# fav_book("Africa is not a country")

# #### Passing Arguments - Positional |  ####
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"I have a {animal_type.lower()}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


# describe_pet('bunny', "bolt")
# pet_type = input("Please enter your pet type : "
#                  "\nDog / Cat /etc\n")
# pet_name = input("Please pet name: ")
# describe_pet(pet_type, pet_name)
# keyword Arguments
# describe_pet(pet_name="John Bull", animal_type="Hamster")

# default Values
def describe_pets(pet_name, pet_type='dog'):
    print(f"My pet {pet_name} is a {pet_type}")


# describe_pets(pet_name='JamesBond',)

# #### Self Test ####
def describe_city(country='Iceland'):
    print(f"Reykjavik is in {country}")


# describe_city('Ghana')
# describe_city('Gambia')
# describe_city('Iceland')
# describe_city()

# returning a simple value
def get_formatted_name(first_name, last_name):
    """return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


# dancer = get_formatted_name('Jonathan', 'Kotey')
# print(dancer)

# to give optional entry
# def get_name(lName, fName, mName=""):
#     if mName:
#         fullName = f"{lName} {fName} {mName}"
#     else:
#         fullName = f"{lName} {fName}"
#
#     return fullName


# details = get_name("kotey", 'Jonathan', 'Nikoi')
# print(details)

# def build_person(first_n, last_n):
#     """Return a dictionary of information about a person"""
#     person = {'first': first_n, 'last': last_n}
#     return person
#
#
# det_ails = (build_person("kotey", 'Loi han'))


# for det in det_ails.values():
# print(f"Your last name is {det[:].title()} and your first name is {det[:].title()} ")


"""def make_album(artiste, album_title):
    music = {'artiste': artiste, 'album': album_title}
    return music


prompt = "Please enter required details."
active = True
while active:
    user_artist = input("Enter artist name: ")
    user_album = input("Enter artist album: ")

    opt = input("would you like to continue? (y|n) ")
    if opt == 'n':
        active = False

    album = make_album(user_artist, user_album)
    print(album)"""


# #### Passing a List ####
"""def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


usernames = ['hannah', 'tily', 'Marriott']
greet_users(usernames)
"""
# explanation of the above
# username's data is being fed into the greet function (names).
# the list is then fed into the for loop's argument.


# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
#
# while unprinted_designs:
#     current_designs = unprinted_designs.pop()
#     completed_models.append(current_designs)
#
# for models in completed_models:
#     print(models)
#


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []


def display_model (unprinted_designs, completed_models):
    while unprinted_designs:
        current_designs = unprinted_designs.pop()
        completed_models.append(current_designs)


def display_cmpltd_models(completed_models):
    for models in completed_models:
        print(models)


# display_model(unprinted_designs[:], completed_models)
# display_cmpltd_models(completed_models)

def get_choices():
    player_choice = input()
    options = ["","",]
    computer_choice = random.choice(options)
    choices = {'key':player_choice, 'computer': computer_choice}
    return choices


def check_win(player, computer):
    return [player, computer]


magicians = ["David Blain", "Wink", "Willie wonker"]

def show_magic(magician):
    for magician in magicians:
        print(magician)


# show_magic(magicians)

toppings=["pepperoni", "Mushrooms", "Green Peppers", "Extra Cheese"]


def make_pizza( size = "large", *toppings,):
    """Print the list of toppings that have been requested.
    :param size:
    """
    print(f"Making a size:{size} pizza with the following toppings")
    for topping in toppings:
        print("-" + topping)


# make_pizza(12, "pepperoni")
# make_pizza(16, "Mushrooms", "Green Peppers", "Extra Cheese")


def build_profile(first, last, **user_info):
    """Building a dictionary to hold user details"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
        return profile


user_profile = build_profile('Albert', "einstein",
                             location = 'princeton',
                             field = 'physics')

print(user_profile)
