arr=list(map(int,input().split()))
ma=0
for i in range(len(arr)):
    for j in range(len(arr)):
        if (i!=j):
            pro=(arr[i]-1)*(arr[j]-1)
            if pro>ma:
                ma=pro
print(ma)