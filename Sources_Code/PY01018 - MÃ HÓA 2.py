while(True):
    A=input().split()
    if(int(A[0])==0):break
    P = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
    k=int(A[0])
    S=str(A[1])
    res=""
    for i in range(len(S)):
        if(str(S[i])=='.'):
            binaryNum=(27+k)%28
        elif str(S[i])=='_':
            binaryNum=(26+k)%28
        else:
            binaryNum=(ord(str(S[i]))-ord('A')+k)%28
        res+=P[binaryNum]
    res="".join(reversed(res))
    print(res)