# All README material gets handled here

#========== Task 2 ===========
# 1
idx = "abcde".index('d')
idx = idx + 11
print('Task 2: Problem 1: ', idx)

# 2
num = 33
isEven = num % 2 == 0
print('Task 2: Problem 2a: ', isEven)
print('Task 2: Problem 2b: ', not isEven)

# 3
str1 = 'marker'
num = len('whiteboard') - len(str1)
print('Task 2: Problem 3a: ', num)
str2 = 'bootcamp'
print('Task 2: Problem 3b: ', str2[num].upper())
char = str2[num].lower()
print('Task 2: Problem 3c: ', char + '!')

# 4
sentence = 'welcome to bootcamp prep'
lastChar = sentence[len(sentence) - 1]
print('Task 2: Problem 4a: ', lastChar)
print('Task 2: Problem 4b: ', sentence.index(lastChar))

#========== Task 3 ===========
# 5
age = 3
if age > 30 :
    print('Task 3: problem 5: ', "older than 30")
else: 
    print('Task 3: problem 5: ', "younger than 30")

# 6
str = 'cheeseburger'
if len(str) > 10:
    print('Task 3: Problem 6: ', "That's a long string")
else: 
    print('Task 3: Problem 6: ', "That's a short string")
if str[0] == 'p':
    print('Task 3: Problem 6: ', "starts with P")
else:
    print('Task 3: Problem 6: ', "Doesn't start with a P")

# 7
num = 25
if num % 3 == 0:
    print('Task 3: Problem 7: ', "Divisible by 3")
elif num % 5 == 0:
    print('Task 3: Problem 7: ', "Divisible by 5")

# 8
num = 69 #nice
if num % 3 == 0:
    print('Task 3: Problem 8: ', "Divisible by 3")
if num % 5 == 0:
    print('Task 3: Problem 8: ', "Divisible by 5")

# 9
str = 'Sailor MooN'
if str[0] == str[0].upper():
    print('Task 3: Problem 9: ', 'Starts with a capital')
if str[len(str)-1] == str[len(str)-1].upper():
    print('Task 3: Problem 9: ', 'Ends with a capital!')

# 10
num = 420
if num > 0:
    print('Task 3: Problem 10a: ', 'Positive')
elif num < 0:
    print('Task 3: Problem 10a: ', 'Negative')
else:
    print('Task 3: Problem 10a: ', 0)
if num % 2 == 0:
    print('Task 3: Problem 10b: ', 'Even')
else: 
    print('Task 3: Problem 10b: ', 'Odd')

#========== Task 4 ===========
# 11
num = 69
if num > 5:
    print("Task 4: Problem 11: ", "if")

# 12
num = -12
if num > 5:
    print("Task 4: Problem 12: ", "if")
else: 
    print("Task 4: Problem 12: ", "else")

# 13
num = 69
if num < 0:
    print("Task 4: Problem 13: ", "if")
elif num > 0:
    print("Task 4: Problem 13: ", "else if")
else: 
    print("Task 4: Problem 13: ", "else")

#========== Task 5 ===========
# 14
def say_hello(name):
    msg = 'Hello ' + name + '. How are you?'
    return msg

print("Task 5: Problem 14: ", say_hello('bootcamp prep'))

# 15
def check_number(num):
    if num > 0:
        return 'positive'
    elif num < 0:
        return 'negative'
    else:
        return 'zero'

print("Task 5: Problem 15: ", check_number(-420))

# 16
def fizz_buzz_1(max):
    for i in range(0, max):
        if i % 3 == 0 and i % 5 != 0:
            print(i)
        elif i % 5 == 0 and i % 3 != 0:
            print(i)

print("Task 5: Problem 16: ", fizz_buzz_1(27))

# 17
def even_caps(sentence):
    new_sentence = ""

    for i in range(len(sentence)):
        if i < len(sentence):
            char = sentence[i]
        if i % 2 == 0:
            capital_char = char.upper()
            new_sentence += capital_char
        else:
            new_sentence += char
    return new_sentence

print("Task 5: Problem 16: ", even_caps("Buttstuff"))
