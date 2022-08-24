def fun(st):
    a='QWERTYUIOPASDFGHJKLZXCVBNM'
    for i in a:
        if i not in st.upper():
            return False
    else:
        return True
        
st=str(input())
if fun(st):
    print('True')
else:
    print('False')