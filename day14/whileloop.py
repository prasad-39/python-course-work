
i=1
while i<=10:
    print(i)
    i+=1

i=10
while i>=1:
    print(i)
    i-=1
    
i=5
while i<=50:
    print(i)
    i+=5 

s='python programming'
i=0
while i<len(s):
    print(s[i])
    i+=1


s='python programming'
i=len(s)-1
while i>=0:
    print(s[i])
    i-=1 

l=[12,23,434,545,65]
i=0
while i<len(l):
    print(l[i])
    i+=1 
n = 8765
while n>0:
    print(n%10)
    n//=10

n=8765
sum=0
while n>0:
    sum+=n%10
    n//=10
print(sum)

n=1234
pro=1
while n>0:
    pro*=n%10 
    n//=10
print(pro)

n=2345
res=0
while n>0:
    rem=n%10
    res=res*10+rem
    n//=10 
print(res)

n=862345
res=0
while n>0:
    rem=n%10
    if rem%2==0:
        res+=rem
    n//=10
print(res)

l=[2,3,4,5,66,654,33,22,2,0,0,0,0,2,2,2,2,22,3,4,43,2,]
i=0
while 0 in l:
    l.remove(0)
print(l)

l=[2,3,4,5,56,67,7,7,4,24,2]
i,j=0,len(l)-1
while i<=j:
    if i==j:
        print(l[i])
    else:
        print(l[i]+l[j])
    i+=1
    j-=1
