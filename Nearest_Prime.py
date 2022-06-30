n=int(input())
for i in range(1,n+1,1):
    a=int(input())
    b=a
    for i in range(a,1,-1):
        for j in range(2,i,1):
            if i%j==0:
                break
        else:
            c=i
            break
    while a:
        for j in range(2,a,1):
            if a%j==0:
                break
        else:
            d=a
            break
        a+=1
    if b-c<=d-b:
        print(c)
    else:
        print(d)