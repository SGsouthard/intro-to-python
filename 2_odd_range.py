def odd_range(end):
    arr = []
    for num in range(end):
        if num % 2 != 0:
            arr.append(num)
    return arr

print(odd_range(27))