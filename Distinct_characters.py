s=input()
s=s.lower()
s=list(s)
a=[]
for i in s:
    if s.count(i)==1:
        a.append(i)
a.sort()
st='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'
for i in a:
    if i==' ':
        continue
    st+=i
print(st)