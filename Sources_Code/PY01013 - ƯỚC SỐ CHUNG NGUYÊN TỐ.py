from cmath import sqrt

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def isPrime(a):
    if a <= 1:
        return False
    for i in range(2, int(sqrt(float(a)).real) + 1):
        if a % i == 0:
            return False
    return True

n = int(input())
for i in range(n):
    A = input().split()
    a = int(A[0])
    b = int(A[1])
    c = gcd(a, b)
    count = 0
    while c > 0:
        count += c%10
        c //= 10
    if isPrime(count):
        print("YES")
    else:
        print("NO")
