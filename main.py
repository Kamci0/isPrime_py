import math


def isprime(num):
    if num <= 1:
        return False
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
            return True


def sito(nums):
    numbers = [True for _ in range(1, nums)]
    primes = []
    for i in range(1, len(numbers)):
        if i <= 1:
            numbers[i] = False
        else:
            if numbers[i]:
                primes.append(i)
                for j in range(i, len(numbers), i):
                    numbers[j] = False

    return primes


print(isprime(47))
print(sito(15))
