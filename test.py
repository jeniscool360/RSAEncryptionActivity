from main import RSA
import multiprocessing as mp
import time

def test_smallest_coprime():
    #good do nothing, bad give error
    assert RSA.smallest_coprime(4) == 3
    assert RSA.smallest_coprime(100) == 3
    assert RSA.smallest_coprime(2**100) == 3

def test_lcm():
    assert RSA.lcm(8, 12) == 24
    assert RSA.lcm(5, 12) == 60
    assert RSA.lcm(7, 9) == 63
    # TODO write some assertions for LCM

def test_encryption_boundary():
    p = 13
    q = 29
    rsa = RSA(p, q)
    # TODO demonstrate the boundary cases
    # Example assertions (replace 10 and 500 with boundary values)
    assert p * q -1 == rsa.c(rsa.m(p*q-1))
    assert p * q != rsa.c(rsa.m(p*q))

def test_rsa(prm):
    p = prm[0]
    q = prm[1]
    rsa = RSA(p, q)
    start = time.time()
    assert p*q-1 == rsa.c(rsa.m(p*q-1))
    print(f"RSA for {p}, {q} PASSED in {time.time()-start}")

def test_encryption_big():
    """
    See https://www.machinelearningplus.com/python/parallel-processing-python/ for more on parallel processing.
    This function compares sequential and parallel processing for the same test cases.
    """

    filename = "bigPrimes.txt"
    with open(filename) as f:
        primes = f.readlines()
        primes.pop(0)
        if len(primes)%2 != 0:
            primes.pop(0)
            primes = [(int(primes[i]), int(primes[i+1])) for i in range(0, len(primes), 2)]

        # Sequential execution
        print("Sequential execution tests")
        start = time.time()
        for prm in primes:
            test_rsa(prm)
        end = time.time()
        print(end-start)

        # Parallel execution
        processors = len(primes) if len(primes) < mp.cpu_count() else mp.cpu_count()
        print("Parallel execution tests with", processors, "processors")
        start = time.time()
        pool = mp.Pool(processors)
        pool.map(test_rsa, primes)
        pool.close()
        end = time.time()
        print(end-start)

if __name__ == "__main__":
    test_smallest_coprime()
    test_lcm()
    test_encryption_boundary()
    test_encryption_big()