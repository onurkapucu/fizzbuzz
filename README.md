# fizzbuzz
This is a nontrivial fizzbuzz code.

This code generates the first n Fibonacci numbers F(n), printing

* "Buzz" when F(n) is divisible by 3.
* "Fizz" when F(n) is divisible by 5.
* "FizzBuzz" when F(n) is divisible by 15.
* "BuzzFizz" when F(n) is prime.
* the value F(n) otherwise.

# Code Comments
Based on the requirements and importance of outcome, one can use probabilistic code or deterministic code to answer the question.

# Personal Comments
Fizbuzz and fibonacci parts of the code were straightforward.
Intiutively, I first thought of implementing a deterministic primality test. My logic was checking if the fibonacci number is divisible to numbers upto its square root. Then I decided on creating an array of primes to reduce the repetitions and I came up with "fizbuzz_deterministic" code. Although it is deterministic, it requires heavy processing. Therefore, I searched for lighter primality tests online and I coded "fizzbuzz_stochastic" using Rabin-Miller pseudocode I found online.
Despite its simplicity this is a stochastic primality test with a possibility of false positives. 

# Addendum - Rabin Miller Primality Test Logic
After searching online for primality tests, I decided on trying to implement the Miller-Rabin method. Pseudocode is as follows:(Taken from https://en.wikipedia.org/wiki/Miller–Rabin_primality_test)  
  
"  
write n − 1 as 2r·d with d odd by factoring powers of 2 from n − 1  
WitnessLoop: repeat k times:  
    pick a random integer a in the range [2, n − 2]  
...x ← ad mod n  
...if x = 1 or x = n − 1 then  
......continue WitnessLoop  
...repeat r − 1 times:  
......x ← x2 mod n  
......if x = 1 then  
.........return composite  
......if x = n − 1 then  
.........continue WitnessLoop  
...return composite  
return probably prime  
"  

