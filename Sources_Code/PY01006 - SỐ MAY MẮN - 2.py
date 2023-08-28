t = int(input())
while t > 0:
    s = input()
    k = 1
    for x in s:
        if x != "4" and x != "7":
            k = 0
            break
    if k == 0:
        print("NO")
    else:
        print("YES")
    t -= 1
