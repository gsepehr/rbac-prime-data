"""
Proofs that none of the multiplication of n-th first prime numbers with size x is divisible by other prime numbers

Finds X (600) first prime numbers before Y (1500), holds them in (P)
Then selects different sizes of [2, X] and loops over sizes (i)
    We shift in the array and create subarray (N) with size of (i)
    We do a multiplication of the items in sub array (N) and hold the result in (A)
    We extract other items in the main list (P - N), and see if A is divisible by items in this list
        If its divisible then the mathematical proof fails.
"""

numr = 15000
primes = []

for n in range(1, numr):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        primes.append(n)


primes = primes[1:600]


for size in range(2, len(primes)):
    for shift in range(len(primes) - 2, -1, -1):
        selected = primes[shift: shift + size]
        check_list = [x for x in primes if x not in selected]

        output = 1
        for item in selected:
            output *= item

        for item in check_list:
            if output % item == 0:
                print(selected, output, item)


print("Finished")
