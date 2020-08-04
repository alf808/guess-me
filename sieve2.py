MAX_PRIME = 100

sieve = [True] * MAX_PRIME
prime_list = []
for i in range(2, MAX_PRIME):
    if sieve[i]:
        prime_list.append(i)
        for j in range(i*i, MAX_PRIME, i):
            sieve[j] = False
for idx, item in enumerate(prime_list):
    print(f"{idx+1}: {item}")
