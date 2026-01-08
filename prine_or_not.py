n = int(input("Enter a number: "))

if n <= 1:
    print(False)
else:
    is_prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    print(is_prime)
# write this into opttimised code
from math import isqrt

n = int(input("Enter a number: "))

if n <= 1:
    print(False)
elif n == 2:
    print(True)
elif n % 2 == 0:
    print(False)
else:
    for i in range(3, isqrt(n) + 1, 2):
        if n % i == 0:
            print(False)
            break
    else:
        print(True)

