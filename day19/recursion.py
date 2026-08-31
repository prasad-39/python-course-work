'''def show(n):
    if n==11:
        return
    show(n+1)
    print(n)
print(show(1))

def display(name,ind):
    if ind==len(name):
        return
    display(name,ind+1)
    print(name[ind],end='') 
display('prasad',0)




s=input('enter string')
w=int(input('enter width'))
def show(s,i,w):
    if len(s)-w+1==i:
        return
    print(s[i:i+w])
    show(s,i+1,w)
show(s,0,w)


l=[12,23,232,434,343,54,5454,54,55,65,65]
def show(l,i=0):
    if i==len(l):
        return 0
    return l[i]+show(l,i+1)
print(show(l)) 

n=87522
def display(n):
    if n==0:
        return 0
    return n%10 +display(n//10)
print(display(n))

def dis(n):
    if n==1:
        return 1
    return n*dis(n-1)
print(dis(5))
print(dis(52))

n=int(input('enter the number :'))
if n==1:
    print(0)
elif n==2:
    print(0,1)
else:
    a,b=0,1
    print(a,b)
    for i in range(n-2):
        a,b=b,a+b
        print(b,end=' ')

def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fibo(n-1)+fibo(n-2)
for i in range(20):
    print(fibo(i),end=' ')
'''


