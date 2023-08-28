def divisible10(a: int):
    sum = 0
    while a > 0:
        b = a % 10
        a //= 10
        sum += b
    return sum % 10 == 0


def spaceNum(a: str):
    for i in range(len(a) - 1):
        if int(a[i]) - int(a[i + 1]) != 2 and int(a[i + 1]) - int(a[i]) != 2:
            return False
    return True


t = int(input())
for i in range(t):
    n = int(input())
    if divisible10(n) and spaceNum(str(n)):
        print("YES")
    else:
        print("NO")
