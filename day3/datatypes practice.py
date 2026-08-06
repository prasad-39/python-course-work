Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #int
>>> a=10
>>> #float
>>> b=2.55
>>> #complex
>>> c=4+5j
>>> type(a)
<class 'int'>
>>> type(b)
<class 'float'>
>>> type(c)
<class 'complex'>
>>> #string
>>> E= "prasad"
>>> type(E)
<class 'str'>
>>> #list
>>> marks=[80,98,90,90]
>>> type(marks)
<class 'list'>
>>> id(marks)
2329617722760
>>> marks.add(99)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    marks.add(99)
AttributeError: 'list' object has no attribute 'add'
>>> marks.insert(99)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    marks.insert(99)
TypeError: insert() takes exactly 2 arguments (1 given)
>>> marks.append(99)
>>> print(marks)
[80, 98, 90, 90, 99]
>>> id(marks)
2329617722760
>>> tup=(10,20,30,40,50)
>>> print(tup)
(10, 20, 30, 40, 50)
>>> a=[10]
>>> print(a)
[10]
>>> hh={20,30,30,40,50}
>>> print{hh}
SyntaxError: invalid syntax
>>> print(hh)
{40, 50, 20, 30}
>>> 
