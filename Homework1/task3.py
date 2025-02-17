def num_test(x):
    if x > 0:
        return "positive"
    elif x < 0:
        return "negative"
    else:
        return 0

def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes(num=10):
    prime_nums = []
    n = 2
    while len(prime_nums) < num:
        if prime(n):
            prime_nums.append(n)
        n += 1
    print(prime_nums)
    return prime_nums

primes()

def sumOfNum():
    total = 0
    i = 1
    for i in range(101):
        total += i
        i += 1
    return total

def test_num():
    assert num_test(9) == "positive"
    assert num_test(-7) == "negative"
    assert num_test(0) == 0

def test_prime():
    assert prime(2) is True
    assert prime(3) is True
    assert prime(4) is False
    assert prime(11) is True
    assert prime(15) is False

def test_primes():
    assert primes() == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    
def test_sum():
    assert sumOfNum() == 5050
