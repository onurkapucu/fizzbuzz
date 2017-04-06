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
Intiutively, I first thought of implementing a deterministic primality test. My logic was checking if the fibonacci number is divisible to numbers upto its square root.Then I decided on keeping the primes calculated in previous steps to speed up the function.This way I am am calculating primes upto square root of the fibonacci and expanding the list every time. I check divisibility of my fibonacci to these primes.This is "fizbuzz_deterministic" code. Although it is deterministic, it requires heavier processing and will eventually slow down. Therefore, I searched for lighter primality tests online and I coded "fizzbuzz_stochastic" using Rabin-Miller pseudocode I found online.
Despite its simplicity this is a stochastic primality test with a possibility of false positives. 

# Addendum - Rabin Miller Primality Test Logic
After searching online for primality tests, I decided on trying to implement the Miller-Rabin method. Pseudocode is as follows:(Taken from https://en.wikipedia.org/wiki/Miller–Rabin_primality_test)  
  

write n − 1 as 2r·d with d odd by factoring powers of 2 from n − 1  
WitnessLoop: repeat k times:  
&nbsp;&nbsp;&nbsp;pick a random integer a in the range [2, n − 2]
&nbsp;&nbsp;&nbsp;x ← ad mod n  
&nbsp;&nbsp;&nbsp;if x = 1 or x = n − 1 then  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;continue WitnessLoop  
&nbsp;&nbsp;&nbsp;repeat r − 1 times:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x ← x2 mod n  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if x = 1 then  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return composite  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if x = n − 1 then  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;continue WitnessLoop  
&nbsp;&nbsp;&nbsp;return composite  
return probably prime  

