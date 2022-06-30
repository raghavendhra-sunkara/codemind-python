v=int(input())
k=0
while(v!=1):
    if v%2==0:
        v//=2
    elif v%3==0:
        v//=3
    elif v%5==0:
        v//=5
    else:
        k+=1
        break
if k!=0:
    print("Not Ugly Number")
else:
    print("Ugly Number")