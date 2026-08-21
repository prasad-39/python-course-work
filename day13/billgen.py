'''data = {
    'book':50,
    'pen':10,
    'bag':500,
    'lunch box':200,
    'shoe':300,
    'socks':100,
    'colours':50,

}
for i in data:
    print(i)
items=input('enter your products:').split()
print('---------bill------------')
bill=0
for i in items:
    print(i.ljust(20),data[i])
    if i in data and i in items:
        bill=data[i]+bill
print('Total bill is',bill)'''

'''
s='python programming'
d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
'''

s='aaaassssssssfffffffffffffdvvvvvvvvvv'
c=1
res=''
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        c+=1
    else:
        res+=s[i]+str(c)
        c=1
print(res+s[i]+str(c))
