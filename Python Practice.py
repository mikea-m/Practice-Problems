# Practice problems

    # 1. Print ‘Hello World’ to the screen.
def q1():
    print('Hello World')
#q1()

    # 2. Ask the user for their name and greet them with their name.
def q2():
    name = intro()
    greeting(name)
def intro():
    name = input('What is your name? \n')
    return name
def greeting(name):
    print('Hello ' + name + '! It\'s nice to meet you.')
#q2()

    # 3. Modify the previous program such that only the users Alice and Bob are greeted with their names.
def q3():
    name = intro()
    if name.lower() == 'alice' or name.lower() == 'bob':
        greeting(name)
    else:
        print('It\'s nice to meet you!')
#q3()

    # 4. Ask the user for a number n and print the sum of the numbers 1 to n
def q4():
    n = getNum()
    getSum(n)   
def getNum():
    n = input('Input a positive integer n: ')
    n = range(int(n) + 1)
    return n
def getSum(n):
    total = sum(n)
    print('The sum of the numbers 1 to n is ' + str(total) + '.')
#q4()

    # 5. Modify the previous program such that only multiples of three or five are considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17
def q5():
    n = getNum()
    total = 0
    for i in n:
        if i % 3 == 0 or i % 5 == 0:
            total = total + i
            print(str(total))
    print('The sum of the multiples of 3 and 5 from 1 to n is ' + str(total) + '.')
#q5()
    
    # 6. Ask the user for a number n and give them the possibility to choose between computing the sum and computing the product of 1,…,n.
def q6():
    n = getNum()
    choice = input('To compute the sum of numbers 1 to n, enter 1. \n'
                   'To compute the product of numbers 1 to n, enter 2. \n')
    if choice == '1':
        getSum(n)
    elif choice == '2':
        getProduct(n)
def getProduct(n):
    product = 1
    for i in n[1:len(n)]:
        product = product * i
    print('The product of numbers 1 to n is ' + str(product) + '.')
#q6()

    # 7. Print a multiplication table for numbers up to 12.
def q7():
    numbers = list(range(12))

    for i in range(12):
        for j in range(12):
            numbers[j] = (i+1)*(j+1)
        print(numbers)
#q7()

    # 8. Print all prime numbers.
def q8():
    end = '1'
    lower = -98
    upper = 2
    print(2)
    while end == '1':
        lower += 100
        upper += 100
        for i in range(lower,upper):
            k = 2
            while i % k != 0:
                k += 1
                if k == i-1:
                    print(i)
        end = input('To print all primes from ' + str(upper) + ' to ' + str(upper + 100) + ' press 1. '
              'To end the program, press 2. \n')
#q8()

    # 9. Write a guessing game where the user has to guess a secret number.
        # After every guess the program tells the user whether their number was too large or too small.
        # At the end the number of tries needed should be printed. 
def q9():
    import random

    number = random.randint(1, 100)
    guess = int(input('Guess the secret number! \n'))
    count = 1

    while guess != number:
        guess = int(input('Not quite! Try again: '))
        count += 1

    print(str(guess) + ' is correct! You found the secret number in ' + str(count) + ' guesses.')
#q9()

    # 10. Write a program that prints the next 20 leap years.
def q10():
    def leaps():
        for i in range(1,21):
            leapYear = thisYear + (4*i)
            print(leapYear)
            
    thisYear = 2023

    for i in range(0,4):
        if thisYear % 4 == i:
            thisYear -= i
            leaps()
#q10()

    # 11. Write a program that computes the sum of an alternating series where each element of the series is an expression of the form 
        # ((-1)^k+1) / (2*k-1) for each value of k from 1 to a million, multiplied by 4. 
import math

#total = float(0)
#for k in range(1,1000001):
#    total += (math.exp(k+1)) / (2*k - 1)
#total *= 4
#print(total)






               
