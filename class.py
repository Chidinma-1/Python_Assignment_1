import random
from math import sqrt

# def test_function():
#     print(4*2 + 2)

# def test_function(n: float):
#     print (n*2 + 2)


# test_function(3)


# def fun3(a, b, c):
#     print(a, b, c)


# # POSITIONAL ARGUMENT
# fun3(1, 2, 3)
# # KEYWORD ARGUMENT
# fun3(b=1, c=3, a=2)
# # ARBITRARY ARGUMENT
# fun3(1, b=3, c=2)


# def mean(arr):
#     mean_value = sum(arr)/len(arr)
#     return round(mean_value, 2)


# print("Calculate your mean")
# print("Enter your number seperated by comma")
# vals = input(":>").split(",")

# print(mean(mapped))

# h = 1
# while h <= 10:
#     h += 1
#     print(h)


# GAME 1
# a = [1, 2, 3, 4, 5, 6, 7]

# random.shuffle(a)
# trial = 3
# score = 0

# while trial > 0:
#     print("\nSelect a number from", a)
#     com_choice = random.choice(a)
#     user = int(input("Your choice \n:>"))
#     if user == com_choice:
#         print("You Win")
#         score += 2
#         trial += 1
#         print(f"You have won an extra trial")
#         print(f"{trial} trial(s) left")
#     else:
#         if user > com_choice:
#             print("Too high")
#         else:
#             print("Too low")
#         trial -= 1
#         print(f"{trial} trial(s) left")

# print(f"\nYou scored {score} points")
# print("Game Over ):")


# options = ["r", "p", "s"]
# trial = 3
# score = 0

# while trial > 0:
#     print(""" Select R for rock, P for paper and S for scissors.""")
#     com_choice = random.choice(options)
#     player_choice = input(">").lower()
#     if player_choice in options:
#         if player_choice == options[0] and com_choice == options[2]:
#             print("You win")
#             print("Computer choose", com_choice)
#             trial += 1
#             trial += 2
#         elif player_choice == options[2] and com_choice == options[1]:
#             print("You win")
#             print("Computer choose", com_choice)
#             trial += 1
#             trial += 2
#         elif player_choice == options[1] and com_choice == options[0]:
#             print("You win")
#             print("Computer choose", com_choice)
#             trial += 1
#             trial += 2
#         elif player_choice == com_choice:
#             print("It's a tie")
#         else:
#             print("You lose")
#             print("Computer choose", com_choice)
#             trial -= 1
# else:
#     print("I nvalid output")
#     print("You scored", score)

# DATA STRUCTURES
# STRUCTURES IN WHUCH WE CAN STORE DATA

# a = [1, 2, 3, 4, 5]
# b = [6, 7, 8, 9, 10]
# b[3] = 82
# print(b)

# slicing
# a = [1, 2, 3, 4, 5, 6, 7, 8]
# a[2:5]
# # Traversing with a for loop

# for element in a:
#     print(element)

# creating new list with for loops using list comprehension
# v = [x if x % 2 == 0 else 0 for x in range(10)]
# print(v)
