Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.

>>> # int
>>> a = 10
>>> type(a)
<class 'int'>

>>> # float
>>> b = 2.55
>>> type(b)
<class 'float'>
>>> # complex
>>> c = 4 + 5j
>>> type(c)
<class 'complex'>

>>> # string
>>> E = "prasad"
>>> type(E)
<class 'str'>

>>> # list
>>> marks = [80, 98, 90, 90]
>>> type(marks)
<class 'list'>

>>> id(marks)
2329617722760

>>> marks.append(99)
>>> print(marks)
[80, 98, 90, 90, 99]

>>> id(marks)
2329617722760

>>> # tuple
>>> tup = (10, 20, 30, 40, 50)
>>> print(tup)
(10, 20, 30, 40, 50)

>>> # list with one element
>>> a = [10]
>>> print(a)
[10]

>>> # set
>>> hh = {20, 30, 30, 40, 50}
>>> print(hh)
{40, 50, 20, 30}


# Type Conversion

>>> # int
>>> n = 10
>>> float(n)
10.0

>>> complex(n)
(10+0j)

>>> list(n)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    list(n)
TypeError: 'int' object is not iterable

>>> tuple(n)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    tuple(n)
TypeError: 'int' object is not iterable

>>> dict(n)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    dict(n)
TypeError: 'int' object is not iterable

>>> bool(n)
True

>>> str(n)
'10'


>>> # float
>>> c = 3.4
>>> int(c)
3

>>> complex(c)
(3.4+0j)

>>> list(c)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    list(c)
TypeError: 'float' object is not iterable

>>> tuple(c)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    tuple(c)
TypeError: 'float' object is not iterable

>>> dict(c)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    dict(c)
TypeError: 'float' object is not iterable

>>> bool(c)
True

>>> str(c)
'3.4'


>>> # string
>>> w = 'prasad'

>>> int(w)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    int(w)
ValueError: invalid literal for int() with base 10: 'prasad'

>>> float(w)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    float(w)
ValueError: could not convert string to float: 'prasad'

>>> set(w)
{'s', 'p', 'a', 'd', 'r'}

>>> list(w)
['p', 'r', 'a', 's', 'a', 'd']

>>> tuple(w)
('p', 'r', 'a', 's', 'a', 'd')

>>> dict(w)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    dict(w)
ValueError: dictionary update sequence element #0 has length 1; 2 is required

>>> bool(w)
True

>>> # complex
>>> c = 2 + 4j

>>> int(c)
Traceback (most recent call last):
  File "<pyshell#29", line 1, in <module>
    int(c)
TypeError: can't convert complex to int

>>> float(c)
Traceback (most recent call last):
  File "<pyshell#30", line 1, in <module>
    float(c)
TypeError: can't convert complex to float

>>> str(c)
'(2+4j)'

>>> list(c)
Traceback (most recent call last):
  File "<pyshell#32", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable

>>> tuple(c)
Traceback (most recent call last):
  File "<pyshell#33", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable

>>> bool(c)
True

>>> # dictionary
>>> bahubali = {
... 'actor': 'prabhas',
... 'director': 'SSR',
... 'actress': 'anushka'
... }

>>> print(bahubali)
{'actor': 'prabhas', 'director': 'SSR', 'actress': 'anushka'}

>>> list(bahubali)
['actor', 'director', 'actress']

>>> set(bahubali)
{'actor', 'actress', 'director'}

>>> tuple(bahubali)
('actor', 'director', 'actress')

>>> bool(bahubali)
True

>>> str(bahubali)
"{'actor': 'prabhas', 'director': 'SSR', 'actress': 'anushka'}"

>>> complex(bahubali)
Traceback (most recent call last):
  File "<pyshell#44", line 1, in <module>
    complex(bahubali)
TypeError: complex() first argument must be a string or a number, not 'dict'

>>> int(bahubali)
Traceback (most recent call last):
  File "<pyshell#45", line 1, in <module>
    int(bahubali)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'dict'

>>> float(bahubali)
Traceback (most recent call last):
  File "<pyshell#47", line 1, in <module>
    float(bahubali)
TypeError: float() argument must be a string or a number, not 'dict'