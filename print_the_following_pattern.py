n=int(input())
p=65
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        print(chr(p),end=' ')
    p+=1
    print()