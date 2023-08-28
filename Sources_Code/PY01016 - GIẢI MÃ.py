t=int(input())
for i in range(t):
    s=input()
    for j in range(0,len(s)-1,2):
        charac=str(s[j])
        num=int(s[j+1])
        for k in range(num):
            print(charac,end="")
    print()