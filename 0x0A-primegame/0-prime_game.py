def isWinner(x, nums):
    # function to generate a list of prime numbers up to n
    def generate_primes(n):
        primes = [True] * (n+1)
        primes[0] = primes[1] = False
        for i in range(2, int(n**0.5)+1):
            if primes[i]:
                for j in range(i**2, n+1, i):
                    primes[j] = False
        return [i for i in range(2, n+1) if primes[i]]

    maria_wins = ben_wins = 0
    for n in nums:
        primes = generate_primes(n)
        turn = 1
        while primes:
            # Maria's turn
            if turn == 1:
                for prime in primes:
                    if n % prime == 0:
                        primes.remove(prime)
                        for i in range(prime, n+1, prime):
                            if i in primes:
                                primes.remove(i)
                        break
                else:
                    ben_wins += 1
                    break
            # Ben's turn
            else:
                for prime in primes:
                    if n % prime == 0:
                        primes.remove(prime)
                        for i in range(prime, n+1, prime):
                            if i in primes:
                                primes.remove(i)
                        break
                else:
                    maria_wins += 1
                    break
            turn = 3 - turn

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
