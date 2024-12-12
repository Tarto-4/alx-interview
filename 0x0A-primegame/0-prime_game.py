#!/usr/bin/python3

def isWinner(x, nums):
    """
    Determines the winner of the prime game.

    Args:
        x (int): Number of rounds.
        nums (list): List of 'n' values for each round.

    Returns:
        str: Name of the winner ('Maria' or 'Ben') or None if tied.
    """
    if not nums or x < 1:
        return None

    max_num = max(nums)
    
    # Sieve of Eratosthenes to precompute primes up to max_num
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime
    for i in range(2, int(max_num**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_num + 1, i):
                sieve[j] = False

    # Precompute the number of primes up to each number
    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if sieve[i] else 0)

    maria_wins = 0
    ben_wins = 0

    # Simulate each round
    for n in nums:
        # If the count of primes is odd, Maria wins; otherwise, Ben wins
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
