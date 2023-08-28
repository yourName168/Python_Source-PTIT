t=int(input())
for i in range(t):
    s=input()
    count=1
    for j in range(len(s)):
        if(j!=len(s)-1 and s[j]==s[j+1]):
            count+=1
        else:
            print(str(count)+s[j],end="")
            count=1
    print()