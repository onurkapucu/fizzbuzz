# Uses python3
from random import randrange

#This code takes an input n and prints first n fibonacci numbers with a twist. 
#If the Fibonacci number is divisible by 3, it prints "Buzz", if it is divisible 
#by 5, it prints "Fizz", if it is divisible by both, it prints "FizzBuzz" ,
#and if the Fibonacci number is a prime number it prints "Buzzfizz".

#Code uses Miller-Rabin Primality test 

n = int(input())

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

#This is the part of the code where I check for primality. I coded following based on a
#pseudocode for Miller Rabin Primality Test. This is a probabilistic method to determine 
#if the given number is prime or not. Method can be repeated with different random conditions
#to increase the probability of getting the right answer. I pre-selected repeat-number as 10.
def is_prime(n):

    repeat_number =10

    if n == 2: #Check if number is 2
        return True
    elif n % 2 == 0: #Check if number is even    
        return False
    else:
        s = 0
        d = n - 1 
        while d % 2 == 0: # we try to itemize n-1 as d*2^s
            s += 1
            d >>= 1  
        for i in range(repeat_number):
            flag = 1
            a = randrange(2, n - 1)
            x = temp = pow(a, d, n)
            if x != 1 and x != n -1: #else it is probably prime
                for r in range(s):
                    x = pow(x,2,n)
                    if x == 1:
                        return False
                    elif x == n-1:
                        flag = 0 #Probably Prime
                        break
                if flag:
                    return False
        return True
            
calc_fib(n)
