numbers = [1, 2, 3, 4]
def double_number(num):
    return num + num

result1 = map(double_number, numbers)
# print("Result 1", result1)

result2 = map(lambda x: x + x, numbers)
# print("Result 2", list(result2))

result3 = map(lambda y: y * y, numbers)
# print("Result 3", list(result3))

def triple_number(num):
    return num + num + num

result1a = map(triple_number, numbers)
# print('Result 1a', list(result1a))

result2a = map(lambda x: x + x + x, numbers)
# print("Result 2a", list(result2a))

result3a = map(lambda y: y * y * y, numbers)
# print("Result 3a", list(result3a))

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
numbers3 = [7, 8, 9]
  
result4 = map(lambda x, y: x + y, numbers1, numbers2)
# print("Result 4", list(result4))

result4a = map(lambda x, y, z: x + y + z, numbers1, numbers2, numbers3)
# print("Result 4a", list(result4a))


# a list contains both even and odd numbers. 
seq = [0, 1, 2, 3, 5, 8, 13]
  
# result contains odd numbers of the list
result5 = filter(lambda x: x % 2 != 0, seq)
# print("Result 5", list(result5)) # [1, 3, 5, 13]
  
# result contains even numbers of the list
result6 = filter(lambda x: x % 2 == 0, seq)
# print("Result 6", list(result6)) # [0, 2, 8]


ages = [23, 17, 21, 20, 19, 34, 40, 41, 22, 25, 27]

young_folks = list(filter(lambda person_age: person_age < 21, ages))
old_folks = list(filter(lambda person_age: person_age > 21, ages))
print('Young Folks', young_folks)
print('Old Folks', old_folks)

def is_not_21(person_age):
    if person_age < 21:
        return True
    else: 
        return False

def is_21(person_age):
    if person_age >= 21:
        return True
    else: 
        return False

young_people = list(filter(is_not_21, ages))
old_people = list(filter(is_21, ages))

print("Young people", young_people)
print("Old People", old_people)
