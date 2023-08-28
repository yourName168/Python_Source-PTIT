t = int(input())
for j in range(t):
    n = int(input())
    res = [1]
    num = [1]
    for i in range(2, n+1):
        count = 0
        while n % i == 0:
            count += 1
            n //= i
        if count != 0:
            res.append(i)

            num.append(count)
    for i in range(0, len(res)):
        if i == 0:
            print("1 ", end="")
        else:
            print("* %d^%d " % (res[i], num[i]), end="")
    print()
