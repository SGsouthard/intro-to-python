# Comment syntax uses Hashtags
# this is a comment
# TODO is built into Python
# https://github.com/SEI-1025/TOOLBOX/tree/main/unit-4/15-python/python-intro for notes

def add():
    '''
    this is supposed to add 2 numbers
    '''

'''
three singly quotes is a multiline comment
'''

name = "Sydney"

nothing = None

is_working = True
car_off = False

# if nothing:
#     print("This is true") # [x]
#     num = 7
#     print(
#         'car is off'
#     )
# elif car_off:
#     print('this is the second condition')
# elif is_working:
#     print("This is working")
# else: 
#     print("This is not true...")


# if is_working: 
    # print("This is working also")
# conditional -> this first item that represents
# True, it runs that indented block

# print(15 / 6)
# print(15 // 6)

# print("Ace of spades".split(" "))
#  => ["ace", "of", "spades"]

# print("abcde".split(""))
# won't function because it can't split on empty strings

my_string = "My code is the best"

# print(my_string[3])
# print(my_string[-1])
# print(my_string[2:8])
# print(my_string[0:8:2])
# print(my_string[:8])
# print(my_string[3:])
# print(my_string[::-1])

# if 7 == 7:
#     print("These are equal")
# else:
#     print("These are not equal")

# if 7 == 6:
#     print("These are equal")
# else:
#     print("These are not equal")

# if not 7:
#     print("This is 7")
# else:
#     print("This is not 7")

# arr = [1,"two", 3, "four", True, False, "hello"]
# print(arr[1])
# print(arr[-1])

# one_through_ten = list(range(10))
# print(one_through_ten)

# three_through_ten = list(range(3, 10))
# print(three_through_ten)

# a = [1, 23, 12, 99, 82]
# a.sort()
# a = a[::-1]
# a.append("Hey")
# a.insert(4, 69)
# a.pop()
# print(a)

# if 42 in a:
#     print("Yep it's there")
# else: 
#     print("Nah dog")

# if 69 in a:
#     print("Nice")
# else: 
#     print("Nah dog")

# String Interpolation
#  1
# state = "Washington State"
# year = 1889
# n = 42
# my_message = f"{state} was the {n}nd state to join the union in {year}."

# print(my_message)

# # 2
# game = "Kingdom Hearts"
# ranking = 1

# my_second_message = f"{} is my #{} favorite game of all time"

# print(my_second_message.format("Assassin's Creed", 2)

# # 3

# game = "Kingdom Hearts"
# ranking = 1

# my_second_message.format()

# print(my_second_message)

# def st_nd_rd_th(n):
#   # add one to 13 because range is exclusive at the end.
#   if n in range(11, 13 + 1):
#     return "th"
#   if n % 10 == 1:
#     return "st"
#   elif n % 10 == 2:
#     return "nd"
#   elif n % 10 == 3:
#     return "rd"
#   else:
#     return "th"

# state = "Washington State"
# year = 1889
# n = 42
# my_message = f"{state} was the {n}{st_nd_rd_th(n)} state to join the union in {year}."
# print(my_message)

# foods = ["carrots", "kale", "beets"]
# for food in foods:
#   print("I like", food)

# print("My favorite foods:")
# foods = ["carrots", "kale", "beets"]
# for i, food in enumerate(foods):
#   print("{}. {}".format(i, food))

def say_hello(friend="Tim"):#If there's no paramater, it will default to Tim
  print("Hello, {}!".format(friend))

say_hello("enemies of the state")

def move(name, city="Seattle", state="Washington"):
  msg = "{} is moving to {}, {}"
  msg = msg.format(name, city, state)
  print(msg)

move("Sydney", "San Diego", "California")

def feed(rat="Jeepers", food="Cheerios")
  msg = "You fed {} some delicious {}"
  msg = msg.format(rat, food)
  print(msg)

feed()