
for loop 
-----------
for var in seq:
    #stmts

s='python programming'
for i in s:
    print(i)

l=[3,4,5,56,32,32]
for i in l:
    print(i)

prices=(43,546,76,787,4325,76253)
for i in prices:
    print(i)
    
names={'tharun','prasad','vinod','nikhil'}
for var in names:
    print(var)

d={1:'prasad',2:'kiran',3:'rahul',4:'vinay'}
for name in d:
    print(name,d[name])



#range function
range(start,end+1,step)
for i in range(1,11):
    print(i)

for i in range(2,21,2):
    print(i)

for i in range(5,101,5):
    print(i)

for i in range(5,0,-1):
    print(i)

for i in range(19,0,-2):
    print(i)   

s='python programming langauge'
for i in range(len(s)):
    print(i,s[i])       

s=['apple','banana','gauve','grapes']
for i in range(len(s)):
    print(i,s[i])

s=(67,3,65,67,76576,43243)
for i in range(len(s)):
    print(i,s[i]) 
s=[655,35,765,786,543]
for i in range(len(s)):
    print(i,s[i])

s=[3,7,54,4678,3,5,8745,]
for i in enumerate(s):
    print(i[0],i[1])

d={1:2,3:4,44:5,5:6}
for i in enumerate(d):
    print(i[0],i[1],d[i[1]])
    
for i in range(1,11):
    if i==5:
        break
    print(i)
    
for i in range(1,11):
    if i==5:
        break
    print(i) 
else:
    print('loop iterated')  

l=[23,434,54,54656,7,6768,78,9,89,8,9,]
n=int(input('enter number'))
for i in l:
    if i==n:
        print(i,'found')
        break
else:
    print(n,'not found') 

pin=2345
for i in range(5):
    epin=int(input('enter the pin '))
    if epin==pin:
        print('unclock phone')
        break
    else:
        print('invalid pin')
else:
    print('try after 30 seconds')

n=int(input('enter a number'))
for i in range(2,n//2+1):
    if n%i==0:
        print('it is a prime number')
        break
else:
    print('it is not a prime number')
