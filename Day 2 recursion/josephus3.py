def josephus(n,k):
    result=0
    for i in range(2,n+1):
        result=(result+k)%i
    return result

n,k=map(int,input().split())
print(josephus(n,k)+1)