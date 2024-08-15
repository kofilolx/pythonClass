#!/usr/bin/python3

x = int(input("Please enter an integer: "))     #type casting string to integer values using int()

# -- beginning of if statement --
if x < 0:
    x = 0
    print("Negative changed to zero")
elif x == 0:
    print("You eneter zero")
elif x == 1:
    print("Single int")
else:
    print("More integers")
