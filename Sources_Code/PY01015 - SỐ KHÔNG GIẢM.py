t = int(input())
for i in range(t):
    k = 1
    s = input()
    for j in range(len(s) - 1):
        if s[j] > s[j + 1]:
            k = 0
            break
    if k == 0:
        print("NO")
    else:
        print("YES")
