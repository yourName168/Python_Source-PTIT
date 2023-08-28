n = input()
count = 0
res = ""
for i in range(len(n) - 1, -1, -1):
    if count != 3:
        res += str(n[i])
        count += 1
    else:
        count = 1
        res += ","
        res += str(n[i])

res = res[::-1]
print(res)
