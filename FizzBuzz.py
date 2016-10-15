'''
Fizz Buzz
Any number divisible by '3' is replaced by Fizz
Any number divisibl by '5' is replaced by Buzz
Any number divisible by both '3' and '5' is repalced by FizzBuzz
'''

# Basic
for num in range(1,16):
    if num % 3 == 0 and num % 5 == 0:
        print('Fizz Buzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 ==0:
        print('Buzz')
    else:
        print(num)

# Slightly better
for num in range(1,16):
    msg = ''
    if num % 3 == 0:
        msg += 'Fizz'
    if num % 5 == 0:
        msg += 'Buzz'
    else:
        msg = num
    print(msg)

# Best
for num in range(1,16):
    msg = ''
    if num % 3 == 0:
        msg += 'Fizz'
    if num % 5 == 0:
        msg += 'Buzz'
    print (msg or num)

#GOLF
for n in xrange(1, 101):
    print("Fizz"*(n % 3 == 0) + "Buzz"*(n % 5 == 0) or n)
