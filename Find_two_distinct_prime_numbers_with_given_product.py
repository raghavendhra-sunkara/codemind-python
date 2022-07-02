def pri(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
a=[]
for i in range(2,n):
    if n%i==0 and pri(i):
        a.append(i)
if a==[]:
    print(-1)
else:
    print(*a)
