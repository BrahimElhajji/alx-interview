#!/usr/bin/python3
"""Prime Game"""

def sieve_of_eratosthenes(n):
    """Use Sieve of Eratosthenes to find all primes up to n."""
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for multiple in range(i * i, n + 1, i):
                primes[multiple] = False
    return primes

def prime_count_up_to(n, primes):
    """Count how many primes are less than or equal to n."""
    count = 0
    for i in range(2, n + 1):
        if primes[i]:
            count += 1
    return count

def isWinner(x, nums):
    """Determine the winner of the game after x rounds."""
    if not nums or x < 1:
        return None

    # Precompute primes up to the largest number in nums
    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)

    # Dynamic programming to count primes up to each number
    prime_counts = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_counts[i] = prime_counts[i - 1]
        if primes[i]:
            prime_counts[i] += 1

    # Initialize score counters for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    # Simulate each round
    for n in nums:
        if prime_counts[n] % 2 == 1:
            maria_wins += 1  # Maria wins if there are an odd number of primes
        else:
            ben_wins += 1  # Ben wins if there are an even number of primes

    # Determine overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
