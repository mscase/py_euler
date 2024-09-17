import math

def sieve(n):
    """Return a list of all prime numbers up to n (inclusive)."""
    if n < 2:
        return []

    # Step 1: Initialize the list of boolean values
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes

    # Step 2: Apply the sieve
    p = 2
    root_number = math.sqrt(n)
    while p <= root_number:
        if is_prime[p]:
            # Mark multiples of p as False
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1

    # Step 3: Collect and return the list of primes
    primes = [num for num, prime in enumerate(is_prime) if prime]
    return primes


if __name__ == "__main__":
    print (sieve(50))
