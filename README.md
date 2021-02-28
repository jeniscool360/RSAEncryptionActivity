# Some fun with an RSA Cryptosystem
## What is an RSA Cryptosystem?
RSA is one of the oldest cryptosystems, relying on public and private keys to encrypt and decrypt messages. The generation of these keys relies on the product of 2 large prime numbers. Essentially, in order to decrypt a message, you need to know the original 2 prime numbers which are difficult to guess given that factoring is a computationally expensive process for large numbers. However, advancements like quantum computing are making this factoring process easier to do, rendering RSA less secure.

Learn more about RSA here:
* https://en.wikipedia.org/wiki/RSA_(cryptosystem)
* https://brilliant.org/wiki/rsa-encryption/
* https://www.technologyreview.com/2019/05/30/65724/how-a-quantum-computer-could-break-2048-bit-rsa-encryption-in-8-hours/

> NOTE: This code is not an optimal or secure implementation of RSA and should only be used for demonstration purposes.

## Learning Intentions
We are going to explore errors and limitations to this code and then use parallel computing to thoroughly test our code. 

Takeaways:

1. Know the 4 types of errors (syntax, overflow, runtime, and logic)
2. Know different ways to test code (test cases, hand tracing, visualizations, debuggers, adding extra output statements).
3. Use defined inputs to ensure that an algorithm or program is producing the expected outcomes. Check boundary cases.
4. Understand the difference between sequential, parallel, and distributed computing.

## Activities
### 1. Raise errors in the code
What does it mean to have a syntax error? An overflow error? A runtime error? A logic error? Explore these errors by trigging them in the code. 

__Syntax Error__
Just misspell something in the code.

__Overflow Error__
Try putting in the largest known Mersenne prime (`math.pow(2, 82589933)-1`) for one of the primes.
This will not work because the max size of a `float` (which `math.pow` calculates with) in python is `import sys; sys.float_info.max` which is `2^1024-1`. 

__Runtime Error__
Try putting in a string for encryption.

__Logic Error__
Try putting in an integer greater than n.

### 2. Use different methods to test code
We need to prevent our logic and runtime errors by writing some input validation in `main.py`. Use the following:
* Hand tracing (evaluate code by hand)
* pdb
* print statements

### 3. Write some test cases
Test cases are predefined inputs and corresponding expected outputs that demonstrate the capabilities of your code an ensure that functions work correctly. In python, test cases are done with the `assert` keyword, which raises an `AssertionError` if the test fails.

Do the following in `test.py`:

1. In `test_lcm()`, write some test cases for the `RSA.lcm(a,b)` function. The function should return the least common multiple of `a` and `b`. Use `assert` to check if the function gives the expected result (see `test_smallest_coprime()` for assertion examples).
2. In `test_encryption_boundary()`, write some boundary assertions for the maximum number `m` that RSA can encrypt/decrypt. Our RSA algorithm does not work for `m >= p*q`. Test numbers near `p*q` (the boundary).

### 4. Sequential vs. parallel testing
There are three types of computing:

1. *Sequential computing* is a computational model in which operations are performed in order one at a time. A sequential solution takes as long as the sum of its steps.
2. *Parallel computing* is a computational model where the program is broken into multiple smaller sequential computing operations, some of which are performed simultaneously. A parallel solution takes as long as its sequential tasks plus the longest of its parallel tasks.
3. *Distributed computing* is a computational model in which multiple devices are used to run a program. 

I wrote a test function called `test_encryption_big()` which compares the time it takes to encrypt/decrypt using primes from 700 to 1200. The difference between sequential and parallel tests is magnified if you run this code on your own machine as opposed to trying to run it in an online IDE.

In `test_encryption_big()`, change the `filename` to `"lotsOfBigPrimes.txt"` to observe a longer test (primes from 700 to 1500). Which computational method scales better, sequential or parallel?

Now change the `filename` to `"twoBigPrimes.txt"`. What is the difference in execution time between the sequential and parallel solution?

Do you think using distributed computing would have a major performance difference from parallel computing for a computation of this size? Why or why not?

Remember Mersenne Primes from the error type portion of this exercise? Here's a video about how these primes are discovered and checked using distributed computing: https://www.youtube.com/watch?v=I7cAZndWkvA.