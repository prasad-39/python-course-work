Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a=10
>>> 
>>> a
10
>>> c=input()
3322
>>> c
'3322'
>>> b=input("enter a number :")
enter a number :55
>>> print(b)
55
>>> marks=int(input('enter your marks:'))
enter your marks:99
>>> marks
99
>>> type(marks)
<class 'int'>
>>> type(b)
<class 'str'>
>>> cgpa=float(input('enter your cgpa:'))
enter your cgpa:8.8
>>> print(cgpa)
8.8
>>> type(cgpa)
<class 'float'>
>>> fruits=list(input('enter fruit names:'))
enter fruit names:apple,banana,jack fruit
>>> fruits
['a', 'p', 'p', 'l', 'e', ',', 'b', 'a', 'n', 'a', 'n', 'a', ',', 'j', 'a', 'c', 'k', ' ', 'f', 'r', 'u', 'i', 't']
>>> fruits.split(',')
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    fruits.split(',')
AttributeError: 'list' object has no attribute 'split'
>>> fruits.split()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    fruits.split()
AttributeError: 'list' object has no attribute 'split'
>>> names=nikhil prasad bunny
SyntaxError: invalid syntax
>>> names=input('enter the names :')
enter the names :prasad nikhil bunny
>>> names.split()
['prasad', 'nikhil', 'bunny']
>>> actors=input('enter a actor name:')
enter a actor name:phabhas mahesh AA 
>>> actors=input('enter a actor name:')
enter a actor name:prabhas,nani,mahesh
>>> actors.split(',')
['prabhas', 'nani', 'mahesh']
>>> avengers=input('entere the avengers names:')
entere the avengers names:thor ironman captain spidy
>>> avengers=input('entere the avengers names:')
entere the avengers names:
	thor ironman captain spidy
>>> avengers=set(input('entere the avengers names:').split())
entere the avengers names:
>>> thor captain hulk spidey
SyntaxError: invalid syntax
>>> avengers=set(input('entere the avengers names:').split())
entere the avengers names:thor captain hulk spidey 
>>> avenhgers
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    avenhgers
NameError: name 'avenhgers' is not defined
>>> avengers
{'thor', 'hulk', 'spidey', 'captain'}
>>> avengers=set(input('entere the avengers names:').split())
entere the avengers names:hulk hulk captain spidey
>>> avengers
{'hulk', 'spidey', 'captain'}
>>> mobiles=tuple(input('enter mobile names"').split())
enter mobile names"iqoo redmi oneplus vivo
>>> mobiles
('iqoo', 'redmi', 'oneplus', 'vivo')
>>> marks=input('enter the marks:').split()
enter the marks:80 90 8 0 70 90
>>> marks
['80', '90', '8', '0', '70', '90']
>>> map(int,marks)
<map object at 0x000002CBBA859470>
>>> marks
['80', '90', '8', '0', '70', '90']
>>> list(map(int,marks))
[80, 90, 8, 0, 70, 90]
>>> marks= list(map(int,input('enter your marks :').split()))
enter your marks :60 70 80 90 80
>>> marks
[60, 70, 80, 90, 80]
>>> marks=tuple(map(int,input('enter your marks :').split()))
enter your marks :60 7 0 8 0 90 
>>> marks
(60, 7, 0, 8, 0, 90)
>>> avengers=set(map(list,input('enter the marks:').split()))
enter the marks:50 60 70 90 8 0
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    avengers=set(map(list,input('enter the marks:').split()))
TypeError: unhashable type: 'list'
>>> marks=list(map(float,input('enter your marks :').split()))
enter your marks :90 80 7 0 88 
>>> marks
[90.0, 80.0, 7.0, 0.0, 88.0]
>>> a,b=[1,2]
>>> a
1
>>> b
2
>>> a,b=(3,4)
>>> email,password=input('enter the emailid and password:').split())
SyntaxError: invalid syntax
>>> email,password=input(('enter the emailid and password:').split())
['enter', 'the', 'emailid', 'and', 'password:']20 30 
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    email,password=input(('enter the emailid and password:').split())
ValueError: too many values to unpack (expected 2)
>>> email,password=input('enter the mailid and password:').split()
enter the mailid and password:prasad 3322
>>> email
'prasad'
>>> password
'3322'
>>> 10thmarks,12thmarks,bscmarks=list(map(int,input().split()))
SyntaxError: invalid syntax
>>> marks10,marks12,bscmarks=list(map(int,input().split()))
90 80 70
>>> marks10
90
>>> status
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    status
NameError: name 'status' is not defined
>>> status =eval(input())

Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    status =eval(input())
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> status=eval(input())
status
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    status=eval(input())
  File "<string>", line 1, in <module>
NameError: name 'status' is not defined
>>> status=eval(input())
50
>>> status
50
>>> type(status)
<class 'int'>
>>> bunny=eval(input())
prasad
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    bunny=eval(input())
  File "<string>", line 1, in <module>
NameError: name 'prasad' is not defined
>>> prasad=eval(input('input eyyi raa:'))
input eyyi raa:True
>>> type(prasad)
<class 'bool'>
>>> prasad
True
>>> comp=eval(input())
4+4j
>>> type(comp)
<class 'complex'>
>>> dic=eval(input('provide key and value'))
provide key and value2:3
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    dic=eval(input('provide key and value'))
  File "<string>", line 1
    2:3
     ^
SyntaxError: invalid syntax
>>> dic=eval(input('provide key and value'))
provide key and value{2:3}
>>> dic
{2: 3}
>>> type(dic)
<class 'dict'>
>>> dic=eval(input('provide key and value'))
provide key and value{2:3,4:6}
>>> dic
{2: 3, 4: 6}
>>> 
