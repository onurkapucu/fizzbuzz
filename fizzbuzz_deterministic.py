# Uses python3
from random import randrange

#This code takes an input n and prints first n fibonacci numbers with a twist. 
#If the Fibonacci number is divisible by 3, it prints "Buzz", if it is divisible 
#by 5, it prints "Fizz", if it is divisible by both, it prints "FizzBuzz" ,
#and if the Fibonacci number is a prime number it prints "Buzzfizz".


n = int(input())
primes = [2]
generatedUpto = 2

#Here I calculate the Fibonacci values and check conditions.
#I assumed first Fibonacci to be 1.
def calc_fib(fib_n):
        a = [0] * (3) 
        a[0] = 1 
        a[1] = 1
        if fib_n == 1:
            print(a[0])
        elif fib_n == 2:
            print(a[0])
            print(a[1])
        elif fib_n == 3:
            print(a[0])
            print(a[1])
            print('BuzzFizz')
            a[2] = (a[0] + a[1])
            a[0]=a[1]
            a[1]=a[2]
        else:
            print(a[0])
            print(a[1])
            print('BuzzFizz')
            a[2] = (a[0] + a[1])
            a[0]=a[1]
            a[1]=a[2]
            for i in range(4, (fib_n)+1):
                a[2] = (a[0] + a[1])
                a[0]=a[1]
                a[1]=a[2]
                if a[2] % 3 == 0 and a[2] % 5 == 0: 
                    print('FizzBuzz')
                elif a[2] % 5 == 0: 
                    print('Fizz')
                elif a[2] % 3 == 0: 
                    print('Buzz')
                elif is_prime(a[2]):
                    print('BuzzFizz')
                else:
                    print(a[2])

#Here I check if the given value is prime or not. I have a "primes" array that keeps being updated as needed. 
#I first make a quick check, using isPrimeSoFar. This only checks if given number is divisible by prime numbers generated in the previous steps.
#Target is speeding up function. If I cannot detect compostie at this step, I go ahead and generate all the prime numbers upto the
#fibonacci number using continueGeneration.
def is_prime(n):
    global generatedUpto
    global primes
    if not isPrimeSoFar(n):
        return(False)
    sqrt_fib = int(n**(0.5))
    continueGeneration(generatedUpto+1,sqrt_fib)
    generatedUpto = sqrt_fib
    for i in primes:
        if n%i==0:
            return(False)
    return(True)

#isPrimeSoFar is a primality checker. It tries to divide input number with prime numbers upto inputs squre root. If it is divisible returns FALSE
#meaning that the input number is composite, else it returns True meaning that number is prime.  
def isPrimeSoFar(i):
    sqrt = i**(0.5)
    for p in primes:
        if p > sqrt:
            break
        if i % p == 0:
            return False
    return True

#This function expands the primes list from the latest call to current fibonacci. It checks primality of all numbers in between n1 and n2 by calling
#isPrimeSoFar which tries to divide its input with prime values upto its square root.
def continueGeneration(n1,n2):
    global primes
    for i in range(n1,n2+1):
        if isPrimeSoFar(i):
            primes.append(i)

calc_fib(n)
