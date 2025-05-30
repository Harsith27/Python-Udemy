import sys
def josephus(n,k,st,arr):
    if len(arr)==1:
        return arr[0]
    d=(st+k-1)%n
    arr.pop(d)
    return josephus(n-1,k,d,arr)

n=int(input())
k=int(input())
arr=[]
st=0
arr=list(range(1,n+1)) 
print(josephus(n,k,st,arr))
sys.exit()






n=int(input())
k=int(input())
arr=[]
st=0
for i in range(1,n+1):
    arr.append(i)
while(len(arr)!=1):
    d=(st+k-1)%n
    arr.pop(d)
    st=d
    n=n-1
print(arr[0])







