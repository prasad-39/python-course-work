Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.

>>> a = 10
>>> a
10
>>> # input()
>>> c = input()
3322
>>> c
'3322'
>>> b = input("enter a number :")
enter a number :55
>>> print(b)
55
>>> # Type conversion with input()
>>> marks = int(input('enter your marks:'))
enter your marks:99
>>> marks
99
>>> type(marks)
<class 'int'>
>>> type(b)
<class 'str'>
>>> cgpa = float(input('enter your cgpa:'))
enter your cgpa:8.8
>>> print(cgpa)
8.8
>>> type(cgpa)
<class 'float'>


>>> # Converting input into a list
>>> fruits = list(input('enter fruit names:'))
enter fruit names:apple
>>> fruits
['a', 'p', 'p', 'l', 'e']

>>> # split() is a string method
>>> names = input('enter the names :')
enter the names :prasad nikhil bunny
>>> names.split()
['prasad', 'nikhil', 'bunny']

>>> actors = input('enter actor names:')
enter actor names:prabhas,nani,mahesh
>>> actors.split(',')
['prabhas', 'nani', 'mahesh']


>>> # Creating a set from input
>>> avengers = set(input('enter the avengers names:').split())
enter the avengers names:thor captain hulk spidey
>>> avengers
{'thor', 'hulk', 'spidey', 'captain'}

>>> # Set removes duplicate elements
>>> avengers = set(input('enter the avengers names:').split())
enter the avengers names:hulk hulk captain spidey
>>> avengers
{'hulk', 'spidey', 'captain'}


>>> # Creating a tuple from input
>>> mobiles = tuple(input('enter mobile names:').split())
enter mobile names:iqoo redmi oneplus vivo
>>> mobiles
('iqoo', 'redmi', 'oneplus', 'vivo')


>>> # Creating a list using split()
>>> marks = input('enter the marks:').split()
enter the marks:80 90 70 90
>>> marks
['80', '90', '70', '90']


>>> # map()
>>> map(int, marks)
<map object at 0x000002CBBA859470>
>>> marks
['80', '90', '70', '90']
>>> list(map(int, marks))
[80, 90, 70, 90]


>>> # Taking multiple integer values as input
>>> marks = list(map(int, input('enter your marks :').split()))
enter your marks :60 70 80 90 80
>>> marks
[60, 70, 80, 90, 80]

>>> # Creating a tuple using map()
>>> marks = tuple(map(int, input('enter your marks :').split()))
enter your marks :60 70 80 90
>>> marks
(60, 70, 80, 90)

>>> # Creating a list of float values
>>> marks = list(map(float, input('enter your marks :').split()))
enter your marks :90 80 70 88
>>> marks
[90.0, 80.0, 70.0, 88.0]

>>> # List unpacking
>>> a, b = [1, 2]
>>> a
1
>>> b
2
>>> # Tuple unpacking
>>> a, b = (3, 4)
>>> a
3
>>> b
4

>>> # Input and unpacking
>>> email, password = input('enter the mailid and password:').split()
enter the mailid and password:prasad 3322
>>> email
'prasad'
>>> password
'3322'

>>> # Multiple values using map() and unpacking
>>> marks10, marks12, bscmarks = list(map(int, input().split()))
90 80 70
>>> marks10
90
>>> marks12
80
>>> bscmarks
70

>>> # eval()
>>> status = eval(input())
50
>>> status
50
>>> type(status)
<class 'int'>

>>> # eval() can evaluate different data types
>>> status = eval(input())
True
>>> status
True
>>> type(status)
<class 'bool'>

>>> # eval() with a complex number
>>> comp = eval(input())
4+4j
>>> type(comp)
<class 'complex'>

>>> # eval() with a dictionary
>>> dic = eval(input('provide key and value:'))
provide key and value:{2:3}
>>> dic
{2: 3}
>>> type(dic)
<class 'dict'>

>>> # Multiple key-value pairs using eval()
>>> dic = eval(input('provide key and value:'))
provide key and value:{2:3, 4:6}
>>> dic
{2: 3, 4: 6}
>>> type(dic)
<class 'dict'>