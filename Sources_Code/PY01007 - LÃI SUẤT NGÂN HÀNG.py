t = int(input())
while t > 0:
    year=0
    a=input().split()
    n,x,m=float(a[0]),float(a[1]),float(a[2])
    lai=1+x/100
    while n<m:
        n*=lai
        year+=1
    print(year)
    t -= 1
