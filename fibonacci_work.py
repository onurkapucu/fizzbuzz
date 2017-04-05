# Uses python3
from random import randrange

n = int(input())

def calc_fib(fib_n):
        a = [0] * (fib_n+1)
        a[1] = 1
        a[2] = 1
        if fib_n == 1:
            print(1)
        elif fib_n == 2:
            print(1)
            print(1)
        else:
            print(1)
            print(1)
            for i in range(3, (fib_n)+1):
                a[i] = (a[i-2] + a[i-1])
                if a[i] % 3 == 0 and a[i] % 5 == 0:
                    print('FizzBuzz')
                elif a[i] % 5 == 0: 
                    print('Fizz')
                elif a[i] % 3 == 0: 
                    print('Buzz')
                elif is_prime(a[i]):
                    print('BuzzFizz')
                else:
                    print(a[i])

def is_prime(n):
    
    s = 0
    d = n - 1

    if n == 2:
        return True
    elif n % 2 == 0:        
        return False
    else:
        while d % 2 == 0:
            s += 1
            d >>= 1  
        for i in range(10):
            flag = 1
            a = randrange(2, n - 1)
            x = temp = pow(a, d, n)
            if x != 1 and x != n -1:
                for r in range(s):
                    x = pow(x,2,n)
                    if x == 1:
                        return False
                    elif x == n-1:
                        flag = 0
                        break
                if flag:
                    return False
        return True

            
calc_fib(n)
