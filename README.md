# fizzbuzz
This is a nontrivial fizzbuzz code.

This code generates the first n Fibonacci numbers F(n), printing

* "Buzz" when F(n) is divisible by 3.
* "Fizz" when F(n) is divisible by 5.
* "FizzBuzz" when F(n) is divisible by 15.
* "BuzzFizz" when F(n) is prime.
* the value F(n) otherwise.

#Comments
Fizbuzz and fibonacci parts of the code were relatively straightforward.
Intiutively, I first thought of implementing a deterministic primality test. My logic was checking if the fibonacci number is divisible to numbers upto its square root. Although it is deterministic, this is not an efficient method.
