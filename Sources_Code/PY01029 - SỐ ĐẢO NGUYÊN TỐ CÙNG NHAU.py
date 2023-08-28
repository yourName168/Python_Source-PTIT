def gcd(a: int, b: int):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def numReverse(a: int):
    res = 0
    while a > 0:
        b = a % 10
        res = res * 10 + b
        a //= 10
    return res


t = int(input())
for i in range(t):
    a = int(input())
    b = numReverse(a)
    if gcd(a, b) != 1:
        print("NO")
    else:
        print("YES")
