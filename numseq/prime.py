def primes(n):
    return [i for i in range(1, n+1) if i % 2 != 0]


def is_prime(m):
    if m % 2 != 0:
        return True
    return False
