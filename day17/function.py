'''
def functionname(arg):
    #statements
    return(opt)
    
functionname(para)

def gst(price):
    print('original price:',price)
    print('final price',price+price*0.18)
gst(1000)
gst(700)
gst(3443)
gst(500)

def table(n):
    print({n},'table')
    print('-------------------')
    for i in range(1,11):
        print(f'{n} * {i} = {n*i}')

for i in range(1,21):
    table(i)

def isleap(n):
    if n%400==0 or (n%4==0 and n%100!=0):
        return 'leap year'
    else:
        return 'not a leap year'
print(isleap(2012))
print(isleap(2020))
print(isleap(2013))

def prime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            print({n},'it is not a prime number')
            break
        else:
            print({n},'it is a prime number')
prime(8)
'''


def display(name,email,pwd=None):
    print('name:',name)
    print('email:',email)
    print('pwd :',pwd)

#positional arguments
display('prasad','prasad0099@gmail.com','prasad123')
display('prasad0099@gmail.com','prasad','prasad123')

#keyword arguments
display(pwd='prasad123',name='prasad',email='prassad0099@gmail.com')
display(email='prasad009@gmail.com',pwd='prasad123',name='prasad') 

#default arguments
display('prasad','prasad0099@gmail.com')

#positional/variable length arguments
def dis(*name):
    print(name)

dis('prasad')
dis('prasad','naveen')
dis('prasad','naveen','vinod')

#key value pairs
def dic(**names):
    print(names)
dic(name1='prasad')
dic(name1='prasad',name2='ravi')

