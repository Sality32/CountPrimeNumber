def countPrime(n):
    isPrime = []
    for i in range (n):
        isPrime.append(True)
    i = 2
    while i*i < n:
        j = i*i
        if isPrime[i]:
            while j < n:
                isPrime[j] = False
                j += i
        else: pass
        i += 1
    count = 0
    i = 2
    while i<n:
        if isPrime[i]:
            count += 1
        i += 1
    return count

rsl = countPrime(10)
print(rsl)