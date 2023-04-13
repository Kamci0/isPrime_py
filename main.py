import math


def isprime(num):
    if num <= 0:
        return False
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
            else:
                return True


print(isprime(8))