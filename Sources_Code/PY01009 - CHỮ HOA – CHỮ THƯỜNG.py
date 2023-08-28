def check(s):
    count = 0
    for i in s:
        if i >= "a" and i <= "z":
            count += 1
        else:
            count -= 1
    if count >= 0:
        return 1
    else:
        return 2


s = input()
if check(s) == 1:
    print(s.lower())
else:
    print(s.upper())
