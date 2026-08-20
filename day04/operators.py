Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #python operators
>>> #arithemetical opearaor
>>> a=10
>>> b=5
>>> a+b
15
>>> a-b
5
>>> a*b
50
>>> a/b
2.0
>>> a//b
2
>>> a%b
0
>>> #comparision operator
>>> a>b
True
>>> a<b
False
>>> a<=b
False
>>> a>=b
True
>>> a==b
False
>>> a!=b
True
>>> #assignment operator
>>> a=10
>>> a+=5
>>> a
15
>>> a-=3
>>> a
12
>>> a*=2
>>> a
24
>>> a%=12
>>> a
0
>>> a//=10
>>> a
0
>>> a/=5
>>> a
0.0
>>> a=2
>>> a**=2
>>> a
4
>>> #relational operator
>>> 
>>> password=True
>>> email=False
>>> password and email
False
>>> password or email
True
>>> login= True
>>> login=False
>>> display_products = True
>>> login or display_products
True
>>> 's' in 'aeiou'
False
>>> 's' not in 'aeiou'
True
>>> not 3%2==0
True
>>> 3%2==0
False
>>> #mebership operator
>>> #used for list,string,tuple,dictionaries
>>> s='hellow world'
>>> 'hellow' in s
True
>>> 'world' not in s
False
>>> fruits=['apple','banana','pineapple']
>>> a in fruits
False
>>> 'a' in fruits
False
>>> 'apple' in fruits
True
>>> mango not in fruit
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    mango not in fruit
NameError: name 'mango' is not defined
>>> 'mango' not in fruits
True
>>> pushpa={'actor':'aa','director':'sukumar','actress':'srivalli'}
>>> print(pushpa)
{'actor': 'aa', 'director': 'sukumar', 'actress': 'srivalli'}
>>> actor in pushpa
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    actor in pushpa
NameError: name 'actor' is not defined
>>> 'actor' in pushpa
True
>>> 'aa' in pushpa
False
>>> 'actress' not in pushpa
False
>>> 'srivalli' not in pushpa
True
>>> game={'pubg','free fire','ludo'}
>>> 'pubg' not in game
False
>>> 'pubg' in game
True
>>> #identity operator
>>> l=[1,2,3,4]
>>> m=[1,2,3,4]
>>> l is m
False
>>> l is not m
True
>>> n=m
>>> n is m
True
>>> id(l)
2179543820424
>>> id(m)
2179548158024
>>> id(n)
2179548158024
>>> #bitwise operator
>>> 
>>> #& | ^ ~ << >>
>>> 2>>
SyntaxError: invalid syntax
>>> 2=20
SyntaxError: can't assign to literal
>>> 8>>2
2
>>> 
