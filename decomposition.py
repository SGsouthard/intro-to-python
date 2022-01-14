# /***********************************************************************
# In these exercises we will be practicing decomposition by building
# multiple functions. Be sure to test each function thoroughly as you go
# before moving on to the next problem. Each function will require the
# previous to solve.
# ***********************************************************************/


# /***********************************************************************
# Write a function `isPrime(number)` that returns a boolean indicating if
# `number` is prime or not. Assume `number` is a positive integer.
# Examples:
# isPrime(2); // => true
# isPrime(1693); // => true
# isPrime(15); // => false
# isPrime(303212); // => false
# ***********************************************************************/

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

print(is_prime(654239))
print('2', is_prime(2))
print('1693', is_prime(1693))
print('15', is_prime(15))
print('303212', is_prime(303212))
  
# /***********************************************************************
# Using the `isPrime` function you made, write a function `firstNPrimes(n)`
# that returns an array of the first `n` prime numbers.
# Examples:
# firstNPrimes(0); // => []
# firstNPrimes(1); // => [2]
# firstNPrimes(4); // => [2, 3, 5, 7]
# ***********************************************************************/

def first_n_primes(n):
    result = []
    num = 2
    if n == 0:
        return result
    while len(result) < n:
        if is_prime(num):
            result.append(num)
        num += 1
    return result

print('15', first_n_primes(15))
print('6', first_n_primes(6))
print('9', first_n_primes(9))

# /***********************************************************************
#  Using `firstNPrimes`, write a function `sumOfNPrimes(n)` that returns
# the sum of the first `n` prime numbers.
# Examples:
# sumOfNPrimes(0); // => 0
# sumOfNPrimes(1); // => 2
# sumOfNPrimes(4); // => 17
# ***********************************************************************/

def sum_of_n_primes(n):
    arr = first_n_primes(n)
    result = 0
    if len(arr) == 0:
        return 0
    
    for num in arr:
        result += num
    return result

print(15, sum_of_n_primes(15))
print(0, sum_of_n_primes(0))
print(1, sum_of_n_primes(1))
print(4, sum_of_n_primes(4))
print(6, sum_of_n_primes(6))
print(9, sum_of_n_primes(9))