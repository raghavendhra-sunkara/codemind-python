s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
s1=list(s1)
s2=list(s2)
c=0
if len(s1)==len(s2):
    for i in s1:
        if i in s2:
            c+=1
    if c==len(s1):
        print(True)
    else:
        print(False)
else:
    print(False)