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
        else:
            print(a[0])
            print(a[1])
            for i in range(3, (fib_n)+1):
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

#Here I check if the given value is prime or not by checking if it is divisible to prime values up to it's square root.
def is_prime(n):
    global generatedUpto
    global primes
    if not isPrimeSoFar(n):
        return(False)
    continueGeneration(generatedUpto+1,n)
    generatedUpto = n
    if n in primes:
        return(True)
    return(False)

def isPrimeSoFar(i):
    sqrt = i**(0.5)
    for p in primes:
        if p > sqrt:
            break
        if i % p == 0:
            return False
    return True

def continueGeneration(n1,n2):
    global primes
    for i in range(n1,n2+1):
        if isPrimeSoFar(i):
            primes.append(i)


calc_fib(n)
