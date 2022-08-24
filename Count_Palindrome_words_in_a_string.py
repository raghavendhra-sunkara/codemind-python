s=input()
s=s.lower()
s=s.split(' ')
c=0
for i in range(len(s)):
    if s[i]==s[i][::-1]:
        c+=1
print(c)